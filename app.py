import base64
import json
import os
from urllib import error as urlerror
from urllib import request as urlrequest

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

CF_ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID")
CF_API_TOKEN = os.environ.get("CF_API_TOKEN")
CF_MODEL = os.environ.get("CF_MODEL", "@cf/black-forest-labs/flux-1-schnell")
CF_URL = f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/ai/run/{CF_MODEL}" if CF_ACCOUNT_ID else None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-image", methods=["POST"])
def generate_image():
    if not CF_ACCOUNT_ID or not CF_API_TOKEN:
        return jsonify({"error": "Server is missing CF_ACCOUNT_ID or CF_API_TOKEN. Set them in your .env file."}), 500

    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "").strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    payload = {"prompt": prompt}
    req = urlrequest.Request(
        CF_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {CF_API_TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlrequest.urlopen(req, timeout=120) as resp:
            content_type = (resp.headers.get("Content-Type") or "").split(";")[0]
            body = resp.read()
    except urlerror.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        return jsonify({"error": "Image generation failed", "details": details}), exc.code
    except urlerror.URLError as exc:
        return jsonify({"error": "Unable to reach Cloudflare", "details": str(exc)}), 502

    # flux-1-schnell returns JSON with a base64 string in result.image
    if content_type.startswith("application/json"):
        parsed = json.loads(body.decode("utf-8"))
        if not parsed.get("success", True):
            return jsonify({"error": "Image generation failed", "details": json.dumps(parsed.get("errors"))}), 502
        b64_image = parsed.get("result", {}).get("image")
        if not b64_image:
            return jsonify({"error": "Unexpected response shape from Cloudflare", "details": json.dumps(parsed)}), 502
        return jsonify({"img": f"data:image/png;base64,{b64_image}"})

    # Other models (e.g. SDXL) return raw image bytes directly
    if content_type.startswith("image/"):
        encoded = base64.b64encode(body).decode("utf-8")
        return jsonify({"img": f"data:{content_type};base64,{encoded}"})

    return jsonify({"error": "Unexpected response type from Cloudflare", "details": content_type}), 502


if __name__ == "__main__":
    app.run(debug=True)
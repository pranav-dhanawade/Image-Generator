import os
from bytez import Bytez
from dotenv import load_dotenv
from flask import Flask , render_template, request,jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate-images', methods=['POST'])
def images():
    data = request.get_json()
    user_prompt = data.get('prompt')
    print(user_prompt)
    load_dotenv()
    api_key = os.getenv("API_KEY") #Your API key here
    # insert your key
    sdk = Bytez(api_key)

    # choose your model
    model = sdk.model("openai/dall-e-2")

    # provide the model with input
    input = user_prompt

    # send to the model
    result = model.run(input)

    #output
    print({"error": result.error, "output": result.output})
    return jsonify({'img': result.output , 'error': result.error})


if __name__ == '__main__':
    app.run(debug=True)

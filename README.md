# Text-to-Image Generator

A full-stack **Text-to-Image Generator** built using **Flask** that converts natural language prompts into AI-generated images using the **OpenAI Image Generation API**. This project demonstrates API integration, secure environment variable handling, and a clean web interface using HTML, CSS, and JavaScript.

This project is designed to be **portfolio- and resume-ready**, following industry best practices.

---

## 🚀 Features

* Generate images from text prompts using AI
* Flask-based backend with REST-style API handling
* Clean frontend using HTML, CSS, and JavaScript
* Secure API key management using environment variables
* Beginner-friendly setup and structure

---

## 🛠 Tech Stack

### Backend

* Python
* Flask
* OpenAI API
* python-dotenv

### Frontend

* HTML
* CSS
* JavaScript

---

## 📦 Python Modules Used

The following modules are used in this project:

```python
import os
from bytez import Bytez
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
```

---

## 📁 Project Structure

```
text-to-image-generator/
├── static/
│   └── openimg.png
├── templates/
│   └── index.html
├── app.py
├── .gitignore
├── .env.example
└── README.md
```

---

## 🔐 Environment Variables Setup

This project uses environment variables to keep the API key secure.

### 1️⃣ Create a `.env` file

In the project root directory, create a file named `.env` and add your Hugging Face token:

```
HF_TOKEN=your_hugging_face_token_here
HF_IMAGE_ENDPOINT=https://router.huggingface.co/fal-ai/ideogram/v4/lora?_subdomain=queue
```

⚠️ **Do NOT upload `.env` to GitHub**. It is already ignored using `.gitignore`.

### 2️⃣ `.env.example`

A `.env.example` file is provided to show the required environment variables. Rename it to `.env` and add your actual API key.

---

## 🧪 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd text-to-image-generator
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install flask python-dotenv openai bytez
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---


## 🔒 Security Best Practices

* API keys are stored in `.env` files
* `.env` is excluded using `.gitignore`
* No sensitive data is committed to GitHub

---

## 📌 Notes

* Ensure you have a valid Hugging Face API token
* Internet connection is required for API requests
* This project is intended for learning and portfolio demonstration

---

## 📄 License

This project is open-source and available for educational and personal use.

---

## 👤 Author

**Pranav Dhanawade**
MCA Student | Full Stack Developer (Python & ReactJs)

---

⭐ If you found this project useful, consider giving it a star on GitHub!

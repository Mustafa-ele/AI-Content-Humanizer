from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    humanized_text = ""
    
    if request.method == "POST":
        input_text = request.form["input_text"]

        if input_text.strip():  # Ensure input is not empty
            try:
                # Choose the best Gemini model for rewriting
                model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

                # Generate humanized content
                response = model.generate_content(
                    f"Rewrite this text to sound natural and human-like:\n\n{input_text}"
                )

                # Get the output text
                humanized_text = response.text.strip()
            except Exception as e:
                humanized_text = f"Error: {str(e)}"

    return render_template("index.html", humanized_text=humanized_text)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("query")

    # Call OpenAI's chat completion API with a system and user message
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are GenAI, a smart helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract the reply from the response
    reply = response.choices[0].message.content.strip()
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=False)

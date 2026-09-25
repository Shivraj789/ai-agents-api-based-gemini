from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        topic = request.form.get("topic")

        prompt = f"""
        Explain the following topic in simple language:

        {topic}

        Give:
        1. A simple explanation
        2. Three important points
        3. One real-world example
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        result = response.text

    return render_template(
        "index.html",
        result=result
    )

@app.route("/generate", methods=["GET", "POST"])
def generate():
    return "This is the Generate page"


print(app.url_map)

 
if __name__ == "__main__":
    app.run()
app = app    

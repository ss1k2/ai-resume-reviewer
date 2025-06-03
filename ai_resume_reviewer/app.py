from flask import Flask, request, render_template
from ai_review import get_resume_feedback
from resume_parser import extract_text_from_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    if request.method == "POST":
        file = request.files["resume"]
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file)
            feedback = get_resume_feedback(text)
    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)


# 🤖 AI Resume Reviewer

A simple, clean, and functional web app that uses OpenRouter's GPT-style models to review resumes and provide structured feedback using natural language.

---

## ✨ Features

- Upload a **PDF resume**
- Uses OpenRouter API with models like `mistralai/mistral-7b-instruct`
- Returns:
  - Summary of your resume
  - Missing skills
  - Suggested improvements
  - Readiness score out of 100
- Simple modern UI using Flask + HTML/CSS

---

## 🚀 Demo Screenshot

📷 *(Insert screenshot here after running the app and uploading a resume)*

---

## 🛠 Tech Stack

- Python 3
- Flask
- OpenAI SDK (configured for OpenRouter)
- PyPDF2 (to extract text from PDF resumes)
- HTML + CSS for frontend

---

## 🔧 Setup Instructions

1. **Clone this repo**
```bash
git clone https://github.com/yourusername/ai-resume-reviewer.git
cd ai-resume-reviewer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add your OpenRouter API key**

Edit `ai_review.py` and replace:
```python
api_key="your_openrouter_key_here"
```
with your actual OpenRouter API key from [https://openrouter.ai/keys](https://openrouter.ai/keys)

4. **Run the app**
```bash
python app.py
```

5. **Open in browser**
```
http://127.0.0.1:5000
```

---

## 💡 Example Prompt

The prompt sent to the AI model:
```
You are a resume reviewer. Analyze the following resume and provide:
1. A brief summary
2. Key missing technical skills
3. Suggested improvements
4. A readiness score out of 100
```

---

## 📂 Folder Structure

```
ai_resume_reviewer/
├── app.py
├── ai_review.py
├── resume_parser.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 🌐 Optional Deployment (Render/Replit)
Want to deploy it online? DM me or check back soon — I’ll publish a guide.

---

## 📜 License
MIT — free to use, modify, or fork.

---

## 🙋‍♂️ Author

Built by [Subhan Shah Khan].  
💬 Questions or feedback? Create an issue or email me!
subhanshahkhan766@gmail.com

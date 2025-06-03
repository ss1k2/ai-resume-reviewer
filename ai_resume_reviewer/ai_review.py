from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://openrouter.ai/api/v1"
)

def get_resume_feedback(resume_text):
    prompt = f"""
You are a resume reviewer. Analyze the following resume and provide:
1. A brief summary
2. Key missing technical skills
3. Suggested improvements
4. A readiness score out of 100

Resume:
{resume_text}
"""
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

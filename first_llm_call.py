from google import genai

client = genai.Client()

def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text or ""

question = "give me three ideas for AI-powered marketing automation."

answer = ask_gemini(question)

print(answer)
# Learning Git: my first tracked project update.
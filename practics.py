from google import genai

client = genai.Client(api_key="AIzaSyDtWi3OPYjZQCeEFUx9VVZh3gbcM-1YvO4")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)
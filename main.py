import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = "Say this is a test"
response = openai.Completion.create(model="ada", prompt=prompt, temperature=0, max_tokens=7)
print(f"{prompt}{response.choices[0].text}")
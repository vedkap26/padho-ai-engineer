import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
role ="user"
prompt = "give me a name for my  coffee shop"
message_system = {"role": "system", "content": "You are a helpful assistant that provides creative and catchy names for businesses."}
message_user = {"role": "system", "content": "give me a name for my coffee shop"}
messages=[message_system, message_user]
response = client.chat.completions.create(model=model, messages=messages,temperature=2)

print(response)
print(response.choices[0].message.content)

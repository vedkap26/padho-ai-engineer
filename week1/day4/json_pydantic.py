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


from typing import Optional
from pydantic import BaseModel
class Ticket(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    message: Optional[str] = None
schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}
text="Hi, I am Vedant a software engineer and I want to learn more about AI. Can you explain the difference between a cat and a dog in simple terms?"
system_prompt1=f"""please extract the personal infromation and give a json output matching this schema: {schema}. Only include fields you can actually find in the text; omit fields that aren't present.\n\ntext: {text}"""
message_system = {"role": "system", "content": system_prompt1}
prompt2="explain the difference between a cat and a dog"
prompt3="essay on the importance of exercise 1000 words"
messages=[message_system]

response = client.chat.completions.create(model=model, messages=messages,response_format=response_format)
usage=response.usage
answer = response.choices[0].message.content
print(answer)
# prompt = "give me a name for my  coffee shop"
# message_system = {"role": "system", "content": "You are a helpful assistant that provides creative and catchy names for businesses."}
# message_user = {"role": "system", "content": "give me a name for my coffee shop"}
# messages=[message_system, message_user]
# response = client.chat.completions.create(model=model, messages=messages,temperature=2)

# print(response)
# print(response.choices[0].message.content)
import json
raw_data = answer
data_file=json.loads(raw_data)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.phone)
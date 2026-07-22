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


prompt1="Hi"
prompt2="explain the difference between a cat and a dog"
prompt3="essay on the importance of exercise 1000 words"

prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    message_system = {"role": "system", "content": "You are a helpful assistant that provides creative and catchy names for businesses."}
    message_user = {"role": "user", "content": prompt}
    messages=[message_system, message_user]
    response = client.chat.completions.create(model=model, messages=messages,temperature=0.7)
    usage=response.usage
    print(f"Prompt: {prompt}--> completion_tokens: {usage.completion_tokens}, prompt_tokens: {usage.prompt_tokens}, total_tokens: {usage.total_tokens}, finish_reason: {response.choices[0].finish_reason}")
    print(response)
    print(response.choices[0].message.content)

# prompt = "give me a name for my  coffee shop"
# message_system = {"role": "system", "content": "You are a helpful assistant that provides creative and catchy names for businesses."}
# message_user = {"role": "system", "content": "give me a name for my coffee shop"}
# messages=[message_system, message_user]
# response = client.chat.completions.create(model=model, messages=messages,temperature=2)

# print(response)
# print(response.choices[0].message.content)

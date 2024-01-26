import os
from openai import OpenAI

client = OpenAI(api_key="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")
# os.environ['OPENAI_API_KEY'] = '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'
client.models.list()
response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
])
print(f"Response:\n==========\n{response}")
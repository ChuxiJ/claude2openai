import sys
sys.path.append("../..")

import claude2openai
# create a chat completion
chat_completion = claude2openai.ChatCompletion.create(model="claude", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
print(chat_completion.choices[0].message.content)


# claude2openai
Claude2OpenAI is a repository that provides a simple way to use the Slack bot Claude API in the same format as OpenAI's pip package. This makes it easy to integrate Claude into your Slack workspace and leverage its capabilities to enhance your team's productivity and communication. With Claude2OpenAI, you can quickly and easily convert your existing Slack bot to use the OpenAI API format, without having to rewrite your code from scratch. Whether you're a developer looking to streamline your workflow or a team leader looking to improve your team's communication, Claude2OpenAI is a powerful tool that can help you achieve your goals.


# Installation
```
pip install --upgrade claude2openai
```
Install from source with
python setup.py install

# Usage
```bash
export SLACK_API_TOKEN=""
export BOT_ID=""
export CHANNEL_ID=""
```

Or set claude2openai to its value
```python
import claude2openai
claude2openai.slack_api_token = "xxx"
claude2openai.bot_id = "xxx"
claude2openai.channel_id = "xxx"
```

Then
```python
import claude2openai
# create a chat completion
chat_completion = claude2openai.ChatCompletion.create(model="claude", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
print(chat_completion.choices[0].message.content)
```


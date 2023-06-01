from slack_sdk.web.client import WebClient
import time
import os


class Claude(WebClient):

    CHANNEL_ID = os.environ['CHANNEL_ID']
    BOT_ID = os.environ['BOT_ID']
    
    def create(self, text: str):
        ts = self.chat_postMessage(channel=self.CHANNEL_ID, text=f"<@{self.BOT_ID}>\n"+text)["ts"]
        for _ in range(60):
            try:
                # 给定ts，轮询对话
                resp = self.conversations_replies(channel=self.CHANNEL_ID, oldest="", ts=ts)
                # 获取claude回复
                if "messages" not in resp:
                    time.sleep(0.5)
                    continue
                msgs = [msg for msg in resp["messages"] if msg["user"] == self.BOT_ID]
                # 回复未完成，则继续轮询
                if len(msgs) == 0 or msgs[0]["text"].endswith("Typing…_"):
                    time.sleep(0.5)
                    continue
                return msgs[0]["text"]
            except Exception as e:
                raise e
        raise Exception("Claude timeout")


class OpenaiResponse:
    pass


def dict_to_object(d):
    obj = OpenaiResponse()
    for key, value in d.items():
        if isinstance(value, list):
            setattr(obj, key, [dict_to_object(item) for item in value])
        elif isinstance(value, dict):
            setattr(obj, key, dict_to_object(value))
        else:
            setattr(obj, key, value)
    return obj


class ChatCompletion(WebClient):

    claude = Claude(os.environ['SLACK_API_TOKEN'])

    @classmethod
    def create(self, model="claude", messages=[]):
        if model == "claude":
            text = ""
            for message in messages:
                role, content = message["role"], message["content"]
                text += f"`role: {role}`\n{content}\n---\n"
            content = self.claude.create(text)
            res = {
                "choices": [{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": content
                    },
                    "finish_reason": "stop"
                }]
            }
            return dict_to_object(res)

        else:
            raise NotImplementedError


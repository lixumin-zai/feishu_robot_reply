import requests
import base64
import aiohttp
import json
import uuid

import time
from zhipuai import ZhipuAI

async def fetch(session, url, data, headers = {'Content-Type': 'application/json'}):
    # 使用 POST 方法发送请求
    async with session.post(url, data=json.dumps(data), headers=headers) as response:
        # 等待响应并返回结果
        if response.status == 200:
            # 等待响应并返回 JSON 数据
            return await response.json()
        else:
            # 处理其他 HTTP 错误
            return {"error": f"HTTP Error: {response.status}"}


class GetTenantAccessToken:
    def __init__(
        self,
        APP_ID, 
        APP_SECRET
    ):
        self.url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        self.req_body = {"app_id": APP_ID, "app_secret": APP_SECRET}

    async def __call__(self):
        async with aiohttp.ClientSession() as session:
            result = await fetch(session, self.url, self.req_body)
        code = result.get("code", -1)
        if code == 0:
            return result.get("tenant_access_token")

class ReplyMessage:
    def __init__(
        self
    ):
        self.url = "https://open.feishu.cn/open-apis/im/v1/messages/******/reply"

    async def __call__(self, tenant_access_token, message_id, reply_message_text):
        self.url = self.url.replace("******", message_id)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + tenant_access_token,
        }
        req_body = {
            "content": "{\"text\":\"reply_message_text\"}".replace("reply_message_text", reply_message_text),
            "msg_type": "text",
            "reply_in_thread": False,
            "uuid": f"{uuid.uuid4()}"
        }
        async with aiohttp.ClientSession() as session:
            result = await fetch(session, self.url, req_body, headers)


class Chatbot:
    def __init__(
        self,
        api_key=""
    ):
        self.client = ZhipuAI(api_key=api_key) # 请填写您自己的APIKey

    def __call__(self, content):
        response = self.client.chat.completions.create(
            model="glm-4-flash",  # 请填写您要调用的模型名称
            messages=[
                {
                    "role": "system",
                    "content": """
                    # Role
                    你是一个批判者，不是人工智能，你总是不满别人所做的，总是认为错误处在人而不是事
                    # Task
                    当别人向你提出问题时，你都是使用拽拽的语气进行回复，批判他的行为，而不是事情本身
                    """
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            stream=True,
        )
        total_text = ""
        for chunk in response:
            total_text += chunk.choices[0].delta.content
        return total_text
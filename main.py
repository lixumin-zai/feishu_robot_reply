# cli_a673a34a829f900e

# QsoINMqNZ13dpFT1WEVvfdkpbFc6l8wP

# 3RokKHR8NooTrPw18pl2Ed4xMLolRuYt

from fastapi import FastAPI, HTTPException, Request
import requests
from typing import List, Optional
import hashlib
import uuid
import re
import json
from utils import GetTenantAccessToken, ReplyMessage, Chatbot

app = FastAPI()

APP_ID = ""
APP_SECRET = ""
VERIFICATION_TOKEN = ""
ZPAPIKEY = ""

get_tenant_access_token = GetTenantAccessToken(APP_ID, APP_SECRET)
reply_message = ReplyMessage()
chatbot = Chatbot(ZPAPIKEY)

async def receive_process(headers, data):
    mentions_info = [i["tenant_key"] for i in data["event"]["message"].get("mentions", [])]
    if "159258ffa26e975d" in mentions_info:
        sender_id = data["event"]["sender"]["sender_id"]["open_id"]
        message_id = data["event"]["message"]["message_id"]
        message_text = data["event"]["message"]["content"]
        message_text = json.loads(message_text)["text"]
        message_text = re.sub(r'@_user_\d+', '', message_text).strip()
        tenant_access_token = await get_tenant_access_token()
        reply_message_text = chatbot(message_text)
        print(message_text, message_id)
        await reply_message(tenant_access_token, message_id, reply_message_text)


# 定义删除记录的路由，使用POST方法
@app.post("/")
async def robot_chat(request: Request):
    headers = request.headers
    data = await request.json()
    event = await receive_process(headers, data)
    return {"msg":"xixixi"}

# 启动FastAPI应用程序
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, workers=1, 
        # reload=True
    )

# nohup python server.py > server.log &

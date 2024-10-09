import requests

def post_test():
    url = "http://localhost:3001/"

    data = {
	    "schema": "2.0",
        "header": {
            "event_id": "14f51533ef5ef64a465b5155846ba493",
            "token": "3RokKHR8NooTrPw18pl2Ed4xMLolRuYt",
            "create_time": "1728459506016",
            "event_type": "im.message.receive_v1",
            "tenant_key": "159258ffa26e975d",
            "app_id": "cli_a673a34a829f900e"
        },
        "event": {
            "message": {
                "chat_id": "oc_85c2c4ade7130eb2aeaa7a080ca2d3de",
                "chat_type": "p2p",
                "content":"{\"text\":\"[\xe6\x96\xb0\xe6\x9c\x88\xe8\x84\xb8]\"}",
                "create_time": "1728459505470",
                "message_id": "om_e1e81013cbd8d94587f994d9990ea50f",
                "message_type": "text",
                "update_time": "1728459505470",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.86 Safari/537.36 Lark/7.27.8 LarkLocale/zh_CN ttnet SDK-Version/7.27.8"
            },
            "sender": {
                "sender_id": {
                    "open_id": "ou_2915fe4e77cbf39a7e2b28197825bd1e",
                    "union_id": "on_7b8789387ff1c03c2430a0c7a304a00d",
                    "user_id": "27f3ca8f"
                },
                "sender_type": "user",
                "tenant_key": "159258ffa26e975d"
            }
        }
    }
    
    headers = {
        "Host": "82.156.3.170:3000",
        "User-Agent": "Go-http-client/1.1",
        "Content-Length": "884",
        "Content-Type": "application/json;charset=utf-8",
        "Unit": "eu_nc",
        "X-Lark-Request-Nonce": "337894320",
        "X-Lark-Request-Timestamp": "1728459506",
        "X-Lark-Signature": "014d4ef4b8fe103b8822974566308e8c329037fb41d4ef697cc4c9ab7e3e7e3f",
        "X-Request-Id": "0667f932-cdbe-4bf7-acf8-87ce5f78f837",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive"
    }


    resp = requests.post(url, json=data, headers=headers)

    print(resp.text)


if __name__ =="__main__":
    post_test()

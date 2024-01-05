from flask import Flask, request
# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
# 載入 json 標準函式庫，處理回傳的資料格式
import requests, json, time

app = Flask(__name__)

access_token = 'DmNJ+OQnnRv7W0q8vCqtiMV0teDV1UKWNCVt9acUxkXAdNkqaLwZIgZCiNmlb1Ks0pQXtBnbMsoF3Oss7QP/dowzxA/0yZqGTMyIbaXqdJbAkeUCZ2e+jghUGF6YnxfW9QzYR8VM62Qsqu8ikuDqIQdB04t89/1O/w1cDnyilFU='
channel_secret = '1c204137165b50e8812555034f2e10d6'

@app.route("/", methods=['POST'])
def linebott():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)             # 確認 token 是否正確
        handler = WebhookHandler(channel_secret)            # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']     # 加入回傳的 headers
        handler.handle(body, signature)                     # 綁定訊息回傳的相關資訊

        json_data = json.loads(body)
        reply_token = json_data['events'][0]['replyToken']
        user_id = json_data['events'][0]['source']['userId']     # 取得使用者 ID push message 使用
        print(json_data)


    except Exception as e:
        print('error')
        print('reason:', e)
    return 'OK'

if __name__ == "__main__":
    app.run()

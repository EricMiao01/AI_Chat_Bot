from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler # 用於接收 LINE 的資訊
from linebot.exceptions import InvalidSignatureError # 用於檢查簽章是否正確
from linebot.models import MessageEvent, TextMessage, TextSendMessage # 用於回傳文字訊息

app = Flask(__name__) 

@app.route("/", methods=['POST']) 
def linebot(): 
    body = request.get_data(as_text=True)                   # 當客戶端發送 POST 請求到本機時，取得請求內容(as_text=True 代表取得的內容為字串)
    try:
        json_data = json.loads(body)                        # 將取得的字串轉成 json 格式

        secret = '1c204137165b50e8812555034f2e10d6'   # 你的權限
        access_token = 'DmNJ+OQnnRv7W0q8vCqtiMV0teDV1UKWNCVt9acUxkXAdNkqaLwZIgZCiNmlb1Ks0pQXtBnbMsoF3Oss7QP/dowzxA/0yZqGTMyIbaXqdJbAkeUCZ2e+jghUGF6YnxfW9QzYR8VM62Qsqu8ikuDqIQdB04t89/1O/w1cDnyilFU=' # 你的權限
        
        line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
        handler = WebhookHandler(secret)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            reply = msg
        else:
            reply = '你傳的不是文字呦～'
        print(reply)
        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()
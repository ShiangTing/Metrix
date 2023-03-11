import openai
from flask_restful import Api, Resource

root_path = 'C:\\OpenAI\\'
key_file_path = f'{root_path}SECRET_KEY.txt'
key_file = open(key_file_path, "r", encoding='utf-8')
key = key_file.read()
openai.api_key = key
print(f'key={key}')

class ChatBot(Resource):
    def chat(self):
        while True:
            source_path = ''
            user_msg = input("You: ")
            if "維運" in user_msg:
                source_path = f'{root_path}DataSource\MantainSulotion.txt'

            if source_path != '':
                f = open(source_path, "r", encoding = 'utf-8')
                source_context = f.read()
                user_msg = f'請給我下列資料中:\n{source_context}\n最接近{user_msg}的解決方案'
    
            print(f'你的問題是:{user_msg}')

            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "系統訊息，目前無用"},
                {"role": "assistant", "content": "此處填入機器人訊息"},
                {"role": "user", "content": user_msg}
            ],
    )

            print(completion.choices[0].message.content)


class QA(Resource):
    def model(self):
        model_engine = "text-davinci-003"

        # 定義要輸入的文本
        text = "請你模擬一個系統 我會問你一些問題 你會整理成可能的關鍵字並組成notion用的查詢物件並回傳 我不需要查詢物件以外的其他訊息 我的問題是關於一個供應商管理系統 這個系統可以協助通路商管理供應商 供應商可以在系統上操作以修改通路商的賣場資料，通路商的賣場是第三方平台 第一個問題是 我在更新可賣量時,系統顯示成功 但是通路的可賣量沒有更新 "

        # 使用 OpenAI API 來取得關鍵字
        response = openai.Completion.create(
            engine=model_engine,
            prompt=text,
            max_tokens=00,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # 從 OpenAI API 回傳的回應中取得關鍵字
        message = response.choices[0].text.strip()
        print(message)

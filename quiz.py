import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GAPI_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

from aiohttp import web

async def quiz(request):
    # data = await request.json()
    # print(data)
    # option_string=""
    # j=0
    # # {"question": "Which of the following is a conditional expression used in SQL?", "options": ["WHERE", "DESCRIBE", "CASE", "NULLIF"]}
    # for i in data['options']:
    #     option_string+=i
    #     j+=1
    #     if j<len(data['options']):
    #         option_string+=", "

    dt = await request.json()
    
    prompt="Solve this DBMS oracle question "+str(dt)+"Give responce with the correct option content as \"Correct Answer:<Correct option here>\""

    response = model.generate_content(prompt)



    return web.json_response({"message": segregator(dt['options'],response)})

def segregator(options,answer):
    presence = {}
    for value in options:
        presence[value] = value in answer

    for value, present in presence.items():
        if present :
            return value
        
    return options[0]

app = web.Application()
app.router.add_post('/sendquestion', quiz)

web.run_app(app, port=5000)
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

    print(dt)
    response = model.generate_content(prompt)

    print(str(response))

    return web.json_response({"message": segregator(response.candidates[0].content.parts[0].text)})

def segregator(answer):
    return answer.split(":")[1].split("\n")[0].strip()

app = web.Application()
app.router.add_post('/sendquestion', quiz)

web.run_app(app, port=5000)
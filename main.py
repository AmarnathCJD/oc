from bot import Bot
n= input("Login oracle academy and Open the Course and type (Yes/Y/y) to continue : ")
bot = Bot()

while True:
    incomplete = bot.getFirstIncomplete()
    if incomplete:
        quizSkip=bot.completeOne(incomplete)
        
        if quizSkip==True:
            bot.play()  
            bot.goBackToLearningPath()
        else:
            
            pass
    else:
        break

#OA1217386390
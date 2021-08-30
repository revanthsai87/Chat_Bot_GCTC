from flask import Flask, render_template, request,session
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import rasa1
app = Flask(__name__)
app.secret_key = "any random string"
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapters=[

{
                          'import_path': 'newadapeter.MyLogicAdapter',
                          'threshold': 0.80,
                          'default_response': 'I am sorry, but I do not understand.'
                      },
{
                          'import_path': 'webscraping.MyLogicAdapter',
                          'threshold': 0.80,
                          'default_response': 'I am sorry, but I do not understand.'
                      },
{
                          'import_path': 'announce.MyLogicAdapter',
                          'threshold': 0.80,
                          'default_response': 'I am sorry, but I do not understand.'
                      },
{
                          'import_path': 'otherreq.MyLogicAdapter',
                          'threshold': 0.80,
                          'default_response': 'I am sorry, but I do not understand.'
                      },
    {
                           "import_path": "chatterbot.logic.BestMatch",
           'default_response': 'I am sorry, but I do not understand.',
            'threshold': 0.80
    }
    ])
#define app routes
@app.route("/")
def index():
    # session['user']=''
    try:
        session.pop('user',None)
    except KeyError:
       pass
    return render_template("index.html")
@app.route("/course")
def course():
    return render_template("course.html")
@app.route("/download")
def download():
    return render_template("download.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/success")
def success():
    return render_template("Success.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    answer=""
    userText = request.args.get('msg1')
    if "r11a0" == userText.lower()[2:7] :
     try:
        session['user']
        return "User is already logged in , please exit or quit to get other person details"
     except KeyError:
        session['user']=userText
    #print("Adaasdsad",userText.lower()[2:7])
    if userText.lower()=='bye'or userText.lower()=='quit' or userText.lower()=='exit':
        session.pop('user', None)
    answer = englishBot.get_response(userText).text
    t=rasa1.Raasa.help(userText)
    print(t)
    if t!="":
        answer=t
    return answer
if __name__ == "__main__":
    app.debug=True
    app.run()
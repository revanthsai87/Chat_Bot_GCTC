from chatterbot.logic import LogicAdapter
from flask import session
class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if ("attandance" in statement.text or "Attandance" in statement.text or "fees" in statement.text or "Fees" in statement.text or "Accounts" in statement.text or "marks" in statement.text or "cgpa" in statement.text or "Marks" in statement.text):
             return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        import random
        import sqlite3
        import mysql.connector
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='pythonlogin',
            port='3306',
        )
        from chatterbot.conversation import Statement
        stemp=""
        #print(session['user'])
        try:
           session['user']
        except KeyError:
            sel_statement = Statement(text="please enter your roll number to get personal details and try again" + stemp)
            sel_statement.confidence=1
            return sel_statement

        c = mydb.cursor()
        # connection = sqlite3.connect('class.db')
        # c = connection.cursor()
        # Randomly select a confidence between 0 and 1
        # confidence = random.uniform(0, 1)
        # For this example, we will just return the input as output
        # sql = 'SELECT Name from mytable where Roll_no=?'.format('16R11A0520'
        if ("marks" in input_statement.text  or "cgpa"in input_statement.text   or "Marks" in input_statement.text):
         c.execute("SELECT gpa FROM mytable WHERE Roll_no=%s", [session['user']])
         result = c.fetchone()
        elif("attandance"in input_statement.text or "Attandance" in input_statement.text):
         c.execute("SELECT Attandance FROM mytable WHERE Roll_no=%s", [session['user']])
         result = c.fetchone()
         if result[0]<=75 and result[0]>=65:
             stemp="<p><br\> Just on safe side man need to attend classes<br\>Else make sure u get ready 500/- for condonation</p>"
         if result[0]<65:
             stemp="<p><br\>High time ... No minimum attandance.. try hard to reach above 65 <br\> good luck bro..!!</p>"
         if result[0]>75:
             stemp=" <p><br\>good going man.. safe ... <br\> try to maintain the same tempoo</p>"

        elif ("fees"in input_statement.text  or "Fees"in input_statement.text   or "Accounts" in input_statement.text):
            c.execute("SELECT Fees FROM mytable WHERE Roll_no=%s", [session['user']])
            result = c.fetchone()
        else:
            c.execute("SELECT Name FROM mytable WHERE Roll_no=%s", [session['user']])
            result = c.fetchone()

        if result != None:
            sel_statement = Statement(text=str(result[0])+stemp)
            sel_statement.confidence = 1
        else:
            sel_statement=Statement(text="sorry we dont have u r data")
            sel_statement.confidence = 1
        #print(sel_statement.text)
        return sel_statement

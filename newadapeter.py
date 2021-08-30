from chatterbot.logic import LogicAdapter
from flask import session

class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if "R11A0" in statement.text:
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        import random
        import sqlite3
        from chatterbot.conversation import Statement
        import mysql.connector
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='pythonlogin',
            port='3306',
        )
        c = mydb.cursor()
        try:
           session['user']
        except KeyError:
            sel_statement = Statement(text="please enter your roll number  to get personal details and try again" )
            sel_statement.confidence=1
            return sel_statement

        # connection = sqlite3.connect('class.db')
        # c = connection.cursor()
        # Randomly select a confidence between 0 and 1
        # confidence = random.uniform(0, 1)
        # For this example, we will just return the input as output
        # sql = 'SELECT Name from mytable where Roll_no=?'.format('16R11A0520')
        c.execute("SELECT Name FROM mytable WHERE Roll_no=%s", [session['user']])
        result = c.fetchone()
        a=str(result[0])
        c.execute("SELECT last_name FROM mytable WHERE Roll_no=%s", [session['user']])
        result = c.fetchone()
        a=a+" "+str(result[0])

        if result != None:
            sel_statement = Statement(text=a)
            sel_statement.confidence = 1
        else:
            sel_statement=Statement(text="sorry we dont have u r data")
            sel_statement.confidence = 1
        #print(sel_statement.text)
        return sel_statement

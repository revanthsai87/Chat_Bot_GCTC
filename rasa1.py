from wit import Wit
from personal import timetable,assign
from server import englishBot
from info import course,admission,quality,place,contact,placement,facilities,a_calender,complaint,ccfile1,ccfile2,ccfile3,ccfile4,ccfile5,greet
class Raasa():
  def first_entity_value(self,entities, entity):
    if entity not in entities:
        return None
    elif entities[entity][0]['confidence']>0.5:
     val = entities[entity][0]['value']
    else:
        val=None
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val
  def help(userText):
    answer=""
    client = Wit("IQZMELMAON6NDR6UXIBDEIZIYTKYPFKO");
    resp = client.message(userText)
    r = resp['entities']
    #print(r)
    a1 = Raasa().first_entity_value(r, 'personal')
    a2 = Raasa().first_entity_value(r, 'information')
    a3 = Raasa().first_entity_value(r, 'college')
    a4 = Raasa().first_entity_value(r, 'coursefile')
    a5=Raasa().first_entity_value(r,'greetings')
    #print(a1,a2,a3,a4,a5)
    if userText.lower() == 'first' or userText.lower() == 'second' or userText.lower() == 'third' or userText.lower() == 'fourth':
        answer = timetable(userText.lower())
    if a1:
        print("a1")
        if a1 == "time table" and "practicals" not in userText:
            answer= "Which Year?"+"\n"+"1.First"+"\n"+"2.Second"+"\n"+"3.Third"+"\n"+"4.Fourth"
        if a1 == "time table" and "practicals" in userText:
            answer=(englishBot.get_response(userText)).text 
        if a1 == "assignments":
            answer=assign()
        if a1 == "attandance":
            answer=(englishBot.get_response(a1)).text
        if a1 == "sgpa":
            answer=(englishBot.get_response("cgpa")).text
        if a1 == "cgpa":
            answer=(englishBot.get_response("cgpa")).text

    elif a2:
        print("a2")
        if a2=="courses":
            answer=course()
        if a2=="admission":
            answer=admission()
        if a2=="placements":
            answer=placement()
        if a2=="quality":
            answer=quality()
        if a2=="place":
            answer=place()
        if a2=="contact":
            answer=contact()
        if a2=="facilities":
            answer=facilities()
        if a2=="buses":
            answer = (englishBot.get_response(userText)).text
    elif a3:
        print("a3")
        if a3=="academic_calender":
            answer=a_calender()
        if a3=="complaint":
            answer=complaint()
        if  a3=="events":
            answer = (englishBot.get_response(userText)).text
        if a3=="updates" :
            answer = (englishBot.get_response(a3)).text
        if a3=="placements":
            answer = (englishBot.get_response(userText)).text
    elif a4:
        print(a4)
        if a4=="cse":
            answer=ccfile1()
        if a4=="ece":
            answer=ccfile2()
        if a4=="mech":
            answer=ccfile3()
        if a4=="eee":
            answer=ccfile4()
        if a4=="civil":
            answer=ccfile5()
    elif a5:
        print("a5")
        answer=greet();


    return answer




from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot,**kwargs)

    def can_process(self, statement):
        if "updates" in statement.text or "Announcements" in statement.text or "announcements" in statement.text or "latest" in statement.text:
            return True
        else:
            return False

    def process(self, input_statement,additional_response_selection_parameters=None):
        import requests
        import bs4
        from chatterbot.conversation import Statement

        res = requests.get('https://www.gctcportal.in/p/index.html')
        # print(res.text)
        t=''
        s = bs4.BeautifulSoup(res.text, 'lxml')
        li = s.find(class_="post-body entry-content")
        lii=li. find_all_next("li")
        # print(t)
        sel_statement = Statement(text=li)
        sel_statement.confidence = 1

        return sel_statement


# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

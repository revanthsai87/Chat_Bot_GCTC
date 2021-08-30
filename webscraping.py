from chatterbot.logic import LogicAdapter
class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot,**kwargs)

    def can_process(self, statement):
        if ("How" not in statement.text) and("placement" in statement.text or "Placements" in statement.text or "placements" in statement.text or "Placement" in statement.text) :
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        import requests
        import bs4
        from chatterbot.conversation import Statement

        res = requests.get('https://www.gctcportal.in/p/placements.html')
        # print(res.text)
        s = bs4.BeautifulSoup(res.text, 'lxml')
        #  print(x)
        li = s.find(class_="post-body entry-content")
        lii=li.find_all_next("ul")
        sel_statement = Statement(text=lii[0])
        sel_statement.confidence = 1
        return sel_statement


# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
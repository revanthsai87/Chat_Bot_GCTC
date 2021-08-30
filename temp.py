import requests
import bs4

res = requests.get('https://www.gctcportal.in/p/index.html')
 # print(res.text)
s = bs4.BeautifulSoup(res.text, 'lxml')
link = s.find_all(class_="post-body entry-content")
t=''
#  print(x)
li = s.find(class_="post-body entry-content")
lii=li.find_all_next("li")
for x in lii:
    t=t+str(x)
print(t)
# for x in range(0, len(t2) - 1):
#     t4=t4+str((t2[x] + " --------" + t3[x]))
#     t4 = t4 + "\n"
#     if x == 10:
#         break
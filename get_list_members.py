import requests
import os
from bs4 import BeautifulSoup

cur_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(cur_dir,"sites.txt")
htmlname = os.path.join(cur_dir,"列表成员.html")
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/68.0.3440.84 Safari/537.36"}
url = 'https://twitter.com/JianyuYang/lists/list/members'
#url = 'https://www.hao123.com'
#html = requests.get(url,headers=headers)
#print(html.text)
html=open(htmlname,'r',encoding="utf-8")
html=html.read()
Soup = BeautifulSoup(html,'lxml')
#Soup = BeautifulSoup(html.text,'lxml')
a_list = Soup.find_all('a',class_="account-group js-user-profile-link")
#all_div = Soup.find('div',class_='account  js-actionable-user js-profile-popup-actionable ')
for a_tab in a_list: ##这个不解释了。看不懂的小哥儿回去瞅瞅基础教程
    #print(a_tab)

    strong=a_tab.find('strong')
    username=strong.get_text()
    #print(username)
    b=a_tab.find('b')
    userID=b.get_text()
    #print(userID)
    userdata = userID+'%'+username+'\n'
    fh=open(filename,'a+',encoding='utf-8')
    fh.write(userdata)
    fh.close()
input(print("完成！"))

from bs4 import BeautifulSoup
import requests
import re


r4 = requests.get("https://www.mobile.ir/phones/comments-38190-apple-iphone-8-plus.aspx")
soup = BeautifulSoup(r4.text,"html.parser")
comment_headline = soup.find_all("a",{"class":"current"})
for c in comment_headline:
    print(re.sub(r'\s+', ' ',c.text).strip())

comment = soup.find_all("div",{"class":"padd"})
comment_name = soup.find_all("h3")
for c in range(0,len(comment)):
    comment_of_user = re.sub(r'\s+', ' ',comment[c].text).strip()
    name_of_user = re.sub(r'\s+', ' ',comment_name[c].text).strip()
    print("{}:\n{}\n".format(name_of_user,comment_of_user))



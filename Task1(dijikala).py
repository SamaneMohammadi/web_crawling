from bs4 import BeautifulSoup
import requests
import re


##the name of mobile
r = requests.get("https://www.digikala.com/product/dkp-97578/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-iphone-6s-plus-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA")
soup = BeautifulSoup(r.text,"html.parser")
name_title = soup.find_all("h1",{"class":"c-product__title"})
print("------------------------------------------")
for n in name_title:
    print(re.sub(r'\s+',' ',n.text).strip())
print("------------------------------------------")


###########################naghd
r1 = requests.get("https://www.digikala.com/product/dkp-97578/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-iphone-6s-plus-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA#/tab-desc")
soup = BeautifulSoup(r1.text, "html.parser")
header = soup.find_all("h2")

print("------------------------------------------")
print(re.sub(r'\s+',' ',header[0].text).strip())
print("------------------------------------------")
comment_title = soup.find_all("h3",{"class":"c-content-expert__title"})
comment_expert = soup.find("section",{"class":"c-content-expert__summary"})
print(re.sub(r'\s+',' ',comment_expert.text).strip())
print("")

comment_expert_stats = soup.find_all("section",{"class":"c-content-expert__stats"})
for comment in range(0,len(comment_expert_stats)):
    c = re.sub(r'\s+', ' ', comment_expert_stats[comment].text).strip()
    print("{}\n".format(c))

comment_expert_article = soup.find_all("section",{"class":"c-content-expert__article js-expert-article is-active"})
for comment in range(0,len(comment_expert_article)):
    c = re.sub(r'\s+', ' ', comment_expert_article[comment].text).strip()
    c_title = re.sub(r'\s+', ' ', comment_title[comment].text).strip()
    print("{}:\n{}\n".format(c_title,c))


##property of moblie
r2 = requests.get("https://www.digikala.com/product/dkp-97578/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-iphone-6s-plus-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA#/tab-params")
soup = BeautifulSoup(r2.text, "html.parser")
prop = soup.find("h3",{"class":"c-params__title"})
print("-----------------------")
print(re.sub(r'\s+',' ',prop.text).strip())
print("-----------------------")

prop_list = soup.find_all("span",{"class":"block"})
p = 0
while(p <= len(prop_list)-1):
    if p == 6:
        p1 = (re.sub(r'\s+', ' ', prop_list[p].text).strip())
        p2 = (re.sub(r'\s+', ' ', prop_list[p + 1].text).strip())
        p3 = (re.sub(r'\s+', ' ', prop_list[p + 2].text).strip())
        print("{} : {},{}\n".format(p1, p2, p3))
        p = p + 3

    else:

        p1 = (re.sub(r'\s+', ' ', prop_list[p].text).strip())
        p2 = (re.sub(r'\s+', ' ', prop_list[p + 1].text).strip())
        print("{} : {}\n".format(p1, p2))
        p = p + 2

# r_cemment = requests.get("https://search.digikala.com/api2/Data/Get?incredibleOnly=true")
# soup = BeautifulSoup(r_cemment,"html.parser")
# comment_user = soup.find_all("div",{"class":"c-comments__evaluation"})
# print(comment_user)


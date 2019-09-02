from bs4 import BeautifulSoup
import requests
import re
r = requests.get("https://www.gooshishop.com/product/gsp-3367/samsung-galaxy-note8-n950f-ds-64gb-dual-sim/%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-%D9%86%D9%88%D8%AA-8-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA")
soup = BeautifulSoup(r.text,"html.parser")
print("\nThe name of the mobile:")
name_title = soup.find("a",{"itemprop" : "alternateName"})
print(re.sub(r'\s+',' ',name_title.text).strip())
name_title_ = soup.find("h1",{"class" : "product-title fa-name"})
print(re.sub(r'\s+',' ',name_title_.text).strip())
print("------------------------------------------")
property_of_mobile = soup.find_all("h2",{"class" : "titlebar"})


print(re.sub(r'\s+',' ',property_of_mobile[6].text).strip())
print("")
attr_name = soup.find_all("th",{"class" : "attr-name"})
attr_title = soup.find_all("td",{"class":"title"})
attr_value = soup.find_all("td",{"class":"value"})

print(re.sub(r'\s+',' ',attr_name[0].text).strip(),":")
print("")
for p in range(0,2):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[1].text).strip(),":")
print("")
for p in range(2,9):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[2].text).strip(),":")
print("")
for p in range(9,16):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[3].text).strip(),":")
print("")
for p in range(17,24):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
attr_title_val = re.sub(r'\s+',' ',attr_title[24].text).strip()
print("{} : {} \n".format(attr_title_val,"دارد"))
attr_title_val = re.sub(r'\s+',' ',attr_title[25].text).strip()
attr_value_val = re.sub(r'\s+', ' ', attr_value[25].text).strip()
print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[4].text).strip(),":")
print("")

for p in range(26,33):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))

print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[5].text).strip(),":")
print("")
for p in range(33,37):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
attr_title_val = re.sub(r'\s+',' ',attr_title[37].text).strip()
print("{} : {} \n".format(attr_title_val,"دارد"))

attr_title_val = re.sub(r'\s+',' ',attr_title[38].text).strip()
attr_value_val = re.sub(r'\s+', ' ', attr_value[38].text).strip()
print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[6].text).strip(),":")
print("")
attr_title_val = re.sub(r'\s+',' ',attr_title[39].text).strip()
attr_value_val = re.sub(r'\s+', ' ', attr_value[39].text).strip()
print("{} : {} \n".format(attr_title_val,attr_value_val))
attr_title_val = re.sub(r'\s+',' ',attr_title[40].text).strip()
print("{} : {} \n".format(attr_title_val,"دارد"))

for p in range(41,43):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[7].text).strip(),":")
print("")
for p in range(43,45):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
attr_title_val_1 = re.sub(r'\s+', ' ', attr_title[45].text).strip()
print("{} : {} \n".format(attr_title_val_1,"ندارد"))
attr_title_val_1 = re.sub(r'\s+', ' ', attr_title[46].text).strip()
print("{} : {} \n".format(attr_title_val_1,"دارد"))
for p in range(47,50):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[8].text).strip(),":")
print("")
for p in range(50,56):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
for p in range(56,58):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    print("{} : {} \n".format(attr_title_val,"دارد"))
for p in range(58,60):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,"ندارد"))
for p in range(60,61):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,attr_value_val))
attr_title_val = re.sub(r'\s+',' ',attr_title[61].text).strip()
print("{} : {} \n".format(attr_title_val,"دارد"))


print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[9].text).strip(),":")
print("")
for p in range(62,70):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val,"دارد"))
attr_title_val = re.sub(r'\s+',' ',attr_title[70].text).strip()
attr_value_val = re.sub(r'\s+', ' ', attr_value[70].text).strip()
print("{} : {} \n".format(attr_title_val,attr_value_val))

print("------------------------------------------")
print(re.sub(r'\s+',' ',attr_name[10].text).strip(),":")
print("")
for p in range(71,76):
    attr_title_val = re.sub(r'\s+',' ',attr_title[p].text).strip()
    attr_value_val = re.sub(r'\s+', ' ', attr_value[p].text).strip()
    print("{} : {} \n".format(attr_title_val, "دارد"))
attr_title_val_1 = re.sub(r'\s+', ' ', attr_title[74].text).strip()
print("{} : {} \n".format(attr_title_val_1,"ندارد"))
attr_title_val = re.sub(r'\s+',' ',attr_title[75].text).strip()
attr_value_val = re.sub(r'\s+', ' ', attr_value[75].text).strip()
print("{} : {} \n".format(attr_title_val,attr_value_val))
print("------------------------------------------")

print("")
review = soup.find_all("section",{"class":"segment review"})
for i in review:
    print(re.sub(r'\.::', '', i.text).strip())

print("------------------------------------------")
print(re.sub(r'\s+',' ',property_of_mobile[10].text).strip())
print("")
comment_user = soup.find_all("span",{"class":"author"})
comment_user1 = soup.find_all("div",{"class":"comment-article"})
useful_comment = soup.find_all("span",{"class":"count"})
for c in range(0,len(comment_user)):
    #print(c.text.strip())
    user = re.sub(r'\n+', '\n', comment_user[c].text).strip()
    comment = re.sub(r'\n+', '\n', comment_user1[c].text).strip()
    rate = re.sub(r'\n+', '\n', useful_comment[c].text).strip()
    print("Author name: {}\nComment : {} \nThe rates of useful comments: {}\n----------------------------------------------\n".format(user,comment,rate))


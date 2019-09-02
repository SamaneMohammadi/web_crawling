from __future__ import unicode_literals
import feedparser
from bs4 import BeautifulSoup
import requests
from hazm import *
import re

r = requests.get("https://www.gooshishop.com/product/gsp-3367/samsung-galaxy-note8-n950f-ds-64gb-dual-sim/%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-%D9%86%D9%88%D8%AA-8-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA")
soup = BeautifulSoup(r.text,"html.parser")
feed = feedparser.parse('https://www.farsnews.com/rss/politics')
# for post in feed.entries:
#     normalizer = Normalizer()
#     print("normalizer : ",normalizer.normalize(post.summary))
#     print("")
#     print("sent tokenize : ",sent_tokenize(post.summary))
#     print("")
#     print("word tokenize : ",word_tokenize(post.summary))
#     print("")
#     print("-------------------------------------------------------------------------------------------------------------")
stemmer = Stemmer()
print("Stemmer : ",stemmer.stem("آمریکایی‌ها"))
print("")
lemmatizer = Lemmatizer()
print("lemmatizer : ",lemmatizer.lemmatize("می‌کنیم"))
print("")

print("-------------------------------------------------------------------------------------------------------------")

print("------------------------------------------")
##print(re.sub(r'\s+',' ',property_of_mobile[10].text).strip())
print("")
comment_user = soup.find_all("span",{"class":"author"})
comment_user1 = soup.find_all("div",{"class":"comment-article"})
useful_comment = soup.find_all("span",{"class":"count"})
for c in range(0,len(comment_user)):
    normalizer = Normalizer()
    print("normalizer : ", normalizer.normalize(comment_user1[c].text))
    print("")
    print("sent tokenize : ", sent_tokenize(comment_user1[c].text))
    print("")
    print("word tokenize : ", word_tokenize(comment_user1[c].text))
    print("")
    print(
        "-------------------------------------------------------------------------------------------------------------")
    #print(c.text.strip())

#comment = re.sub(r'\n+', '\n', comment_user1[c].text).strip()

import feedparser
feed = feedparser.parse('https://www.farsnews.com/rss/politics')
print("---------------------------------------------------اخبار سیاسی-------------------------------------")
print("\nFeed title: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['title']))
print ("Feed Link: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['link']))
print ("Feed Subtitle: {}\n---------------------------------------------------------------------------------------------\n".format(feed.feed.subtitle))
print ("Feed rights: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['rights']))
for post in feed.entries:

    print ("post title : {}\n\npost link : {}\n\npost summary : {}\n\npost published : {} ".format(post.title ,post.link,post.summary,post.published))
    print("-------------------------------------------------------------------------------------------------------------")

print("")
print("---------------------------------------------------اخبار ورزشی---------------------------------------")

feed = feedparser.parse('https://www.farsnews.com/rss/sports')
print("\nFeed title: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['title']))
print ("Feed Link: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['link']))
print ("Feed Subtitle: {}\n---------------------------------------------------------------------------------------------\n".format(feed.feed.subtitle))
print ("Feed rights: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['rights']))
for post in feed.entries:

    print ("post title : {}\n\npost link : {}\n\npost summary : {}\n\npost published : {} ".format(post.title ,post.link,post.summary,post.published))
    print("-------------------------------------------------------------------------------------------------------------")
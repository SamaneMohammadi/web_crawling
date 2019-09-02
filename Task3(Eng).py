import feedparser


print("-------------------------------------- PoliticsNews -------------------------------------")
feed = feedparser.parse('http://feeds.reuters.com/Reuters/PoliticsNews')

print("\nFeed title: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['title']))
print ("Feed Link: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['link']))
print ("Feed Subtitle: {}\n---------------------------------------------------------------------------------------------\n".format(feed.feed.subtitle))
print ("Feed rights: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['rights']))
for post in feed.entries:
    summary = post.summary.split("<")
    print ("post title : {}\n\npost link : {}\n\npost summary : {}\n\npost published : {} ".format(post.title ,post.link,summary[0],post.published))
    print("-------------------------------------------------------------------------------------------------------------")




print("-------------------------------------- sportsNews -------------------------------------")
feed = feedparser.parse('http://feeds.reuters.com/reuters/sportsNews')

print("\nFeed title: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['title']))
print ("Feed Link: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['link']))
print ("Feed Subtitle: {}\n---------------------------------------------------------------------------------------------\n".format(feed.feed.subtitle))
print ("Feed rights: {}\n---------------------------------------------------------------------------------------------\n".format(feed['feed']['rights']))
for post in feed.entries:
    summary = post.summary.split("<")
    print ("post title : {}\n\npost link : {}\n\npost summary : {}\n\npost published : {} ".format(post.title ,post.link,summary[0],post.published))
    print("-------------------------------------------------------------------------------------------------------------")
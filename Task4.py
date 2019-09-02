import json
import numpy as np


#محاسبه فاصله‌ی جاکارد

def jaccard_dist(tweet1, tweet2):
    x = set(tweet1.split(' '))
    y = set(tweet2.split(' '))
    x_intersection_y = x.intersection(y)
    x_union_y = x.union(y)
    return 1 - len(x_intersection_y) / len(x_union_y)




def clustering_tweets(tweet_dict, centroid_ids):

    #ایجاد دیکشنری برای centriod
    centroid_dict = {}
    for centroid_id in centroid_ids:
        centroid_dict[centroid_id] = []


    #متن centriod
    centroid_text_list = []
    for tweet_id in list(centroid_dict.keys()):
        centroid_text_list.append(tweet_dict[tweet_id])



    #محاسبه فاصله جاکارد بین یک توییت با تمامی مرکزیت ها این حلقه را برای تمام توییت ها اجرا کن
    for tweet_id, tweet_text in tweet_dict.items():
        dist_of_centroid = []
        for centroid_text in centroid_text_list:
            jcc_distance = jaccard_dist(tweet_text, centroid_text)
            dist_of_centroid.append(jcc_distance)


        # پیدا کردن ایندکس نزدیکترین مرکزیت به توییت
        index_of_closet_centroid = np.argmin(dist_of_centroid)

        # اضافه کردن آیدی توییتی به عنوان نزدیکترین توییت به توییت مرکزیت
        centroid_dict[centroid_ids[index_of_closet_centroid]].append(tweet_id)

    return(centroid_dict)




#محاسبه مرکزیت جدید
def compute_new_centroid(tweet_dict, centroid_dict):

    new_centroid_ids = []

    #پیدا کردن میانگین جدید برای مرکزیت
    for centroid_id, tweet_ids in centroid_dict.items():
        centroid_min_dist = 1
        centroid_min_dist_id = ''

        #محاسبه فاصله جاکارد از این تویییت به توییت های دیگر
        for tweet_id in tweet_ids:

            this_tweet = tweet_dict[tweet_id]
            other_tweets = []
            for other_id in tweet_ids:
                other_tweets.append(tweet_dict[other_id])

            dist_to_other_tweets = []
            for other_tweet in other_tweets:
                jcc_distance = jaccard_dist(this_tweet, other_tweet)
                dist_to_other_tweets.append(jcc_distance)

            #محاسبه میانگین فاصله یک توییت از دیگر توییت ها
            ave_dist_to_other_tweets = np.mean(dist_to_other_tweets)

            # اگر مرکزیت این توییت نزدیکتر از مرکزیت قبلی باشد، آن را به عنوان مرکزیت جدید قرار بده
            if ave_dist_to_other_tweets < centroid_min_dist:

                centroid_min_dist = ave_dist_to_other_tweets
                centroid_min_dist_id = tweet_id

        # اضافه کن ایدی مرکزیت جدیدرو
        new_centroid_ids.append(centroid_min_dist_id)

    return (new_centroid_ids)




#لود کردن داده ها و استفاده از json به خاطر پشتیبانی از انواع مختلف داده
tweets_file = open("tweets_file.txt","r")
tweet_dict = {}
#در دیکشنری کلید ها ایدی توییت و مقادیر متن آن تویییت است
for tweet in tweets_file.readlines():
    tweet_json = json.loads(tweet)
    tweet_dict[tweet_json['id']] = tweet_json['text']



seeds_file = open("seeds_file.txt","r")
centroid_ids = seeds_file.readlines()
centroid_ids = [int(x.strip().replace(',','')) for x in centroid_ids]


#به صورت رندم centroid_ids را از بین ۲۵ تا انتخاب می‌کنیم
centroid_ids = list(np.random.choice(centroid_ids, size= 25 , replace=False))


count = 1
print("")
print('using 25-means algorithm for clustering tweet !!!')
print("")

#اجرا شود تا زمانی که converge کند
while (True):


    centroid_dicts = clustering_tweets(tweet_dict, centroid_ids)
    centroid_ids_old = centroid_ids
    centroid_ids = compute_new_centroid(tweet_dict, centroid_dicts)


    if centroid_ids == centroid_ids_old:

        print('Algoritm converged in the step {} :) and the dict of clustering tweet is:\n'.format(count))
        print(centroid_dicts)
        break

    else:

        print('Algoritm could not converged in the step {} :( !!!\n'.format(count))
        count = count + 1
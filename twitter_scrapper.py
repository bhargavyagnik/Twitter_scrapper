from twitterscraper import query_tweets
import datetime as dt
import pandas as pd


def tweet_scrape(tag, save, lang='en', limit=10, begindt=dt.date(2019, 1, 1), enddt=dt.date.today()):
    list_of_tweets = query_tweets(tag, lang=lang, limit=limit, begindate=begindt, enddate=enddt)
    for tweet in list_of_tweets:
        print(tweet.text)
    d = pd.DataFrame(i.__dict__ for i in list_of_tweets)
    remove = ['screen_name', 'username', 'user_id', 'tweet_id', 'tweet_url', 'timestamp', 'timestamp_epochs',
              'text_html', 'links', 'has_media', 'img_urls', 'video_url', 'likes', 'retweets', 'replies', 'is_replied',
              'is_reply_to', 'parent_tweet_id', 'reply_to_users']
    d.drop(remove, inplace=True, axis=1)
    d.to_csv(str(save + '.csv'))


tags = []  # List of tags you want to record the tweets
for tag in tags:
    tweet_scrape(tag=tag, save=tag, limit=1000)

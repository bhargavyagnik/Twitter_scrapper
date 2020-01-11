# Twitter_scrapper
Tweet Scrapper using the Twitterscraper package in python.
![](https://www.growthplug.com/wp-content/uploads/2018/07/twitter_logo_0.png)

One can scrap Twitter for data using various methods like 
- python-twitter (official API)
- twitterscraper (https://github.com/taspinar/twitterscraper)
- Tweetscraper
- Tweepy
- Twython

# Twitter API
1. Create your app
The first step in doing so is to create a Twitter App. Click the “Create New App” button and fill out the fields on the next page.

![](https://python-twitter.readthedocs.io/en/latest/_images/python-twitter-app-creation-part1.png)

Once your app is created, you’ll be directed to a new page showing you some information about it.
![](https://python-twitter.readthedocs.io/en/latest/_images/python-twitter-app-creation-part2.png)
```python
import twitter
api = twitter.Api(consumer_key=[consumer key],
                  consumer_secret=[consumer secret],
                  access_token_key=[access token],
                  access_token_secret=[access token secret])
```                  

Then you can use to access the tweets follwoing the documentation. Tweepy and Twython also require this authentication but if you want to access tweets without the OAuth then there's Twitterscraper or other packages helpful for scrapping with using the Twitter API.
And more.. But we'll use Twitterscrapper as it is free, easy and has the following advantages over Twitter API Twitter has provided REST API's which can be used by developers to access and read Twitter data. They have also provided a Streaming API which can be used to access Twitter Data in real-time.

Most of the software written to access Twitter data provide a library which functions as a wrapper around Twitters Search and Streaming API's and therefore are limited by the limitations of the API's.

With Twitter's Search API you can only sent 180 Requests every 15 minutes. With a maximum number of 100 tweets per Request this means you can mine for 4 x 180 x 100 = 72.000 tweets per hour. By using TwitterScraper you are not limited by this number but by your internet speed/bandwith and the number of instances of TwitterScraper you are willing to start.

One of the bigger disadvantages of the Search API is that you can only access Tweets written in the past 7 days. This is a major bottleneck for anyone looking for older past data to make a model from. With TwitterScraper there is no such limitation.

Install it using the following Command in the CMD

```
pip install twitterscraper
```
You can try out some examples at https://github.com/taspinar/twitterscraper/tree/master/examples

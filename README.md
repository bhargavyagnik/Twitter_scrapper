# Twitter_scrapper
Tweet Scrapper using the Twitterscraper package in python.
![](https://www.growthplug.com/wp-content/uploads/2018/07/twitter_logo_0.png)

One can scrap Twitter for data using various methods like 
- python-twitter (official API)
- twitterscraper (https://github.com/taspinar/twitterscraper)
- Tweetscraper

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



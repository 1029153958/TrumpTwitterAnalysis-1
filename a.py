# -*- coding: UTF-8 -*-
import json
import requests
from bs4 import BeautifulSoup

class Spyder(object):
    def __init__(self,times,init="TWEET--1017190186269184001"):
        self.URL="https://twitter.com/i/search/timeline?f=tweets&q=from:realdonaldtrump&max_position="
        self.HEADER={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        self.MAX_POSITION=init
        self.TIMES=times

    def getURL(self):
        return self.URL+self.MAX_POSITION

    def getNextPosition(self,tweets):
        return tweets['min_position']

    def writeCSV(self,tweets):
        print(tweets)
        with open("trunmp.csv","a+",encoding='utf8') as f:
            for i in tweets:
                res=""
                for j in i:
                    res+=str(i[j]).replace(";",",");res+=";"
                res=res[:-1].replace("\n"," ")
                f.write(res+"\n")

    def search(self):
        JSON=json.loads(requests.get(self.getURL(),headers=self.HEADER).text)
        self.MAX_POSITION=self.getNextPosition(JSON)
        return BeautifulSoup(JSON["items_html"],'html.parser')

    def parseTweet(self,soup):
        tweets=[]
        for li in soup.find_all("li", class_='js-stream-item'):
            # If our li doesn't have a tweet-id, we skip it as it's not going to be a tweet.
            if 'data-item-id' not in li.attrs:
                continue
            tweet = {'tweet_id': li['data-item-id'],'text': None,'user_id': None,'user_screen_name': None,
                     'user_name': None,'created_at': None,'retweets': 0,'favorites': 0}
            # Tweet Text
            text_p = li.find("p", class_="tweet-text")
            if text_p is not None:
                tweet['text'] = text_p.get_text()
            # Tweet User ID, User Screen Name, User Name
            user_details_div = li.find("div", class_="tweet")
            if user_details_div is not None:
                tweet['user_id'] = user_details_div['data-user-id']
                tweet['user_screen_name'] = user_details_div['data-user-id']
                tweet['user_name'] = user_details_div['data-name']
            # Tweet date
            date_span = li.find("span", class_="_timestamp")
            if date_span is not None:
                tweet['created_at'] = float(date_span['data-time-ms'])
            # Tweet Retweets
            retweet_span = li.select("span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount")
            if retweet_span is not None and len(retweet_span) > 0:
                tweet['retweets'] = int(retweet_span[0]['data-tweet-stat-count'])
            # Tweet Favourites
            favorite_span = li.select("span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount")
            if favorite_span is not None and len(retweet_span) > 0:
                tweet['favorites'] = int(favorite_span[0]['data-tweet-stat-count'])
            tweets.append(tweet)
        return tweets

    def doing(self):
        for i in range(self.TIMES):
            self.writeCSV(self.parseTweet(self.search()))

if __name__=="__main__":
    test = Spyder(1000)
    while(True):
        try:
            test.doing()
            break
        except (Exception,EnvironmentError) :
            pass

    # ["id","content","user_id",'user_screen_name','user_name','created_at','retweets','favorites']

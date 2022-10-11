import snscrape.modules.twitter as sntwitter
import numpy as np
import pandas as pd
import os
dagpath = os.getcwd()

qry="Business intelligence"
max=5
tweets=[]



def Fetchtweets():
        

        for tweet in sntwitter.TwitterSearchScraper("Business intelligence").get_items():
            
            if len(tweets)==5:
                break
            else:
                tweets.append([tweet.username,tweet.date,tweet.content])
            

        df=pd.DataFrame(tweets,columns=["User","date","tweet"])

        #print(df)

        df.to_csv(f'{dagpath}/../temp/file.csv')


Fetchtweets()        


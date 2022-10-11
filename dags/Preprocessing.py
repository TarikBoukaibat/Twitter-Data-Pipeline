import re
import nltk
from nltk.corpus import stopwords
import pandas as pd 
import os



dagpath = os.getcwd()
df=pd.read_csv(f'{dagpath}/../temp/file.csv')

stw=stopwords.words('english')


def clean_tweets(tweet):
    temp=tweet.lower()
    temp = re.sub("'", "", temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[.*?\]',' ', temp)
    temp = re.sub(r'http\S+', '', temp)
    temp = re.sub("@[A-Za-z0-9_]+","", temp)
    temp = re.sub("#[A-Za-z0-9_]+","", temp)
    temp = re.sub("[^a-z0-9]"," ", temp)
    temp = temp.split()
    temp = [word for word in temp if not word in stw]
    temp = " ".join(word for word in temp)
    return temp


df.tweet.apply(lambda text: clean_tweets(text))
df.to_csv(f'{dagpath}/../temp/file_cleaned.csv')
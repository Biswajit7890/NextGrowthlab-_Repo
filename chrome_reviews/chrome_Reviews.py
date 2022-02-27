import pandas as pd
import numpy as np
import string
import nltk 
import string 
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
import emoji
from contractions_dict.contractions import expand_contractions
from contractions_dict.contractions import cleaning
from contractions_dict.contractions import lemmatize_words
from contractions_dict.contractions import deEmojify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sent = SentimentIntensityAnalyzer()

def reviews_tag(df):
    df=df.drop(labels=['ID','Review URL','User Name','Developer Reply','Version','Review Date','App ID'], axis=1)
    df=df.reset_index(drop=True)
    df=df.dropna()
    df['Text_emo']=df['Text'].apply(lambda x:deEmojify(x))
    df['Text_contract']=df['Text_emo'].apply(lambda x:expand_contractions(x))
    df['text_clean']=df['Text_contract'].apply(cleaning)
    df["text_lemma"] =df["text_clean"].apply(lambda text: lemmatize_words(text))
    df=df.drop(labels=['Text','Text_emo','Text_contract','text_clean'], axis=1)
    polarity = [round(sent.polarity_scores(i)['compound'], 2) for i in df['text_lemma']]
    df['sentiment_score'] = polarity
    Filtercondition1=df['sentiment_score']>0.40
    Filtercondition2=df['Star']<=2
    df=df[Filtercondition1 & Filtercondition2]
    df=df[['text_lemma','Star']]
    return df

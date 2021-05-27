#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:54:08 2019

@author: wajgilani
"""
import pip

import numpy as np
import pandas as pd


#!pip install twitter

from twitter import Twitter
from twitter import OAuth


apikey='LmWo260maj5KsmP3wnigGiymR'
apisecretkey='wdFhGB3XV79csLvSI57R1OFavsXNntbdtmlJzy2spNdMIFbnxn'
accesstoken='4012083173-pdPffs50tApeBURWR9QQt22rlhEp0sdEaCFwBvR'
accesstokensecret='PVwr62zsdUF0QQpcRMkPDBLxJ4HhAG4Cjccy49GwPv8pK'

oauth = OAuth(accesstoken,accesstokensecret,apikey,apisecretkey)
api = Twitter(auth=oauth)

#lets look at whats trending around the world
t_loc = api.trends.available()
print(t_loc)

from pandas.io.json import json_normalize

df_loc=json_normalize(t_loc)

#Which country has the most cities being tracked?
df_loc.country.value_counts()

#What if we wanted to search for a particular city, using a partial word?
dfNew=df_loc[df_loc['name'].str.contains('New')]

ny=dfNew.loc[dfNew.name=='New York','woeid']

#ny_trend = api.trends.place(_id=ny)

type(ny)
ny.values
ny.values[0]
ny_trend = api.trends.place(_id=ny.values[0])

########## Saving and Reading Objects ######################
import json
with open('ny_trend.json', 'w') as outfile:
    json.dump(ny_trend, outfile)

# Getting back the objects:
with open('ny_trend.json') as json_data:
    ny_trend_example = json.load(json_data)

############################################################

dfny=json_normalize(ny_trend)
type(dfny.trends)
    dfny.trends.shape

dfny.trends.values
dfny['trends'].values

############ Series example #############
s=pd.Series(['ny','nj','ct','tx'])
s.values[0]


dftrends=json_normalize(dfny.trends.values[0])
dftrends.to_pickle('dftrends.pkl')
dftrends = pd.read_pickle('dftrends.pkl')

# 5 Trending Topic In NY
tt=dftrends.sort_values('tweet_volume',ascending=False).head(5)
# or
dftrends.columns
dftrends.nlargest(5,'tweet_volume')
dftrends.nlargest(5,'tweet_volume')[['name','tweet_volume']]


#Twitter - Post and Read a Tweet
api.statuses.update(status="Their is an invasion at the border, someone get Jon Snow!!!")
mytweets=api.statuses.home_timeline()


dfmyt=json_normalize(mytweets)
dfmyt.to_pickle('dfmyt.pkl')

dfmyt=pd.read_pickle('dfmyt.pkl')
dfmyt['text']

mytweets1=api.statuses.home_timeline(count=1)
dfmyt1=json_normalize(mytweets1)
##############################################################################
#Searching tweets on prarticular trending topics
search_result = api.search.tweets(q='Trump',count = 100,tweet_mode='extended')

dfsr=json_normalize(search_result)
dfsr.to_pickle('dfsr.pkl')
dfsr=pd.read_pickle('dfsr.pkl')



dfst=json_normalize(dfsr.statuses.values[0])
dfst2=json_normalize(dfsr.loc[0,'statuses'])
dfst3=json_normalize(search_result, 'statuses')


dfst.full_text

dfst.full_text.shape
type(dfst.full_text)


df0=pd.DataFrame({'Value':dfst.loc[0]})
www=dfst.loc[0]
dd=dfst.iloc[0]

aaa= pd.DataFrame({'Value':dfst.full_text})

#####################################################################################
#Twitter - Following a Twitter Account
tjson=api.statuses.user_timeline(screen_name="narendramodi",tweet_mode='extended')
dfmodi=json_normalize(tjson)
dfmodi.full_text

#Twitter - Followers of a Twitter Account
tfollow=api.followers.ids(screen_name="narendramodi")
dffol=json_normalize(tfollow)

dffol2=json_normalize(tfollow,'ids')

dffol2.to_pickle('dffol2.pkl')
dffol2=pd.read_pickle('dffol2.pkl')


u0=api.users.lookup(user_id=dffol2.loc[0,0])
dfu0=json_normalize(u0)


user1=api.statuses.user_timeline(id=dffol2.loc[4,0],tweet_mode='extended')

dfuser1=json_normalize(user1)

#######################  textblob ################################
!pip install textblob
!python -m textblob.download_corpora




#import TextBlob
import pip

!pip install textblob
!python -m textblob.download_corpora

from textblob import TextBlob

import numpy as np
import pandas as pd
import nltk
nltk.download()

df= pd.read_pickle('dfall.pkl')
tx = df.loc[1,'full_text']
blob = TextBlob(tx)
blob.tags
blob.tags[0]
blob.sentences
blob.sentences[0]
blob.sentences[0].words
blob.sentences[0].words[0]
blob.noun_phrases
blob.ngrams(3)
blob.ngrams(5)
blob.ngrams(5)[0]
blob.correct()
blob.words[9].spellcheck()
blob.words[5].spellcheck()
blob.detect_language()
blob.translate(to= 'ur') 

verbs = []
for word, tag in blob.tags:
  if (tag=='VB') | (tag=='VBG'):
    verbs.append(word.lemmatize())

verbs = []
for word, tag in blob.tags:
  if tag in ['VB','VBG']:
    verbs.append(word.lemmatize())

nouns = []
for word, tag in blob.tags:
	if tag == 'NN':
		nouns.append(word.lemmatize())

nounsp = []
for word, tag in blob.tags:
	if tag == 'NNP':
		nounsp.append(word.lemmatize())

blob.sentiment.polarity
blob.sentiment.subjectivity

#Create 2 arrays
polarity=[]
subj=[]

#Get polarity and sentiment for each row and put it in either polarity or sentiment 
for t in df.full_text:
    tx=TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    subj.append(tx.sentiment.subjectivity)

#Put in dataframe polsubj which has a column of polarity values and a column of subjectivity values
polsubj = pd.DataFrame({'polarity': polarity,'subjectivity': subj})

#Plot the line graph
polsubj.plot(title='Polarity and Subjectivity')

polsubj.plot(kind='bar',title='Polarity and Subjectivity')

polsubj.tail(30).plot(title='Polarity and Subjectivity')
polsubj.head(30).plot(title='Polarity and Subjectivity')





import pip
!pip install wordcloud

from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop = stopwords.words('english')


wordcloud = WordCloud(background_color= 'white' , stopwords=stop).generate(tx)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

tx2=df.full_text.str.cat(sep=' ')
wordcloud3 = WordCloud(stopwords=stop, max_words=100).generate(tx2)
plt.imshow(wordcloud3)
plt.axis('off')
plt.show()

stop.append('co')
stop.append('https')

tx2=df.full_text.str.cat(sep=' ')
wordcloud3 = WordCloud(stopwords=stop, max_words=10).generate(tx2)
plt.imshow(wordcloud3)
plt.axis('off')
plt.show()
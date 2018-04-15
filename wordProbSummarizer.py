
# coding: utf-8

# In[1]:

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import string
puncts = string.punctuation
from collections import Counter
#word_count = Counter(words)
#commonWords = word_count.most_common(10)


# In[3]:

def tokenizeImpWords(sentence):
    words = word_tokenize(sentence.lower())
    words = [word for word in words if word not in stop_words and word not in puncts]
    return list(set(words))


# In[36]:

data = ''
with open('sample_article.txt','r') as f:
    data = f.read()

from nltk import sent_tokenize

sentences = sent_tokenize(data)
#sentences = data.split('.')
#sentences = sentences[:len(sentences)-1]
print (sentences)

wordDict = []
for sentence in sentences:
    wordDict += tokenizeImpWords(sentence)
    
wordDict = wordDict
word_count = Counter(wordDict)
N = len(wordDict)


# In[37]:

def word_score(word):
    return (word_count[word]/N)


# In[38]:

def SumBasic(sentence):
    wordCollection = tokenizeImpWords(sentence)
    totalCard = len(wordCollection)
    
    sentenceScore = 0
    for word in wordCollection:
        sentenceScore += word_score(word)
    
    return sentenceScore


# In[39]:

print ('Total words: ', N)
print (wordDict)

sentImpMap = {}
cnt=0
for sentence in sentences:
    print (sentence,': Score-> ', SumBasic(sentence))
    sentImpMap[cnt] = SumBasic(sentence)
    cnt+=1


# In[40]:

import operator
sentImpMap_sorted = sorted(sentImpMap.items() ,key=operator.itemgetter(1), reverse=True)
i=0
for (key, value) in sentImpMap_sorted:
    if i==3:
        break
    print (sentences[key])
    i+=1


# In[ ]:




# coding: utf-8

# In[1]:

from collections import Counter


# In[2]:

data = ''
with open('sample_article.txt','r') as f:
    data = f.read()

from nltk import sent_tokenize

#sentences = sent_tokenize(data)
sentences = data.split('.')
sentences = sentences[:len(sentences)-1]
print (sentences)


# In[3]:

from nltk.tokenize import word_tokenize

words = []
for l in sentences:
    cur_words = word_tokenize(l.lower())
    #print (cur_words)
    words += cur_words


# In[4]:

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = [lemmatizer.lemmatize(word) for word in words]

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
#print (words)
import string
puncts = string.punctuation
words = [word for word in words if word not in stop_words and word not in puncts]

word_count = Counter(words)

commonWords = word_count.most_common(10)

topWordList = [word[0] for word in commonWords]

print (topWordList)


# In[5]:

abstract = ''
for sentence in sentences:
    score = 0
    for word in topWordList:
        if word in sentence:
            score +=1
    if score > 3:
        abstract += sentence+'.'


# In[6]:

print ('\nArticle: \n')
print (data)

print ('\nAbstract: \n')
print (abstract)


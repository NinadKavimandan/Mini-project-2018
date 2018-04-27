from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import string
puncts = string.punctuation
from collections import Counter
import math

def getSumExtractive(data):
	sentences = sent_tokenize(data)
	print (sentences)
	
	def tokenizeImpWords(sentence):
		words = word_tokenize(sentence.lower())
		words = [word for word in words if word not in stop_words and word not in puncts]
		return list(set(words))

	
	wordDict = []
	for sentence in sentences:
		wordDict += tokenizeImpWords(sentence)    
	wordDict = wordDict
	word_count = Counter(wordDict)
	N = len(wordDict)
	
	def word_score(word):
		return (word_count[word]/N)

	def SumBasic(sentence):
		wordCollection = tokenizeImpWords(sentence)
		totalCard = len(wordCollection)
		sentenceScore = 0
		for word in wordCollection:
			sentenceScore += word_score(word)
		return sentenceScore
	
	print ('Total words: ', N)
	print (wordDict)

	sentImpMap = {}
	cnt=0
	for sentence in sentences:
		print (sentence,': Score-> ', SumBasic(sentence))
		sentImpMap[cnt] = SumBasic(sentence)
		cnt+=1
	import operator
	print ('Summary: ')
	sentImpMap_sorted = sorted(sentImpMap.items() ,key=operator.itemgetter(1), reverse=True)
	i=0
	summ = ''
	thresh = math.ceil(len(sentences)/3)
	for (key, value) in sentImpMap_sorted:
		if i==3:
			break
		#print (sentences[key])
		summ += sentences[key]
		i+=1
	return summ
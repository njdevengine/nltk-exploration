from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8')
type(raw)
len(raw)
raw[:100]

#tokenize the text, splitting all words and punctuation
import nltk, re, pprint
from nltk import word_tokenize
tokens = word_tokenize(raw)
type(tokens)
len(tokens)
tokens[:10]

#convert to nltk Text object
text = nltk.Text(tokens)

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
#top bigrams in the text
text.collocations()

# Method##########Functionality####################################################
# s.find(t)	      index of first instance of string t inside s (-1 if not found)
# s.rfind(t)	    index of last instance of string t inside s (-1 if not found)
# s.index(t)	    like s.find(t) except it raises ValueError if not found
# s.rindex(t)	    like s.rfind(t) except it raises ValueError if not found
# s.join(text)	  combine the words of the text into a string using s as the glue
# s.split(t)	    split s into a list wherever a t is found (whitespace by default)
# s.splitlines()	split s into a list of strings, one per line
# s.lower()     	a lowercased version of the string s
# s.upper()	      an uppercased version of the string s
# s.title()	      a titlecased version of the string s
# s.strip()	      a copy of s without leading or trailing whitespace
# s.replace(t, u)	replace instances of t with u inside s

#dealing with different encodings
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path, encoding='latin2')
for line in f:
  line = line.strip()
  print(line)
# Pruska Biblioteka Państwowa. Jej dawne zbiory znane pod nazwą
# "Berlinka" to skarb kultury i sztuki niemieckiej. Przewiezione przez
# Niemców pod koniec II wojny światowej na Dolny Śląsk, zostały
# odnalezione po 1945 r. na terytorium Polski. Trafiły do Biblioteki
# Jagiellońskiej w Krakowie, obejmują ponad 500 tys. zabytkowych
# archiwaliów, m.in. manuskrypty Goethego, Mozarta, Beethovena, Bacha.
  
f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))
    
#b'Pruska Biblioteka Pa\\u0144stwowa. Jej dawne zbiory znane pod nazw\\u0105'
#b'"Berlinka" to skarb kultury i sztuki niemieckiej. Przewiezione przez'
#b'Niemc\\xf3w pod koniec II wojny \\u015bwiatowej na Dolny \\u015al\\u0105sk, zosta\\u0142y'
#b'odnalezione po 1945 r. na terytorium Polski. Trafi\\u0142y do Biblioteki'
#b'Jagiello\\u0144skiej w Krakowie, obejmuj\\u0105 ponad 500 tys. zabytkowych'
#b'archiwali\\xf3w, m.in. manuskrypty Goethego, Mozarta, Beethovena, Bacha.'

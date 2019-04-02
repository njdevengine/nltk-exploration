import nltk
# opens download navigator, just download book
nltk.download()
from nltk.book import *

#for your own viewing of raw text
moby=[]
for i in text1:
    moby.append(i)
moby = " ".join(moby)

#contextual use of the word. Limit 25, shows total # as well.
text1.concordance("monstrous")

#words used in a similar manner to the word.
text2.similar("monstrous")

#finds common contexts for the words, both words appear in the text between the others
text2.common_contexts(["very", "always"])
#returns: were_great though_unwilling

text2.concordance("unwilling")
#has both:"I was very unwilling to enter" and "though always unwilling to join any"

import matplotlib
import numpy
#creates a graphical representation of where words appear, plots in a matplotlib chart.
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
#http://www.nltk.org/images/inaugural.png

sorted(set(text3))
#returns all individual words and punctuation(tokens) sorted:
# ['!', "'", '(', ')', ',', ',)', '.', '.)', ':', ';', ';)', '?', '?)',
# 'A', 'Abel', 'Abelmizraim', 'Abidah', 'Abide', 'Abimael', 'Abimelech',
# 'Abr', 'Abrah', 'Abraham', 'Abram', 'Accad', 'Achbor', 'Adah', ...]

#NOTE: Capitalized letters come first ie: @,1,A,Z,Za,apple,zebra

len(set(text3))
#returns the number of unique (distinct words) word types / (punctuation) tokens

len(set(text3)) / len(text3)
#returns the lexical richness of the text, distinct words are just 6% here. Each word is used 16* on avg.

#count how many times a word is used	
text3.count("smote")
# returns: 5
#calc percentage of text a word is, a is 1 of this text (genesis)
100 * text4.count('a') / len(text4)
# returns: 1.4643016433938312

#functions built to simplify the above
def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

lexical_diversity(text3)
percentage(text4.count('a'), len(text4))

#return the index of a word
text3.index("the")
#find the word at an index
text3[100]

#most common words in a text
fdist1 = FreqDist(text1)
fdist1.most_common(50)
# [(',', 18713), ('the', 13721), ('.', 6862), ('of', 6536), ('and', 6024),
# ('a', 4569), ('to', 4542), (';', 4072), ('in', 3916), ('that', 2982),
# ("'", 2684), ('-', 2552), ('his', 2459), ('it', 2209), ('I', 2124)...]

#most of these words are useless, connector words etc. they account for a large portion of the text
fdist1.plot(50, cumulative=True)
#single use one time only words
fdist1.hapaxes()

#print the context of hapaxes (single use words)
array = fdist1.hapaxes()[:25]
for i in array:
    print("RESULT ",str(i),"\n")
    print(text2.concordance(i))
    print("_______________________________________________________")
    
#view the long words
my_set = set(text4)
long_words = [word for word in my_set if len(word) > 15]
sorted(long_words)

for i in long_words:
    print(i+ " " + str(len(i)))
#view their context
for i in long_words:
    print("RESULT ",str(i),"\n")
    print(text4.concordance(i))
    print("_______________________________________________________")

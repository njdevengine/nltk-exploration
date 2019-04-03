#http://www.nltk.org/book/ch01.html

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

#frequent & lengthy words
fdist5 = FreqDist(text5)
array = sorted(word for word in set(text5) if len(word) > 7 and fdist5[word] > 7)
#and their context
for i in array:
    print("RESULT ",str(i),"\n")
    print(text5.concordance(i))
    print("_______________________________________________________")

#show word pairs
list(bigrams(['more', 'is', 'said', 'than', 'done']))
#returns: [('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]

#A collocation is a sequence of words that occur together unusually often. like: red wine (ie.phrases)
text1.collocations()
# Sperm Whale; Moby Dick; White Whale; old man; Captain Ahab; sperm
# whale; Right Whale; Captain Peleg; New Bedford; Cape Horn; cried Ahab;
# years ago; lower jaw; never mind; Father Mapple; cried Stubb; chief
# mate; white whale; ivory leg; one hand

#find 10  most common word lengths in a text:
fdist = FreqDist(len(w) for w in text1)
fdist
# FreqDist({3: 50223, 1: 47933, 4: 42
345, 2: 38513, 5: 26597, 6: 17111, 7: 14399,
#   8: 9966, 9: 6428, 10: 3528, ...})

# most frequent word length is 3, and that words of length 3 account for roughly 50,000 (or 20%) of the words making up the book
fdist.most_common()
# [(3, 50223), (1, 47933), (4, 42345), (2, 38513), (5, 26597), (6, 17111), (7, 14399),
# (8, 9966), (9, 6428), (10, 3528), (11, 1873), (12, 1053), (13, 567), (14, 177),
# (15, 70), (16, 22), (17, 12), (18, 1), (20, 1)]
fdist.max()
# 3
fdist[3]
# 50223
fdist.freq(3)
# 0.19255882431878046

## Functions Defined for NLTK's Frequency Distributions

# Example	                    Description
# fdist = FreqDist(samples)	    create a frequency distribution containing the given samples
# fdist[sample] += 1	        increment the count for this sample
# fdist['monstrous']	        count of the number of times a given sample occurred
# fdist.freq('monstrous')	    frequency of a given sample
# fdist.N()	                    total number of samples
# fdist.most_common(n)	        the n most common samples and their frequencies
# for sample in fdist:	        iterate over the samples
# fdist.max()	                sample with the greatest count
# fdist.tabulate()	            tabulate the frequency distribution
# fdist.plot()	                graphical plot of the frequency distribution
# fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
# fdist1 |= fdist2	            update fdist1 with counts from fdist2
# fdist1 < fdist2	            test if samples in fdist1 occur less frequently than in fdist2


#### Word Comparison Operators ####

# Function	        Meaning
# s.startswith(t)	test if s starts with t
# s.endswith(t)	    test if s ends with t
# t in s	        test if t is a substring of s
# s.islower()	    test if s contains cased characters and all are lowercase
# s.isupper()	    test if s contains cased characters and all are uppercase
# s.isalpha()	    test if s is non-empty and all characters in s are alphabetic
# s.isalnum()	    test if s is non-empty and all characters in s are alphanumeric
# s.isdigit()	    test if s is non-empty and all characters in s are digits
# s.istitle()	    test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)

sorted(w for w in set(text7) if '-' in w and 'index' in w)
sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10)
sorted(w for w in set(sent7) if not w.islower())
sorted(t for t in set(text2) if 'cie' in t or 'cei' in t)

[len(w) for w in text1]
# returns: [1, 4, 4, 2, 6, 8, 4, 1, 9, 1, 1, 8, 2, 1, 4, 11, 5, 2, 1, 7, 6, 1, 3, 4, 5, 2, ...]
[w.upper() for w in text1]
# returns: ['[', 'MOBY', 'DICK', 'BY', 'HERMAN', 'MELVILLE', '1851', ']', 'ETYMOLOGY', '.', ...]

#########TEXT CLEANUP
len(text1)
# 260819
len(set(text1))
# 19317
len(set(word.lower() for word in text1))
# 17231
len(set(word.lower() for word in text1 if word.isalpha()))
# 16948

# filter results
filtered_array = sorted(set(word.lower() for word in text1 if word.isalpha() and len(word)>3))

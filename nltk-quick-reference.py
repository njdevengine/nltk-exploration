Basic Corpus Functionality defined in NLTK: more documentation can be found using help(nltk.corpus.reader) and by reading the online Corpus HOWTO at http://nltk.org/howto.

Example	                  Description
fileids()	                the files of the corpus
fileids([categories])	    the files of the corpus corresponding to these categories
categories()	            the categories of the corpus
categories([fileids])	    the categories of the corpus corresponding to these files
raw()	                    the raw content of the corpus
raw(fileids=[f1,f2,f3])	  the raw content of the specified files
raw(categories=[c1,c2])	  the raw content of the specified categories
words()	                  the words of the whole corpus
words(fileids=[f1,f2,f3])	the words of the specified fileids
words(categories=[c1,c2])	the words of the specified categories
sents()	                  the sentences of the whole corpus
sents(fileids=[f1,f2,f3])	the sentences of the specified fileids
sents(categories=[c1,c2])	the sentences of the specified categories
abspath(fileid)	          the location of the given file on disk
encoding(fileid)	        the encoding of the file (if known)
open(fileid)	            open a stream for reading the given corpus file
root	                    if the path to the root of locally installed corpus
readme()	                the contents of the README file of the corpus

import nltk
from nltk.corpus import gutenberg

#import large body of  text from project gutenberg (books)
#nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')

#convert to a text object, to perform nltk functions
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#contextual use of word surprize:
emma.concordance("surprize")

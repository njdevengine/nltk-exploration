import nltk

#import large body of  text from project gutenberg (books)
#nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')

#convert to a text object, to perform nltk functions
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#contextual use of word surprize:
emma.concordance("surprize")

from nltk.corpus import gutenberg
gutenberg.fileids()
# returns: ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', ...]

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
# avg word length, sentence length, and lexical diversity 
# 5 25 26 austen-emma.txt
# 5 26 17 austen-persuasion.txt
# 5 28 22 austen-sense.txt
# 4 34 79 bible-kjv.txt
# 5 19 5 blake-poems.txt
# 4 19 14 bryant-stories.txt
# 4 18 12 burgess-busterbrown.txt
# 4 20 13 carroll-alice.txt
# 5 20 12 chesterton-ball.txt

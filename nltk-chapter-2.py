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

#display sentences for macbeth *there is also words(), raw(), and sents()
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1116]

#find longest sentence
longest_len = max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s) == longest_len]

#shows other text types contained in nltk
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')
# firefox.txt Cookie Manager: "Don't allow sites that set removed cookies to se ...
# grail.txt SCENE 1: [wind] [clop clop clop] 
# KING ARTHUR: Whoa there!  [clop ...
# overheard.txt White guy: So, do you have any plans for this evening?
# Asian girl ...
# pirates.txt PIRATES OF THE CARRIBEAN: DEAD MAN'S CHEST, by Ted Elliott & Terr ...
# singles.txt 25 SEXY MALE, seeks attrac older single lady, for discreet encoun ...
# wine.txt Lovely delicate, fragrant Rhone wine. Polished leather and strawb ...

# chatroom logs
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]
# ['i', 'do', "n't", 'want', 'hot', 'pics', 'of', 'a', 'female', ',',
# 'I', 'can', 'look', 'in', 'a', 'mirror', '.']
[print(i) for i in chatroom]

#brown corpus, writings of all genres from 1960
from nltk.corpus import brown
brown.categories()
# ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies',
# 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance',
# 'science_fiction']
brown.words(categories='news')
# ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
brown.words(fileids=['cg22'])
# ['Does', 'our', 'society', 'have', 'a', 'runaway', ',', ...]
brown.sents(categories=['news', 'editorial', 'reviews'])
# [['The', 'Fulton', 'County'...], ['The', 'jury', 'further'...], ...]

#compare genres for their use of modal verbs
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end=' ')

#frequency distribution of words in brown genres

cfd = nltk.ConditionalFreqDist(
          (genre, word)
          for genre in brown.categories()
          for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)

#                  can could  may might must will
#            news   93   86   66   38   50  389
#        religion   82   59   78   12   54   71
#         hobbies  268   58  131   22   83  264
# science_fiction   16   49    4   12    8   16
#         romance   74  193   11   51   45   43
#           humor   16   30    8    8    9   13


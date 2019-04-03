import nltk
from nltk.corpus import gutenberg

#import large body of  text from project gutenberg (books)
#nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')

#convert to a text object, to perform nltk functions
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#contextual use of word surprize:
emma.concordance("surprize")

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

##### THE CORPUS LIST ####
# Brown Corpus                                15 genres, 1.15M words, tagged, categorized
# CESS Treebanks                              1M words, tagged and parsed (Catalan, Spanish)
# Chat-80 Data Files                          World Geographic Database
# CMU Pronouncing Dictionary                  127k entries
# CoNLL 2000 Chunking Data                    270k words, tagged and chunked
# CoNLL 2002 Named Entity                     700k words, pos- and named-entity-tagged (Dutch, Spanish)
# CoNLL 2007 Dependency Treebanks (sel)       150k words, dependency parsed (Basque, Catalan)
# Dependency Treebank                         Dependency parsed version of Penn Treebank sample
# FrameNet                                    10k word senses, 170k manually annotated sentences
# Floresta Treebank                           9k sentences, tagged and parsed (Portuguese)
# Gazetteer Lists                             Lists of cities and countries
# Genesis Corpus                              6 texts, 200k words, 6 languages
# Gutenberg (selections)                      18 texts, 2M words
# Inaugural Address Corpus                    US Presidential Inaugural Addresses (1789-present)
# Indian POS-Tagged Corpus                    60k words, tagged (Bangla, Hindi, Marathi, Telugu)
# MacMorpho Corpus                            1M words, tagged (Brazilian Portuguese)
# Movie Reviews                               2k movie reviews with sentiment polarity classification
# Names Corpus                                8k male and female names
# NIST 1999 Info Extr (selections)            63k words, newswire and named-entity SGML markup
# Nombank                                     115k propositions, 1400 noun frames
# NPS Chat Corpus                             10k IM chat posts, POS-tagged and dialogue-act tagged
# Open Multilingual WordNet                   15 languages, aligned to English WordNet
# PP Attachment Corpus                        28k prepositional phrases, tagged as noun or verb modifiers
# Proposition Bank                            113k propositions, 3300 verb frames
# Question Classification                     6k questions, categorized
# Reuters Corpus                              1.3M words, 10k news documents, categorized
# Roget's Thesaurus                           200k words, formatted text
# RTE Textual Entailment                      8k sentence pairs, categorized
# SEMCOR                                      880k words, part-of-speech and sense tagged
# Senseval 2 Corpus                           600k words, part-of-speech and sense tagged
# SentiWordNet                                sentiment scores for 145k WordNet synonym sets
# Shakespeare texts (selections)              8 books in XML format
# State of the Union Corpus                   485k words, formatted text
# Stopwords Corpus                            2,400 stopwords for 11 languages
# Swadesh Corpus                              comparative wordlists in 24 languages
# Switchboard Corpus (selections)             36 phonecalls, transcribed, parsed
# Univ Decl of Human Rights                   480k words, 300+ languages
# Penn Treebank (selections)                  40k words, tagged and parsed
# TIMIT Corpus (selections)                   audio files and transcripts for 16 speakers
# VerbNet 2.1                                 5k verbs, hierarchically organized, linked to WordNet
# Wordlist Corpus                             960k words and 20k affixes for 8 languages
# WordNet 3.0 (English)                       145k synonym sets

dict = {"Brown Corpus":"15 genres, 1.15M words, tagged, categorized",
"CESS Treebanks":"1M words, tagged and parsed (Catalan, Spanish)",
"Chat-80 Data Files":"World Geographic Database",
"CMU Pronouncing Dictionary":"127k entries",
"CoNLL 2000 Chunking Data":"270k words, tagged and chunked",
"CoNLL 2002 Named Entity":"700k words, pos- and named-entity-tagged (Dutch, Spanish)",
"CoNLL 2007 Dependency Treebanks (sel)":"150k words, dependency parsed (Basque, Catalan)",
"Dependency Treebank":"Dependency parsed version of Penn Treebank sample",
"FrameNet":"10k word senses, 170k manually annotated sentences",
"Floresta Treebank":"9k sentences, tagged and parsed (Portuguese)",
"Gazetteer Lists":"Lists of cities and countries",
"Genesis Corpus":"6 texts, 200k words, 6 languages",
"Gutenberg (selections)":"18 texts, 2M words",
"Inaugural Address Corpus":"US Presidential Inaugural Addresses (1789-present)",
"Indian POS-Tagged Corpus":"60k words, tagged (Bangla, Hindi, Marathi, Telugu)",
"MacMorpho Corpus":"1M words, tagged (Brazilian Portuguese)",
"Movie Reviews":"2k movie reviews with sentiment polarity classification",
"Names Corpus":"8k male and female names",
"NIST 1999 Info Extr (selections)":"63k words, newswire and named-entity SGML markup",
"Nombank":"115k propositions, 1400 noun frames",
"NPS Chat Corpus":"10k IM chat posts, POS-tagged and dialogue-act tagged",
"Open Multilingual WordNet":"15 languages, aligned to English WordNet",
"PP Attachment Corpus":"28k prepositional phrases, tagged as noun or verb modifiers",
"Proposition Bank":"113k propositions, 3300 verb frames",
"Question Classification":"6k questions, categorized",
"Reuters Corpus":"1.3M words, 10k news documents, categorized",
"Roget's Thesaurus":"200k words, formatted text",
"RTE Textual Entailment":"8k sentence pairs, categorized",
"SEMCOR":"880k words, part-of-speech and sense tagged",
"Senseval 2 Corpus":"600k words, part-of-speech and sense tagged",
"SentiWordNet":"sentiment scores for 145k WordNet synonym sets",
"Shakespeare texts (selections)":"8 books in XML format",
"State of the Union Corpus":"485k words, formatted text",
"Stopwords Corpus":"2,400 stopwords for 11 languages",
"Swadesh Corpus":"comparative wordlists in 24 languages",
"Switchboard Corpus (selections)":"36 phonecalls, transcribed, parsed",
"Univ Decl of Human Rights":"480k words, 300+ languages",
"Penn Treebank (selections)":"40k words, tagged and parsed",
"TIMIT Corpus (selections)":"audio files and transcripts for 16 speakers",
"VerbNet 2.1":"5k verbs, hierarchically organized, linked to WordNet",
"Wordlist Corpus":"960k words and 20k affixes for 8 languages",
"WordNet 3.0 (English)":"145k synonym sets"}

import pandas as pd
corpus = pd.DataFrame(dict.items(), columns=['Corpus', 'Description'])
corpus

#full list of corpi and their names at: http://www.nltk.org/nltk_data/

#stopwords are verbal plumbing not necessary to extract meaning wholesale from text.
from nltk.corpus import stopwords
stopwords.words('english')
# ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
# 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
# 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
# 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
# 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
# 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
# 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
# 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
# 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
# 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
# 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
# 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

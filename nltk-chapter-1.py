import nltk

# opens download navigator, just download book
nltk.download()

from nltk.book import *

#contextual use of the word.
text1.concordance("monstrous")

#words used in a similar manner to the word.
text2.similar("monstrous")

#finds common contexts for the words, both words appear in the text between the others
text2.common_contexts(["very", "always"])
#returns: were_great though_unwilling

text2.concordance("unwilling")
#has both:"I was very unwilling to enter" and "though always unwilling to join any"

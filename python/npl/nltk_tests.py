from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import ngrams, FreqDist
from gensim.models import Word2Vec

text_fr = "Salut comment ca va ? J'apprend la base d'une librairie pour le TALN. j'espere que ca ira \n mais en sommes nous Sur"
bible_file = open("bible.txt", 'r')

sentences = sent_tokenize(text_fr, language = 'french')
words = word_tokenize(text_fr, language = 'french')
postag = pos_tag(words)

# bible_file.read()
all_counts = {}

for size in 5, 6:
	all_counts = FreqDist(ngrams(bible_file.read(), size))

print all_counts

for sent in sentences:
	print sent

for word in words:
	print word

print postag

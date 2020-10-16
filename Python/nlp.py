from bs4 import BeautifulSoup as BS
berkas = open('corpus.txt','r')
artikel = ' '
for teks in iter( lambda: berkas.readline(), ''):
    artikel = artikel + '' + (teks[teks.find('<html>')])
artikel = BS(artikel,'lxml').text
artikel = artikel.replace('\n', ' ')
artikel = artikel.replace('\t', ' ')
artikel = artikel.replace('.', '.') 

import nltk
from nltk.util import ngrams
token = nltk.word_tokenize(artikel)
bigram = ngrams(token,2)

from nltk import *
from nltk.util import ngrams
kalimat = sent_tokenize(artikel)
token = []
for klm in kalimat :
    token.append(word_tokenize(klm))
listbigram = []
for tk in token :
    bigram = ngrams(tk,2, pad_right =True, pad_left = True, left_pad_symbol ='<s>', right_pad_symbol = '</s>')
for gram in bigram :
    listbigram.append(gram)

bigram_fd = FreqDist(listbigram)
for key,value in bigram_fd.items() :
    print(key,value)

import pickle
pickle.dump(bigram_fd,open('bigram.p', 'wb'))


kal1 = 'buah berwarna hijau dan merah'
token = word_tokenize(kal1)

for kata in token:
    p = 1
    pkata = bigram_fd.freq((kata,))
    print("p('%s') = %f" %((kata,pkata)))
    p = p*pkata
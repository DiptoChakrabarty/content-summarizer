import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
from nltk.corpus import wordnet

#en = spacy.load('en')

synonymns=[]
words=input("give your text : ")
for syn in wordnet.synsets(words):
    for l in syn.lemmas():
        synonymns.append(l.name())
synonymns=set(synonymns)
print(synonymns) 
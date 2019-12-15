import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
from nltk.corpus import wordnet

def context_search(words):
    synonymns=[]
    #words=input("give your text : ")
    for syn in wordnet.synsets(words):
        for l in syn.lemmas():
            synonymns.append(l.name())
    synonymns=set(synonymns)
    print(synonymns) 
    file=open('terms.txt','r')
    content=file.read()
#print(content)
    content=nltk.sent_tokenize(content)
#print(content)
    sentences=[]
    for i in range(len(content)):
        review=re.sub('[^a-zA-Z]',' ',content[i])
        review=review.lower()
        review=review.split()
        review=[word for word in review if word not in set(stopwords.words("english"))]    
        review= " ".join(review)
        if len(review)>5:
            sentences.append(review)
    context=[]
    for sent in sentences:
        for word in synonymns:
            if word in sent:
                context.append(sent)
    return context

word=input("Give word : ")
print(context_search(word))


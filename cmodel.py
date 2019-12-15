import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from sklearn.metrics.pairwise import cosine_similarity


file=open('terms.txt','r')
content=file.read()
#print(content)
content=nltk.sent_tokenize(content)
#print(content)
ps=PorterStemmer()
sentences=[]
for i in range(len(content)):
    review=re.sub('[^a-zA-Z]',' ',content[i])
    review=review.lower()
    review=review.split()
    review=[word for word in review if word not in set(stopwords.words("english"))]    
    review= " ".join(review)
    if len(review)>5:
        sentences.append(review)
#print(sentences)
#print("/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
word_dict={}
for sent in sentences:
    for word in sent.split():
        
        if word not in word_dict :
            word_dict[word]=1
        else:
            word_dict[word]+=1
#print(word_dict['apple'])
sent_rank={}
count=0
for sent in sentences:
    sum=0
    for word in sent.split():
        sum=sum+word_dict[word]
    sent_rank[count]=sum/len(sent)
    count=count+1
#print(word_dict)
#print("****************************************")
print(sent_rank)
p=0
threshold=5.7
for i in sent_rank:
    if sent_rank[i] > threshold:
        index=int(i)
        p+=1
        print(sentences[i])
print(p)


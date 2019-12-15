import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

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
    sentences.append(review)
#print(sentences)

word_embeddings = {}
f = open('glove.6B.50d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()
sentence_vectors=[]
for i in sentences:
  if len(i) != 0:
    v = sum([word_embeddings.get(w, np.zeros((50,))) for w in i.split()])/(len(i.split())+0.001)
  else:
    v = np.zeros((50,))
  sentence_vectors.append(v)

# similarity matrix
sim_mat = np.zeros([len(sentences), len(sentences)])

for i in range(len(sentences)):
  for j in range(len(sentences)):
    if i != j:
      sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,50), sentence_vectors[j].reshape(1,50))[0,0]



nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

# Extract top 10 sentences as the summary
for i in range(10):
  print("{}".format(i+1),ranked_sentences[i][1])
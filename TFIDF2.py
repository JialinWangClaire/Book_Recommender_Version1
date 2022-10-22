import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from TFIDF import vectorizer
from TFIDF import x_old
f=open('person_profile.txt')
corpus0=f.readlines()
#new_features = vectorizer.transform(corpus0)
x_to_train=0
c=0
for each in corpus0:
    x_to_train+=x_old[int(each)]
    c+=1
x_to_train=x_to_train/c
print(x_to_train.shape)


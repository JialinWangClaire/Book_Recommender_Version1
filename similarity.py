from  TFIDF import x_old
from TFIDF2 import x_to_train
import numpy as np
from stemming import book_order
np.set_printoptions(suppress=True, threshold=0.00000001)

def square_rooted(x):
   return round(np.sqrt(sum([a*a for a in x])),3)
  
def cosine_similarity(x,y):
 numerator = sum(a*b for a,b in zip(x,y))
 denominator = square_rooted(x)*square_rooted(y)
 return round(numerator/float(denominator),6)

dic={}
c=0
for i in x_old:
    value=cosine_similarity(x_to_train,i)
    dic[c]=value
    c+=1
    if c==100:
        break
print(sorted(dic, key=dic.get,reverse=True))
for each in sorted(dic, key=dic.get,reverse=True):
    print(book_order[each])

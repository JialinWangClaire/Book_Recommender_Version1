from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()
f_new = open("processed_abstract.txt",'a')
f_old= open("book_abstract.txt")
book_order={}
i=0
for line in f_old:
    out = line.translate(str.maketrans('', '', string.punctuation))
    out0 = out.split()[1:]
    num = out.split()[0]
    book_order[i] = int(num)
    for each in out0:
        f_new.write(ps.stem(each))
        f_new.write(' ')
    f_new.write('\n')
    i+=1
f_new.close()
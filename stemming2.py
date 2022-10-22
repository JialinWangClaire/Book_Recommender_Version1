from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()
f_new = open("p_person_profile.txt",'a')
f_old= open("person_profile.txt")

for line in f_old:
    out = line.translate(str.maketrans('', '', string.punctuation))
    out0 = out.split()[1:]
    for each in out0:
        f_new.write(ps.stem(each))
        f_new.write(' ')
    f_new.write('\n')

f_new.close()
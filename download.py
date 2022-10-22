import json
import csv
import pandas as pd
f=open('book_abstract.txt','a')
def load_data(file_name, head=5000):
    count = 0
    data = []
    with open(file_name) as fin:
        for l in fin:
            d = json.loads(l)
            count += 1
            data.append(d)

            # break if reaches the 100th line
            if (head is not None) and (count > head):
                break
    return data
books = load_data('goodreads_books.json')
print(books[0].keys())
for each in range(5000):
    content=books[each]['description']
    idnum=books[each]['book_id']
    if content!='':
        f.write(idnum)
        f.write(' ')
        f.write(content.replace('\n', ''))
        f.write('\n')

with open('goodreads_interactions.csv') as fileObject:
    reader_obj = csv.reader(fileObject)
    list0=[]
    i=0
    for row in reader_obj:
        if i!=0:
            list0.append(map(int,row))
        else:
            list0.append(row)
        i+=1
        if i==500:
            break
    df=pd.DataFrame(list0[1:],columns=list0[0])
    df0=df.loc[(df['user_id']==0) & (df['rating']==5) & (df['is_read']==1)&(df['is_reviewed']==1)]
    df0.index=range(len(df0))
    print(df0)

list1=list(df0['book_id'])
person_book_id=[]
with open('book_id_map.csv') as fileObject1:
    reader_obj1 = csv.reader(fileObject1)
    next(reader_obj1, None)
    c=0
    diction={}
    for i in reader_obj1:
        diction[int(i[0])]=int(i[1])
        c+=1
        if c==1000:
            break
    for each in list1:
        person_book_id.append(diction[each])
f.close()

f=open('book_abstract.txt','r')
Lines = f.readlines()
f2=open('person_profile.txt','a')

for each in person_book_id:
    indexing = 0
    for lines in Lines:
        k=int(lines.split()[0])
        if each==k:
            f2.write(str(indexing).replace('\n', ''))
            f2.write('\n')
        indexing+=1
f2.close()
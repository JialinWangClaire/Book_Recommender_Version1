from sklearn.feature_extraction.text import TfidfVectorizer
f=open('processed_abstract.txt')
corpus=f.readlines()
vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit(corpus)
features = vectorizer.transform(corpus)
x_old=features.toarray()
print(x_old.shape)

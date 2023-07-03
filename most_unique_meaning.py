from gensim.test.utils import common_texts
from gensim.models import Word2Vec

#model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)
#model.save("word2vec.model")
model = Word2Vec.load("word2vec.model")
model.train([["hello", "world"]], total_examples=1, epochs=1)
maxDistance=float('+inf')
bestWord=''
for word in model.wv.index_to_key:
    newDist=model.wv.most_similar(word)[0][1]
    if newDist>maxDistance:
        maxDistance=newDist
        bestWord=word
print(word)
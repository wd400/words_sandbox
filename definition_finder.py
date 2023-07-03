#find word = w1 +/- w2 +/- w3 relations
import gensim.downloader
from itertools import combinations
import numpy as np

model =  gensim.downloader.load('glove-wiki-gigaword-50')
from queue import PriorityQueue

bestMatchs = PriorityQueue()
#inputvector=model.get_vector("mouse")
inputvector=np.zeros((len(model.vectors[0]),))

def signGenearator(vectors:list):
    if len(vectors)==1:
        yield vectors[0],['+']
        yield -vectors[0],['-']
        return
    for result,signList in signGenearator(vectors[1:]):
        yield vectors[0]+result,['+']+signList
        yield vectors[0]-result,['-']+signList
    
N=3

for indexes in combinations(range(len(model)),N):
    #word:index
 #   print("indexes",indexes)
    vectors=[model[index] for index in indexes]
    for linearCombination,signList in signGenearator(vectors):
        distance=np.linalg.norm(linearCombination - inputvector)
        if distance<=1.5:           
            expression= model.index_to_key[indexes[0]] + ''.join((signList[i]+ model.index_to_key[indexes[i+1]] for i in range(N-1) )) 
            bestMatchs.put(

                (
                    distance,
                    expression
           )
                )
                
                
            print(distance,expression)

    

        

print(bestMatchs)
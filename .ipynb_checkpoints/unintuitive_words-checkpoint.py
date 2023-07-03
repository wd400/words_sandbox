import math
from nltk.corpus import wordnet as wn

class Node:
    def __init__(self):
        self.childs={}
        self.wordsPrefix=set()
        self.wordsSuffix=set()

words=[]
meaning={}
with open('words_alpha.txt') as f:
    for line in f:
        word=line.strip()
        words.append(word)
        meaning[word]=wn.synsets(word)


tree=Node()

#composition tolerance
alpha=0.7

def properPrefix(word,i):
    return i>alpha*len(word)

def properSuffix(word,i):
    return i<len(word)*(1-alpha)


def getNextNode(node,letter):
    if letter in node.childs:
        return node.childs[letter]
    else:
        node.childs[letter]=Node()
        return node.childs[letter]

def appendWord(tree,word):
    currentNode=tree
    for i,letter in enumerate(word):
        currentNode=getNextNode(currentNode,letter)
        if properPrefix(word,i):
            currentNode.wordsPrefix.add(word)
    
    currentNode=tree
    for i,letter in enumerate(word[::-1]):
        currentNode=getNextNode(currentNode,letter)
        if properSuffix(word,len(word)-i):       
            currentNode.wordsSuffix.add(word)
    
    
def getNode(tree,word):
    currentNode=tree
    for letter in word:
        if letter in currentNode.childs:
            currentNode=currentNode.childs[letter]
        else:
            return None
    return currentNode

def getPrefixes(tree,prefix):
    relatedNode=getNode(tree,prefix)
    if relatedNode is None:
        return {}
    else:
        return relatedNode.wordsPrefix

def getSuffixes(tree,suffix):
    relatedNode=getNode(tree,suffix)
    if relatedNode is None:
        return {}
    else:
        return relatedNode.wordsSuffix

for word in words:
    appendWord(tree,word)


results=set()

def nonintuitive(senses,sensesprefix,sensessuffix):
    bestSimilarity=float('-inf')
    for sense in senses:
        for senseprefix in sensesprefix:
            for sensesuffix in sensessuffix:
                bestSimilarity=max(bestSimilarity,
                                    max(sense.wup_similarity(senseprefix),
                                        sense.wup_similarity(sensesuffix)))


        
    return float('-inf')<bestSimilarity<0.1


for word in words:
    for i in range(1,len(word)-1):
        prefixes=getPrefixes(tree,word[:i])
        if len(prefixes)==0:
            continue
        
        suffixes=getSuffixes(tree,word[i:][::-1])
        if len(suffixes)==0:
            continue

        for wordprefix in prefixes:
            for wordsuffix in suffixes:
                if nonintuitive(meaning[word],meaning[wordprefix],meaning[wordsuffix]):
                    results.add((wordprefix,wordsuffix,word))
                #    print(f'{wordprefix}+{wordsuffix}={word}')

for result in results:
    print(f'{result[0]} + {result[1]} =/= {result[2]}')

#output
#burg + claries =/= burglaries
#ante + lope =/= antelope
#struthio + mimus =/= struthiomimus
#pint + ados =/= pintados
#ante + lopes =/= antelopes
#derma + titis =/= dermatitis
#sass + abies =/= sassabies
#guar + panties =/= guaranties
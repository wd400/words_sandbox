class Node:
    def __init__(self) -> None:    
        self.isWord = False
        self.childrens = dict()

root = Node()

f = open("/home/zach/Downloads/phonetique.csv")
line =  f.readline()

words=set()


while line:
    mot, phonetique = line[:-1].split(',')
    words.add(mot)
   # words.add(phonetique)
    line = f.readline()

# words=['archipelle','archi','pelle']

for word in words:
    current=root
    for letter in word:
        if letter not in current.childrens:
            current.childrens[letter]=Node()
        current=current.childrens[letter]
    current.isWord=True
            


def isWord(word:str):
    current=root
    for letter in word:
        if letter in current.childrens:
            current=current.childrens[letter]
        else:
            return False
  #  print("oui",word)
    return current.isWord

def subwords(subword:str):
    res=[]
    for i in range(0, len(subword)+1):
        if isWord(subword[:i]):
            sub=subwords(subword[i:])
            if len(sub)>0 or i==len(subword):
                res.append([subword[:i], sub])
    
    return res
for word in words:
    sub = subwords(word)
    if len(sub)>1:
        print(sub)

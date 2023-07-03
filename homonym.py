from nltk.corpus import wordnet as wn
for word in wn.all_lemma_names():
    similar=wn.synsets(word)
    next=False
    for i in range(len(similar)-1):
        if next:
            break
        for j in range(i+1,len(similar)):
            if similar[i].wup_similarity(similar[j])<0.07:
                print(similar[i])
                print(similar[i].definition())
                print(similar[j].definition()+'\n')
                next=True
                break
       #     print(similar[i].lch_similarity(similar[j]))
            """
            if similar[i].wup_similarity(similar[j])<0.1:
                print(similar[i])
                next=True
                break
            """
        




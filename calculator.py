# https://gist.githubusercontent.com/urielha/6c11c29073dddbb9a0b9a1b92c1af3be/raw/2eb2609d7fbb8a00201ad4f6518bec34438778fa/calculator.py

import gensim.downloader

model =  gensim.downloader.load('glove-wiki-gigaword-100')


class Calculator():
    def __init__(self, s):
        self._s = s.replace(' ','')  
        self._i = 0
        self._len = len(s)
        self._err = False
    
    def next(self):
        self._i += 1
        
    def take(self):
        l = self._len
        j = i = self._i
        s = self._s
        if j<l and s[j] == '(':
            self.next()
            n = self.calc()
            if s[self._i] != ')':
                raise Exception()
            self.next()
            return n
        while j < l and s[j].isalpha():
            j += 1
        self._i = j
        if i == j:
            raise Exception()
        if s[i:j] in model:
            return model.get_vector(s[i:j])
        raise Exception(f"Word '{s[i:j]}' not found")
    
    def mul(self):
        res = self.take()
        l = self._len
        s, i = self._s, self._i
        while self._i < l and s[self._i]  == ".":
            self.next()
            num = self.take()
            res = res * num
        return res
    
    def plus_minus(self):
        res = self.mul()
        l = self._len
        s, i = self._s, self._i
        while self._i < l and s[self._i] in ('+', '-'):
            op = s[self._i]
            self.next()
            num = self.mul()
            if op == '+':
                res = res + num
            if op == '-':
                res = res - num
        return res

    def calc(self):
        try:
            return self.plus_minus()
        except Exception as e :
            if not self._err:
                print('Parsing Error at index {}.'.format(self._i),e)
            self._err = True
        return None
    
    def calcword(self):
            final_vector=self.calc()
            if final_vector is not None:
               return [x[0] for x in model.most_similar(positive=[final_vector])]

while True:
    print(">> ",end="")
    print("=",Calculator(input()).calcword())

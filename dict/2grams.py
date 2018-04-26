# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 08:15:41 2018

@author: gogoing
"""


import itertools
from collections import Counter
import pandas as pd


class Double:
    '''输入分词好了之后的list对象，进行双连词处理
    还有得到每一个单词,同时过滤低频词的工具也在里面'''
    
    def __init__(self, fc = None):
        self.fc = fc
            
    def get_one(self,fc):
        ''' 将输入的分词变为每一单的词，如[[你好 周五],[赶快 复习]]
            变为[你好,周五,赶快,复习]'''
        def fff(x):
            return x.split(" ")
        
        all1 = list(map(fff, fc))
        all1 = list(itertools.chain.from_iterable(all1))
        return all1
    
    def __double(self,t):
        '''双连词构造'''
        t = t.split(" ")
        cutone = t[:-2]
        lag = t[1:]
        double = []
        for i, j in zip(cutone,lag):
            double.append(i+"cut"+j) 
        return double
    
    def get_double(self,fc):
        ''' 得到双连词如[a,b,c,d] -> [ab, bc, cd]'''
        res = [self.__double(i) for i in fc]
        res = list(itertools.chain.from_iterable(res))
        return res
    
    def filter_freq(self, res, p):
        ' 用于过滤掉低频的字段'
        res = Counter(res)
        df = pd.DataFrame(pd.Series(res))
        df = df[df[0] > p]
        return list(df.index)
 
    

class Pmi:
    def __init__(self, double= None, filter1=None, one=None, neg=None, pos=None):
        self.double = double
        self.filter1 = filter1
        self.one = one
        self.neg = neg
        self.pos = pos
        
    def __pmi_neg(self, x):
        pmi = 0.0
        g = 0.0
        cut1 = x.split('cut')
       
        px = self.one.count(cut1[0])/len(self.one)
        if cut1[0] in self.neg.keys(): g = 0.5
        
        py = self.one.count(cut1[1])/len(self.one)
        if cut1[1] in self.neg.keys(): g = 0.5
        
        pxy =self.double.count(x)/(len(self.double)+1)
        pmi = pxy/px*py + g
        return pmi
    
    def __pmi_pos(self, x):
        pmi = 0.0
        g = 0.0
        cut1 = x.split('cut')
        
        px = self.one.count(cut1[0])/len(self.one)
        if cut1[0] in self.pos.keys(): g = 0.5
        
        py = self.one.count(cut1[1])/len(self.one)
        if cut1[1] in self.pos.keys(): g = 0.5
        
        pxy =self.double.count(x)/(len(self.double)+1)
        pmi = pxy/px*py + g
        return pmi
    
    def get_neg_pmi(self):
        print('计算进行中...')
        p = list(map(self.__pmi_neg, self.filter1))
        return p
    
    def get_pos_pmi(self):
        print('计算进行中...')
        p = list(map(self.__pmi_pos, self.filter1))
        return p
    
    

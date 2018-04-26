# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:22:22 2018

@author: gogoing

新词发现，的2-grams->计算pmi值
"""


#%%
import re
import itertools
from collections import Counter
import pandas as pd

def double(t):
    t = t.split(" ")
    cutone = t[:-2]
    lag = t[1:]
    double = []
    for i, j in zip(cutone,lag):
        double.append(i+"cut"+j) 
    return double


res = [double(i) for i in fc]
res = list(itertools.chain.from_iterable(res))

a = Counter(res)

# 过滤低频词，去重复
z = pd.DataFrame(pd.Series(a))
z = z[z[0] > 5]

# 取出来
res1 = list(set(z.index))


def fff(x):
    return x.split(" ")

all1 = list(map(fff, fc))
all1 = list(itertools.chain.from_iterable(all1))


def pmi_neg(res1):
    pmi = 0.0
    g = 0.0
    cut1 = res1.split('cut')
    px = all1.count(cut1[0])/len(all1)
    if cut1[0] in neg.keys(): g = 0.5
    py = all1.count(cut1[1])/len(all1)
    if cut1[1] in neg.keys(): g = 0.5
    pxy =res.count(res1)/(len(res)+1)
    pmi = pxy/px*py + g
    return pmi

def pmi_pos(res1):
    pmi = 0.0
    g = 0.0
    cut1 = res1.split('cut')
    px = all1.count(cut1[0])/len(all1)
    if cut1[0] in pos.keys(): g = 0.5
    py = all1.count(cut1[1])/len(all1)
    if cut1[1] in pos.keys(): g = 0.5
    pxy =res.count(res1)/(len(res)+1)
    pmi = pxy/px*py + g
    return pmi

p = list(map(pmi_neg, res1))
    
z = pd.DataFrame({'a':res1, 'b':p})
z.to_csv('bbb.csv')
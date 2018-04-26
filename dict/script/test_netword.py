# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 08:15:51 2018

@author: gogoing
"""

import pandas as pd
test_path = r'E:\job\正负分类\dict\input/test.xlsx'


test = pd.read_excel(test_path)['内容']  


art = test[1]
art = art.replace("-", "").replace("\x01", "").replace("—", "")

import re
Ju = re.split("。| ”", art)



art = re.sub("。|、|”|“|:|,|，|（|）|：","", art)
import jieba
test_fc=" ".join(jieba.cut(art))
test_fc

#%% 
netword = r'E:\job\正负分类\dict\dict\netword\BosonNLP_sentiment_score.txt'

import codecs

f = codecs.open(netword, 'r', 'utf-8')
res = []
for i in f.readlines():
    res.append(i.replace("\n", ""))
f.close()

# 如果是空的那么就不能变为dict
res.remove("")

def spl(x):
    return x.split(" ")

z = list(map(spl, res))
z[0][0]

senti_dict = {}
for i in z:
    senti_dict[i[0]] = i[1]

# %%    
'''
    这个好像没有负的怎么，分个球球
    大多数都是正面词啊啊
'''
def fc_score(test_fc):
    score = []
    for i in test_fc.split(" "):
        if i in list(senti_dict.keys()):
            score.append(float(senti_dict[i]))
        
    score = sum(score, 0)
    return score    
    
def aa(art):
    art = re.sub("。|”|“|:|,|，|（|）|：","", art)
    import jieba
    test_fc=" ".join(jieba.cut(art))
    test_fc    
    return test_fc
    
    
score = []
num = int(1)
for i in test:
    fc = aa(i)
    score.append(fc_score(fc))
    print(num)
    num += 1 
    
#%%
print(score)
import numpy as np
np.mean(score)
np.median(score)
np.std(score)

#%%

    
    
    
    
    
    
    
    
    
    
    
    

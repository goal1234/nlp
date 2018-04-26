# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:59:25 2018

@author: gogoing
"""

import pandas as pd
test_path = r'E:\job\正负分类\dict\input/test.xlsx'


test = pd.read_excel(test_path)['内容']  


art = test[3]
art = art.replace("-", "").replace("\x01", "").replace("—", "")

import re
Ju = re.split("。| ”", art)



art = re.sub("。|”|“|:|,|，|（|）|：","", art)
import jieba
test_fc=" ".join(jieba.cut(art))
test_fc


#%%
import codecs

neg = r'E:\job\正负分类\dict\dict\tsinghua\tsinghua.negative.gb.txt'
pos = r'E:\job\正负分类\dict\dict\tsinghua\tsinghua.positive.gb.txt'


def openfile(path):
    f = codecs.open(path, 'r')
    res = []
    for i in f.readlines():
        res.append(i.replace("\n", "").replace(" ", ""))
        
    return res

neg = openfile(neg)
pos = openfile(pos)
#%%



    
fc = test_fc.split(" ")
    
        
    # 第一个分词和pos第一个信息 
def one_pmi(fc, pos, position):
    '''为什么“的”pmi很大, 在pos中，大于neg'''
    res = []
    for k in range(len(pos)):       
        pxy = []
        i = fc[position]
        p = pos[k]
        
        # 在文章中出现的概率
        pi = fc.count(i)/len(fc)
        pp = fc.count(p)/len(fc)
        a = list(map(lambda x: x == i, fc))
        b = list(map(lambda x: x == p, fc))
        p1 = min(sum(a,0), sum(b, 0))
        pxy = p1/len(fc)

        try:
            pmi = pxy/(pi*pp)
        except:
            pmi = 0
            
        res.append(pmi)
    return sum(res,0)

def pmi_cal(fc, pos):
    res = []
    for i in range(len(fc)):
        print(i/len(fc))
        r = one_pmi(fc, pos, i)
        res.append(r)
    return sum(res, 0)
          
    
def so_pmi(fc, pos, neg):
    a = pmi_cal(fc, pos)
    b = pmi_cal(fc, neg)
    if a/b > 2.0:
        sent = "pos"
    elif(a/b < 0.6):
        sent = "neg"
    else:
        sent = "neu"
    return sent


# 这一步太慢了
# 字典的长度也太长了
import datetime
start = datetime.datetime.now()
tt = so_pmi(fc, pos, neg)
end = datetime.datetime.now()

spend = start - end
#%% pmi
pos = ['遂意', '得救', '稳帖', '谦诚', '赞成', '谦虚谨慎', '清淡', '佳境', '患得患失', '不惑']
dict(enumerate(pos))

a = {}
for i in pos:
    a[i] = 1
    
    
   
        

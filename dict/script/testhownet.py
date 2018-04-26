# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:46:44 2018

@author: gogoing

利用模糊标签进行
比如评论的标签
通过提取模糊标签进行机器学习

字典进行查询，随着字典的变多，准确性提高，但是其查询次数增大，所以时间变慢了
似乎这个很难克服这个东东

对于短文字典的方法可以考虑，不过长文本似乎就容易尴尬了

对于正常的文章是pos词出现的概率高于neg
"""

import codecs
import itertools
import numpy as np
import re
import jieba
import jieba.analyse
    
pos2 = r'E:\job\正负分类\dict\dict\hownet\知网_正面评价词语.txt'
pos1 = r'E:\job\正负分类\dict\dict\hownet\知网_正面情感词语.txt'

neg2 = r'E:\job\正负分类\dict\dict\hownet\知网_负面评价词语.txt'
neg1 = r'E:\job\正负分类\dict\dict\hownet\知网_负面情感词语.txt'

point1 = r'E:\job\正负分类\dict\dict\hownet\感知_觉得.txt'
point2 = r'E:\job\正负分类\dict\dict\hownet\感知_认为.txt'

grade6 = r'E:\job\正负分类\dict\dict\hownet\程度_极.txt'
grade5 = r'E:\job\正负分类\dict\dict\hownet\程度_超.txt'
grade4 = r'E:\job\正负分类\dict\dict\hownet\程度_很.txt'
grade3 = r'E:\job\正负分类\dict\dict\hownet\程度_较.txt'
grade2 = r'E:\job\正负分类\dict\dict\hownet\程度_稍.txt'
grade1 = r'E:\job\正负分类\dict\dict\hownet\程度_欠.txt'

neg = r'E:\job\正负分类\dict\dict\tsinghua\tsinghua.negative.gb.txt'
pos = r'E:\job\正负分类\dict\dict\tsinghua\tsinghua.positive.gb.txt'

ntneg = r'E:\job\正负分类\dict\dict\ntusd\ntusd-negative.txt'
ntpos = r'E:\job\正负分类\dict\dict\ntusd\ntusd-positive.txt'

stop_dict =r'E:\job\正负分类\dict\dict\stopwords.txt'



def Read_txt(filename):
    try:
        outlist = []
        with codecs.open(filename) as f:
            for i in f.readlines():
                outlist.append(i.replace("\n","").replace(" ", ""))
        f.close()
        print("txt读入完成，输出list")
        return outlist
    except:
        f = codecs.open(filename, 'r', 'utf-8')
        res = []
        for i in f.readlines():
            res.append(i.replace("\n", "").replace("\r","").replace(" ",""))
        f.close()
        print("txt读入完成，输出list")
        return res
        
scoretsing1 = Read_txt(pos)
scoretsing2 = Read_txt(neg)

scorent1 = Read_txt(ntpos)
scorent2 = Read_txt(ntneg)

score1 = Read_txt(pos1)
score2 = Read_txt(pos2)

scoren1 = Read_txt(neg1)
scoren2 = Read_txt(neg2)

scorep1 = Read_txt(point1)
scorep2 = Read_txt(point2)

scoreg1 = Read_txt(grade1) # 1.1
scoreg2 = Read_txt(grade2) # 1.2
scoreg3 = Read_txt(grade3) # 1.3
scoreg4 = Read_txt(grade4) # 1.4
scoreg5 = Read_txt(grade5) # 1.5
scoreg6 = Read_txt(grade6) # 1.6

stop_dict = Read_txt(stop_dict)

#%%

def Make_dict(file, score):
    if type(file) != list:
        return print("file应该为list")
    if type(score) != list:
        return print("score应该为list")
    
    key = []
    for i in file:
        key += i
        
    value = []
    start = int(0)
    for i in score:
        value += list(itertools.repeat(i, len(file[start])))
        start += 1
    print("Make a dict \n\n" )
    return dict(zip(key, value))


dict_pos = Make_dict([score1, score2, scoretsing1, scorent1],[1, 2, 1, 1])
dict_neg = Make_dict([scoren1, scoren2, scoretsing2, scorent2], [1, 2, 1,1])

len(set(list(dict_pos.keys())))/len(list(dict_pos.keys()))

dict_point = Make_dict([scorep1, scorep2], [2, 4])

dict_beta = Make_dict([scoreg1, scoreg2, scoreg3, scoreg4, scoreg5, scoreg6], [1.1, 1.2, 1.3, 1.4, 1.5, 1.6])

def Base_score(file, dictin):
    base_score = []
    for i in file.split(" "):
        if i in dictin.keys():
            base_score.append(dictin[i])
    return sum(base_score, 0)


#%%
def Score(test, dictin, dict_beta, dict_point, position):
    position = int(position)
    base_score = []
    beta_score = []  #程度词
    base_point = []  #观点词
    start = int(0)
    t = test.split(" ")
    if len(t) < position: position = int(2)
    
    for i in t:
        if i in dictin.keys():
            # 多了5次的循环
            if position !=0:
                if t.index(i) >= position:
                    index = t.index(i)
                    t1 =t[index - position:index]
                    for j in t1:
                        if j in dict_beta.keys():
                            beta_score.append(dict_beta[j])
                        if j in dict_point.keys():
                            base_point.append(dict_point[j])
                            
            base_score.append(dictin[i])
        start += 1
        
    base_score = sum(base_score, 0)/len(t)
    base_point = sum(base_point, 0)/len(t)
    
    if beta_score == []:
        beta_score = 1
    elif len(beta_score) > 10:
        beta_score = 1.6
    else:
        beta_score = max(np.array(beta_score))
        
        
    p = (base_score+base_point)*beta_score
    p = round(p, 2)
    return p

def Fenci(test, stop_dict):
    res = []
    s = int(0)
    for art in test:
        art = art.replace("-", "").replace("\x01", "").replace("—", "")
        art = re.sub("。|、|”|“|:|,|，|（|）|：","", art)
        test_fc=[i for i in jieba.cut(art) if i not in stop_dict]
        res.append(" ".join(test_fc))
        print(s)
        s += 1
    return res


import pandas as pd
test_path = r'E:\job\正负分类\dict\input/test.xlsx'


test = pd.read_excel(test_path)['内容']  

fc = Fenci(test, stop_dict)


def p_neg(x):
    return Score(x, dict_neg, dict_beta, dict_point, 5)
    
def p_pos(x):
    return Score(x, dict_pos, dict_beta, dict_point, 5)

def textrank_neg(x):
    a = " ".join(jieba.analyse.textrank(x))
    return Score(a, dict_neg, dict_beta, dict_point, 0)

def textrank_pos(x):
    a = " ".join(jieba.analyse.textrank(x))
    return Score(a, dict_pos, dict_beta, dict_point, 0)

s1 = list(map(textrank_neg, fc))    
s2 = list(map(textrank_pos, fc))

nn = list(map(p_neg, fc))
pp = list(map(p_pos, fc))



aa  = pd.DataFrame([np.array(nn), np.array(pp)])
aa = aa.T
aa['all'] = aa.sum(axis= 1)
aa['c'] = aa[1]/aa[0]
aa['textrankneg'] = s1
aa['textrankpos'] = s2

def panduan(neg, pos, al, c, textrankneg, textrankpos):
    tk = 0
    if al >= 0.6:
        if c >= 1.2:
            res = 20
        elif c >= 1:
            res = 15
        else:
            res = 5
    elif al >= 0.3:
        if c >=1.5:
            res = 15
        elif c >= 1:
            res = 12
        else:
            res = 5
    else:
        if c >= 2:
            res = 15
        elif c>= 1:
            res = 10
        else:
            res = 5
    
    if textrankpos > textrankneg:
        tk = 5
    
    p = tk*0.2 + res*0.8
    return p
    
    
nn = np.array(nn)
pp = np.array(pp)

p = map(panduan,aa[0], aa[1],aa['all'], aa['c'],aa['textrankneg'], aa['textrankpos'])
p = list(p) 

aa['res'] = p 

def label(x):
    if x >= 10:
        label = '正面'
    elif x <= 4.5:
        label = '负面'
    else:
        label = '中性'
    return label

aa['label'] = aa['res'].apply(label)
aa['txt'] = test

aa.to_excel("aaa.xlsx")
#%%
len([i for i in p if i <= 4.5 ])/len(p)

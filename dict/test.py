# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:15:38 2018

@author: gogoing
"""

import LoadDict
import ScoreDict
import pandas as pd


# 输入测试数据
test_path = r'E:\job\正负分类\dict\input\neg.xls'
tt = pd.read_excel(test_path)
tt.columns = ['aa']
test = tt['aa'] 

# 载入数据字典
a = LoadDict.MakeDict()
pos = a.load_pos()
neg = a.load_neg()
point = a.load_point()
beta = a.load_beta()
stop = a.stop_dict


# 分词处理
fc = ScoreDict.Fenci(test, stop)

# 进行打分
c = ScoreDict.MakeScore()
c.dict_neg = neg
c.dict_pos = pos
c.dict_point = point
c.dict_beta = beta
c.fc = fc

# 开始进行
aaa = c.Make_it()

# 标签--> 输出正面，负面，中性
ggg = ScoreDict.get_label(aaa)


# 输出文件
ScoreDict.store(ggg, tt, 'neg测试2')


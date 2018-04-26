# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:31:51 2018

@author: gogoing
"""

import re

line = '作者倒是个很小资的人,但有点自恋的感觉,书并没有什么大帮助'

p = re.compile(r'小资.*人')
p.findall(line)


line = '如果有这个东东，那么正的是太好！！'
p1 = re.compile(r'如果.*不太好')
p1.findall(line)

line = '这个玩意，好不容易才好。'
p2 = re.compile(r"，好不容易")
p2.findall(line)

line = "那么好，那么美，那么"
p3 = re.compile(r'那么.*那么')
p3.findall(line)


t = test[1]
t = t.replace("\x01", "")

t = t.split("。")


def P1(x):
    return p1.findall(x) != []

list(map(P1, t))


line = '用它我也没多记住什么单词啊！大家要是想学单词，有很多方式，没必要买这个浪费钱，我可是后悔死洌！'

def count1(line):
    '''
        是由有感叹句
    '''
    var = line.split("！")
    return len(var)

count1(line)


def count2(line):
    '''
        反问句
    '''
    p1 = re.compile(r'.*吗？|呢？')
    return p1.findall(line) != []



    
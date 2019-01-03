# -*- coding: cp936 -*-
import time
start = time.time()
import sys
import codecs
sys.setrecursionlimit(1000000)
f1=codecs.open('dictionary1.txt','r')
list1=[]
for line in f1:
    line = line.strip()
    if len(line) == 0:
        continue
    line =  line.split()
    for each in line:
        if each in list1:
            continue
        else:
            list1.append(each)

f=codecs.open('FMM.txt','w')

def getSeg(text,temp):# 获取分词
    if not text:
        return ''
    if len(text) == 1:
        return text
    if text in list1:
        return text
    else:
        if temp==1:
            text=text[:-1]
        else:
            text = text[1:]
        return getSeg(text,temp)

def main(temp):
    global list1 #定义全局变量
    global a
    a = []
    b = []
    f2=codecs.open('pku_test.txt','r')#打开文件
    for line in f2:
        test_str=line.strip()
        while test_str: #while循环
            seg_str = getSeg(test_str,temp) #调用
            a.append(seg_str)
            seg_len = len(seg_str)
            if temp==1:
                test_str = test_str[seg_len:]
            else:
                test_str = test_str[0:len(test_str)-seg_len]
        if temp==1:
            b=a
        else:
            b = list(reversed(a))
        for i in b:
            f.write(i+'  ')
        f.write('\n')
        a=[]
        b=[]
    f.close()
    f1.close()
    f2.close()
    print(time.time()-start)

if __name__ == '__main__':
    main(1)

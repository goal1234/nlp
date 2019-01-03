# -*- coding: cp936 -*-
import time
start = time.time()
import sys
import codecs
f1=codecs.open('dictionary3.txt','r')

word_dict={}#打开词典
for line in f1:
    line = line.strip()
    if len(line) == 0:
        continue
    line =  line.split()
    for each in line:
        if each in word_dict:
            word_dict[each]=word_dict[each]+1
        else:
            word_dict[each]=1

def main():
    global start #定义全局变量
    start = time.time()
    a = []
    b = []
    f=codecs.open('BMM.txt','w')
    f2=codecs.open('pku_test.txt','r')#打开文件
    for line in f2:
        line=line.strip()
        len1 = len(line)
        k = 0
        i = len1
        max1 = 22
        while len1!=0 or i!=k: #while循环
            if len1 < max1:
                max1 = len1
            a=line[i-max1:i]
            while (a not in word_dict) and len(a)!=1:
                a=line[i-len(a)+1:i]
            b.append(a)
            len1 = len1 - len(a)
            i=i-len(a)
        c = list(reversed(b))
        for i in c:
            f.write(i+'  ')
        f.write('\n')
        a=[]
        b=[]
    f.close()
    f2.close()
    f1.close()


if __name__ == '__main__':
    main()
    print(time.time()-start)

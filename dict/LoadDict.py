# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 08:17:49 2018

@author: gogoing
"""
import codecs
import itertools

class MakeDict:
    def __init__(self):
        self.pos2 = r'E:\job\正负分类\dict\dict\hownet\知网_正面评价词语.txt'
        self.pos1 = r'E:\job\正负分类\dict\dict\hownet\知网_正面情感词语.txt'
        self.neg2 = r'E:\job\正负分类\dict\dict\hownet\知网_负面评价词语.txt'
        self.neg1 = r'E:\job\正负分类\dict\dict\hownet\知网_负面情感词语.txt'
        
        self.point1 = r'E:\job\正负分类\dict\dict\hownet\感知_觉得.txt'
        self.point2 = r'E:\job\正负分类\dict\dict\hownet\感知_认为.txt'
        
        self.grade6 = r'E:\job\正负分类\dict\dict\hownet\程度_极.txt'
        self.grade5 = r'E:\job\正负分类\dict\dict\hownet\程度_超.txt'
        self.grade4 = r'E:\job\正负分类\dict\dict\hownet\程度_很.txt'
        self.grade3 = r'E:\job\正负分类\dict\dict\hownet\程度_较.txt'
        self.grade2 = r'E:\job\正负分类\dict\dict\hownet\程度_稍.txt'
        self.grade1 = r'E:\job\正负分类\dict\dict\hownet\程度_欠.txt'
        
        self.neg = r'E:\job\正负分类\dict\dict\tsinghua\tsinghua.negative.gb.txt'
        self.pos = r'E:\job\正负分类\dict\dict\tsinghua\tsinghua.positive.gb.txt'
        
        self.ntneg = r'E:\job\正负分类\dict\dict\ntusd\ntusd-negative.txt'
        self.ntpos = r'E:\job\正负分类\dict\dict\ntusd\ntusd-positive.txt'
        
        self.stop_dict =r'E:\job\正负分类\dict\dict\stopwords.txt'
        
        self.scoretsing1 = self.Read_txt(self.pos)
        self.scoretsing2 = self.Read_txt(self.neg)
        
        self.scorent1 = self.Read_txt(self.ntpos)
        self.scorent2 = self.Read_txt(self.ntneg)
        
        self.score1 = self.Read_txt(self.pos1)
        self.score2 = self.Read_txt(self.pos2)
        
        self.scoren1 = self.Read_txt(self.neg1)
        self.scoren2 = self.Read_txt(self.neg2)
        
        self.scorep1 = self.Read_txt(self.point1)
        self.scorep2 = self.Read_txt(self.point2)
        
        self.scoreg1 = self.Read_txt(self.grade1) # 1.1
        self.scoreg2 = self.Read_txt(self.grade2) # 1.2
        self.scoreg3 = self.Read_txt(self.grade3) # 1.3
        self.scoreg4 = self.Read_txt(self.grade4) # 1.4
        self.scoreg5 = self.Read_txt(self.grade5) # 1.5
        self.scoreg6 = self.Read_txt(self.grade6) # 1.6
        
        self.stop_dict = self.Read_txt(self.stop_dict)
                
        
    def Read_txt(self, filename):
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
        
    def Make_dict(self, file, score):
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
            
    def load_pos(self):
        a =self.Make_dict([self.score1, self.score2, self.scoretsing1, self.scorent1],[1, 2, 1, 1])
        return a
    
    def load_neg(self):
        a  = self.Make_dict([self.scoren1, self.scoren2, self.scoretsing2, self.scorent2], [2, 4, 2, 2])
        return a
    
    def load_point(self):
        a = self.Make_dict([self.scorep1, self.scorep2], [2, 4])
        return a
    
    def load_beta(self):
        a = self.Make_dict([self.scoreg1, self.scoreg2, self.scoreg3, 
                            self.scoreg4, self.scoreg5, self.scoreg6], 
                            [1.5, 1.8, 2, 3, 3.5, 4])
        return a
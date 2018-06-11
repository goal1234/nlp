

    def ner(rm_stop):
        '''

        :return:词性标注的表，对于每一个元组有DATE,MONEY等这样的实体词在里面会被清楚了
        '''

        # 词性标注
        tokens = nltk.pos_tag(rm_stop)

        # 实体命名识别
        entity = nltk.chunk.ne_chunk(tokens)
        tidy = list(entity)
        return tidy


    def get_ner(tidy, what):
        '''
        可能返回空

        :param tidy:输入的一个实体命名树为nltk.tree格式
        :param what: 识别里面有神马：['LOCATION', 'ORGANIZATION', 'PERSON', 'DURATION','DATE', 'CARDINAL', 'PERCENT', 'MONEY', 'MEASURE', 'FACILITY', 'GPE']
        :return:一个被清理过的列表
        '''
        ner_list = []
        for i in tidy:
            i = str(i)
            if i.find(what) == 1:
                i = i.replace(what+" ","")
                i = i.replace("(", "")
                i = i.replace(")", "")
                i = i.replace("/", ",")
                ner_list.append(i)
        return ner_list

    def tidy_ner(gpe):
        '''将输入的树形数据结构中，查找出实体
            可以在直接调用对于上面['LOCATION, PERSON...]
            test = RemoveNer(rm_stop)
            GPE = test.tidy_ner('GPE')

        '''

        res = []
        for i in gpe:
            if len(i.split(" ")) < 2:
                temp1 = i.split(",")[0]
            else:
                more = i.split(" ")
                for_store = []
                for j in more:
                    first = j.split(",")[0]
                    for_store.append(first)
                    temp1 = " ".join(for_store)
            res.append(temp1)
        return res


    def remove_ner(self):
        '''
        调用上面的方法进行为韦德字典进行后面的情感输出
        :return:
        '''
        print("正在进行去除相关的实体")
        rm_data = []
        tidy = ner(rm_s)
        dd = ['LOCATION', 'ORGANIZATION', 'PERSON', 'DURATION','DATE',
              'CARDINAL', 'PERCENT', 'MONEY', 'MEASURE', 'FACILITY', 'GPE']

        for i in dd:
            print(i)
            for_tidy = get_ner(tidy, i)  # for tidy 返回空
            rm_data.extend(for_tidy)

        # 清理完成后的list
        input_sent = [w for w in self.rm_stop if w not in rm_data]
        return input_sent
#!/usr/bin/env pytho
# -*- coding:utf-8 -*-
import pymysql

# 创建连接
conn = pymysql.connect(host='10.0.12.3', port=3306, user='root', passwd='12345678', db='test', charset='utf8')
# 创建游标
cursor = conn.cursor()

cursor.executemany("insert into nlp_test(pos, neu, neg, pos_neg, top5, person, location, similar, count_similar)"
                   "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", to_sql)


cursor.executemany("insert into nlp_test(pos, neu, neg, pos_neg, top5, person, location, similar, count_similar) "
                   "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",to_sql)
# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

# ---进行数据获取

def sql_input():
    import pymysql

    # 创建连接
    conn = pymysql.connect(host='10.0.12.3', port=3306, user='root', passwd='12345678', db='test', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    cursor.execute("select iid, title, content from clean_fd_content_particle_HWW2CRAW")
    result = cursor.fetchall()
    conn.commit()
    # 关闭游标
    cursor.close()
    return result


a = sql_input()
iid = [i[0] for i in a]
title = [i[1] for i in a]
content = [i[2] for i in a]


content =[i.split("<p>") for i in content]



f = open('iid.txt','wb')
import pickle
pickle.dump(iid, f)
f.close()

f = open('title.txt','wb')
pickle.dump(title, f)
f.close()

f = open('content.txt', 'wb')
pickle.dump(content, f)
f.close()

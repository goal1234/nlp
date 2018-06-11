import pandas as pd

temp = pd.read_csv('data/export2.csv')
temp.columns




def get_csv(path):
    if isinstance(path, str) == False:
        return "Your input must be str"
    try:
        res =[]
        with open(path, 'rb') as f:
            print('csv is reading......')
            for i in f.readlines():
                res.append(i)
        print("finsh the data input ")
        return res

    except Exception as e:
        print("check your input")
        print(str(e))


temp = get_csv('data/text1.csv')

def change(i):
    return str(i, encoding='utf-8')



import csv

csvfile = open('data/text1.csv', 'rb')
reader = csv.reader(open('data/text1.csv','rb'))

for i in reader:
    print(i)


import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="Utxwp5F5lIyFesnf", host="223.203.96.250", port="5432")

cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
cur.execute("SELECT * FROM test;")
cur.fetchone()


cur.execute("select id from fd_content_particle_HWW2CRAW;")
rows = cur.fetchall()
print(rows)
conn.commit()
cur.close()
conn.close()

import argparse
import sqlite3
import random 
par = argparse.ArgumentParser()
par.add_argument("a",type = int, help = "Num str")
par.add_argument("k",type = str, help = "Name table")
x = par.parse_args()
K = x.k
Z = x.a
Table1 = sqlite3.connect('server.Tablet1')
sql = Table1.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" %K)
Table1.commit()
for i in range(Z):
    U = random.randint(1,100)
    sql.execute("INSERT INTO %s VALUES(?,?)" %K, (i+1,U))
sql.execute("SELECT * FROM %s" %K)
print(sql.fetchall())

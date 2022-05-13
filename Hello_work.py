import argparse
import sqlite3
import random 
import os
def multi():
    Table1 = sqlite3.connect('%s.db' %TABLE.name) 
    sql = Table1.cursor()
    Table_Length = 20
    for i in range (TABLE.num):
        Name_Tab_s = 'Table' + str(i+1)
        sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" %Name_Tab_s)                 #  Создает бд с произвольным кол-вом таблиц и произвольной длиной таблиц
        Table1.commit()
        for i in range(Table_Length):
            Random_number = random.randint(1,100)
            sql.execute("INSERT INTO %s VALUES(?,?)" %Name_Tab_s, (i+1,Random_number))# 
        sql.execute("SELECT * FROM %s" %Name_Tab_s)
        print('\n'+Name_Tab_s) 
        print(sql.fetchall())  
        print('\n\n\n') 
def create():
    Table1 = sqlite3.connect('%s.db' %TABLE.name) 
    sql = Table1.cursor()
    Table_Length = 20
    sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" %TABLE.TAB)                 #  Создает бд c таблицей произвольного имени
    for i in range(Table_Length):
        Random_number = random.randint(1,100)
        sql.execute("INSERT INTO %s VALUES(?,?)" %TABLE.TAB, (i+1,Random_number))# 
    sql.execute("SELECT * FROM %s" %TABLE.TAB)
    print('\n'+TABLE.TAB) 
    print(sql.fetchall())  
    print('\n\n\n') 

par = argparse.ArgumentParser()
subparser = par.add_subparsers()  
CREATE_Y_T = subparser.add_parser('create', help = 'Create Table')
CREATE_Y_T.add_argument("name",type = str , help = "Name of db that you need to connect")
CREATE_Y_T.add_argument("TAB",type = str , help = "Name of table")
Cr_m_t = subparser.add_parser('multi', help = 'Create Table')
Cr_m_t.add_argument("name",type = str , help = "Name of db that you need to connect")
Cr_m_t.add_argument("num",type = int, help = "Number of Tables you need to create")
Cr_m_t.set_defaults(func=multi)
CREATE_Y_T.set_defaults(func=create)
TABLE = par.parse_args() 
TABLE.func()
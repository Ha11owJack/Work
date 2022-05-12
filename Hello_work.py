import argparse
import sqlite3
import random 
import os
par = argparse.ArgumentParser() 
subparser = par.add_subparsers(dest = "command")  
Create_Y_T= subparser.add_parser('create', help = 'Create Table')
Cr_m_t = subparser.add_parser('multi', help = 'Create Table')
Create_Y_T.add_argument("Name_create",type = str, help = "Name of db that you need to connect")
Create_Y_T.add_argument("Tab",type = str, help = "Name of Table")
Cr_m_t.add_argument("Name_multi",type = str, help = "Name of db that you need to connect")
Cr_m_t.add_argument("Tab_num",type = int, help = "Number of Tables you need to create")
TABLE = par.parse_args() 

if TABLE.command == "create": 
    NameTab = TABLE.Tab
    Table1 = sqlite3.connect('%s.db' %TABLE.Name_create) 
    sql = Table1.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" %NameTab)                    # Создает бд , с таблицей произвольного имени и длины
    Table1.commit()
    Table_Length = 20
    for i in range(Table_Length): 
        Random_number = random.randint(1,100)
        sql.execute("INSERT INTO %s VALUES(?,?)" %NameTab, (i+1,Random_number))
    sql.execute("SELECT * FROM %s" %NameTab) 
    print('\n'+NameTab) 
    print(sql.fetchall()) 

elif TABLE.command == "multi": 
    Table1 = sqlite3.connect('%s.db' %TABLE.Name_multi) 
    sql = Table1.cursor()
    Table_Length = 20
    for i in range (TABLE.Tab_num):
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
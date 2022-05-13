import argparse
import sqlite3
import random 


def multi():
    Table = sqlite3.connect('%s.db' 
                            %Table_work.name) 
    sql = Table.cursor()
    Table_Length = 20
    for i in range(Table_work.num):
        Name_Tabs = Table_work.name + ".db " + str(Table_Length) + "(" + str(i+1) + ")"
        sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" 
                    %Name_Tabs)                                                                    #  Создает бд с произвольным кол-вом таблиц и произвольной длиной таблиц
        Table.commit()
        for i in range(Table_Length):
            Random_number = random.randint(1,100)
            sql.execute("INSERT INTO %s VALUES(?,?)" 
                        %Name_Tabs, (i+1,Random_number))
        sql.execute("SELECT * FROM %s" 
                    %Name_Tabs)
        print('\n'+Name_Tabs) 
        print(sql.fetchall())  
        print('\n\n\n') 
    print("Replace id")


def create():
    Table = sqlite3.connect('%s.db' 
                            %Table_work.name) 
    sql = Table.cursor()
    Table_Length = 20
    sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" 
                %Table_work.TAB)                                                                     #  Создает бд c таблицей произвольного имени
    for i in range(Table_Length):
        Random_number = random.randint(1, 100)
        sql.execute("INSERT INTO %s VALUES(?,?)" 
                    %Table_work.TAB, 
                    (i+1,Random_number))
    sql.execute("SELECT * FROM %s" 
                %Table_work.TAB)
    print('\n'+Table_work.TAB) 
    print(sql.fetchall())  
    print('\n\n\n') 


par = argparse.ArgumentParser()
subparser = par.add_subparsers()  
Create_one = subparser.add_parser('create', 
                                    help = 'Create Table')
Create_one.add_argument("-n", "--name", 
                            type = str, 
                            help = "Name of db that you need to connect")
Create_one.add_argument("-t", "--TAB", 
                            type = str, 
                            help = "Name of table")
Create_multi = subparser.add_parser('multi', 
                                    help = 'Create Table')
Create_multi.add_argument("-n", "--name", 
                            type = str, 
                            help = "Name of db that you need to connect")
Create_multi.add_argument("-num", "--num",
                            type = int, 
                            help = "Number of Tables you need to create")
Create_multi.set_defaults(func=multi)
Create_one.set_defaults(func=create)
Table_work = par.parse_args() 
Table_work.func()
print("Replace call subparser to function")
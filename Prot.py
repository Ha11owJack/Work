import argparse
import sqlite3
import random 
def parser():
    high_parser = argparse.ArgumentParser()
    subparser = high_parser.add_subparsers()  
    create_one = subparser.add_parser('create', 
                                    help = 'Create Table')
    create_multi = subparser.add_parser('multi', 
                                    help = 'Create Table')
    high_parser.add_argument("-n", 
                            type = str, 
                            help = "Name of db that you need to connect")
    high_parser.add_argument("-l",
                            type = int, 
                            help = "High of table")
    create_one.add_argument("table", 
                            type = str, 
                            help = "Name of table")
    create_multi.add_argument("number",
                            type = int, 
                            help = "Number of Tables you need to create")
    create_multi.set_defaults(func=multi)
    create_one.set_defaults(func=create)
    table_work = high_parser.parse_args() 
    table_work.func(table_work)

def multi(parser): 
    table = sqlite3.connect('%s.db' 
                            %parser.n) 
    sql = table.cursor()
    for i in range(parser.number):
        vertion = "_" + str(i+1)
        name_tabs = parser.n + str(parser.l) + vertion
        sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" 
                    %name_tabs)                                                                    #  Создает бд с произвольным кол-вом таблиц и произвольной длиной таблиц
        table.commit()
        for i in range(parser.l):
            random_number = random.randint(1,100)
            sql.execute("INSERT INTO %s VALUES(?,?)" 
                        %name_tabs, (i+1,random_number))
        sql.execute("SELECT * FROM %s" 
                    %name_tabs)
        print('\n'+name_tabs) 
        print(sql.fetchall())  
        print('\n\n') 
    print("Replace id\n")


def create(parser):
    table = sqlite3.connect('%s.db' 
                            %parser.n) 
    vertion = "_" + parser.table
    name_tab = parser.n + str(parser.l) + vertion
    sql = table.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" 
                %parser.table)                                                                     #  Создает бд c таблицей произвольного имени
    for i in range(parser.l):
        random_number = random.randint(1, 100)
        sql.execute("INSERT INTO %s VALUES(?,?)" 
                    %parser.table, 
                    (i+1,random_number))
    sql.execute("SELECT * FROM %s" 
                %parser.table)
    print('\n'+name_tab) 
    print(sql.fetchall())  
    print('\n\n') 
    print("Replace id\n")
parser()
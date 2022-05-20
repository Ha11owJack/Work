import argparse
import sqlite3
import random 
import os
def parser():
    high_parser = argparse.ArgumentParser()
    high_parser.add_argument("-n",required = True,
                            type = str, 
                            help = "Name of db that you need to connect")
    subparser = high_parser.add_subparsers()  
    create_multi = subparser.add_parser('multi', 
                                    help = 'Create Table')
    show_table = subparser.add_parser('show', 
                                    help = 'show the Table')                               
    create_multi.add_argument("-l", nargs = '?', const = 5,
                            type = int, 
                            help = "High of table")
    create_multi.add_argument("-t", "--table", required = True, 
                            type = str, 
                            help = "Name of table")
    create_multi.add_argument("-i","--number", nargs='?', const=5, 
                            type = int, 
                            help = "Number of Tables you need to create")
    show_table.set_defaults(func=show)
    create_multi.set_defaults(func=multi)
    table_work = high_parser.parse_args() 
    table_work.func(table_work)


def show(parser):
    user = os.getlogin()# имя юзера(для папки)
    table = sqlite3.connect('/home/%s/%s.db' %(user,parser.n), uri = True)# поиск таблицы в папке
    sql = table.cursor()
    sql.execute("SELECT name FROM sqlite_master WHERE type = 'table';") # выполнение команды поиска таблиц
    print(sql.fetchall())

def multi(parser): 
    table = sqlite3.connect('%s.db' 
                            %parser.n) 
    sql = table.cursor()
    if parser.number <= 0 or parser.l <= 0:
        print("Неверно введены аргументы")
    else:
        for i in range(parser.number):
            vertion = "_" + parser.table + "_" + str(i+1)
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
parser()
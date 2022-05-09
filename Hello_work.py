import argparse #Парсер
import sqlite3
import random 
import os
par = argparse.ArgumentParser() # Создание парсера
subparser = par.add_subparsers(dest = "command") # Объявление субпарсера 
Sub1 = subparser.add_parser('show', help = 'Table') # Создание субпарсера показать список таблиц
Sub2 = subparser.add_parser('create', help = 'Create Table')# Создание субпарсера создание таблиц
Sub2.add_argument("a",type = int, help = "Num str") # Аргумент субпарсера 2 (число)
Sub2.add_argument("k",type = str, help = "Name table")# Аргмент субпарсера 2 (строка)
x = par.parse_args() # Присвоение всеё информации парсера
if x.command == "create": # проверка на слово
    K = x.k # присвоение переменной
    Z = x.a 
    Table1 = sqlite3.connect('server.Tablet1') 
    sql = Table1.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS %s (id INT,N INT)" %K) # Создание произвольной таблицы
    Table1.commit()
    for i in range(Z): #Создание таблицы размером Z
        U = random.randint(1,100)# рандомное число
        sql.execute("INSERT INTO %s VALUES(?,?)" %K, (i+1,U))# Вставка в произвольную таблицу
    sql.execute("SELECT * FROM %s" %K)# Выбрать всё из таблицы
    print(sql.fetchall())# Вывод таблицы
elif x.command == "show":# проверка на слово
    user = os.getlogin()# имя юзера(для папки)
    Table1 = sqlite3.connect('/home/%s/Work/server.Tablet1' %user, uri = True)# поиск таблицы в папке
    sql = Table1.cursor()
    sql.execute("SELECT name FROM sqlite_master WHERE type = 'table';") # выполнение команды поиска таблиц
    print(sql.fetchall())#вывод таблиц
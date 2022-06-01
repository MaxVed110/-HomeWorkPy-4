# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

from ntpath import join
from random import randint, random


def generate(deviation, count, name="file.txt"):
    data = open(name, 'a')
    stringNumbers = ''
    for i in range(count):
        stringNumbers += f'{randint(-deviation, deviation)} '
    data.writelines(f'{stringNumbers} \n')
    data.close


def sort(name):
    data = open(name, 'r')
    newStringNumbers = ''
    for line in data:
        bufString = ''
        bufString += line
        listNumbers = list(map(int, bufString.split()))
        listNumbers.sort()
        newStringNumbers += ' '.join(list(map(str, listNumbers))) + '\n'
    data = open(name, 'a')
    data.writelines(newStringNumbers)
    data.close
    

 
generate(8, 9, 'abc.txt')
sort('abc.txt')

#Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и
#умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.
#Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53)
#является 938-м в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
#Какова сумма очков имен в файле?

from itertools import count


alphabet = {
 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
 25: 'Y', 26: 'Z'}

def sort(name):
    data = open(name, 'r')
    listName = []
    for line in data:
        listName=line.split(',')
    listName.sort()
    data.close
    dataN = open('sort.txt', 'a')
    dataN.writelines(str(listName))
    dataN.close
    return listName

def point(listNames: list):
    count = 0
    for i in range(len(listNames)):
        bufCount = 0
        for k in alphabet.keys():
            for element in listNames[i]:
                if alphabet[k] == element:
                     bufCount += k
        count += bufCount*i
    return count




list = sort('english_names.txt')
countList = point(list)
print(countList)
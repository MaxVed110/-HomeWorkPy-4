# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

def ascendingList(listUser: list):
    count = 0
    dictionaryLen = {}
    dictionaryList = {}
    while(listUser[count] == max(listUser)):
        count += 1
    while(count<len(listUser)):
        newList = []
        maxMinElement = listUser[count]
        newList.append(listUser[count])
        for i in range(count, len(listUser)):
             if(listUser[i] > maxMinElement):
                 maxMinElement = listUser[i]
                 newList.append(listUser[i])
        dictionaryLen[count] = len(newList)
        dictionaryList[count] = newList
        count+=1
    maxDict = [k for k in dictionaryLen.keys() if dictionaryLen[k] == max(dictionaryLen.values())]
    endList = dictionaryList[maxDict[0]]
    return endList
    
        


listU = [9, 9, 5, 2, 3, 7, 5, 8]
newList = ascendingList(listU)
print(newList)

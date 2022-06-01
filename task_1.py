# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

def ascendingList(listUser: list):
    newList = []
    count = 0
    while(listUser[count] >= max(listUser)):
        count += 1
    maxm = listUser[count]
    newList.append(listUser[count])
    for i in range(count, len(listUser)):
        if(listUser[i] > maxm):
            maxm = listUser[i]
            newList.append(listUser[i])
    return newList


listU = [9, 9, 2, 5, 6, 7, 5, 8]
newList = ascendingList(listU)
print(newList)

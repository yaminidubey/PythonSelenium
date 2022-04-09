def selection_sort(list1):
    i = 0
    while i < len(list1)-1:
        j = i + 1
        while j < len(list1):
            if list1[i] > list1[j]:
                list1[i],list1[j] = list1[j],list1[i]
                j += 1
            else:
                j += 1

        i += 1


    return list1

list1 = eval(input())
print(selection_sort(list1))
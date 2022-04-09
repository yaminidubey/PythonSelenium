def insertion_sort(list1):
    i = 1
    while i < len(list1):
        j = i-1
        temp = list1[i]
        while j >= 0:
            if temp < list1[j]:
                list1[j+1] = list1[j]
                list1[j] = temp
                j -= 1
            else:
                break
        i += 1

    return list1
list1 = eval(input())
print(insertion_sort(list1))

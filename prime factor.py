def prime_factor(num):
    i = 1

    list1 = []

    while i <= num:
        if i == 1:
            list1.append(i)
            i += 1
        if i == 2 and num % i == 0:
            list1.append(i)
            i += 1
        else:
            i += 1
        j = 2
        while j <= i:
            if i % j != 0:
                if j == i-1:
                    if num%i == 0:
                        list1.append(i)
                        i += 1
                    else:
                        i += 1
                        break
                else:
                    j += 1
            else:
                break


    return  list1
num = eval(input())
print(prime_factor(num))

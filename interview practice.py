# str1 = "yamini"
# str2 = "dubey"
# str3 = str1 + str2
# print(str3)
# print(len(str3))
# str4 = str3 * 3
# print(str4)
# print(str3[7:-8:-2])
# list1 = ["apple", "orange"]
# list2 = ["grepas","watermelon"]
# list1.insert(0,"banana")
# list1.append("mango")
# print(len(list1))
# list1.remove("apple")
# print(list1)
# list1.extend(list2)
# print(list1)
dict1 = {}
dict1["a"] = 1
dict1["b"] = 2
#del dict["b"]
dict2 = {"c":1, "d":6}
dict1.update(dict2)

dict1 = dict2
dict1.clear()
product = ["orange","apple","greps"]
quality = [12,14,15]
d = dict(zip(product,quality))
print(d)
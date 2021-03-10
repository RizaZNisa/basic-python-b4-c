#1
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)

#2
mylist = [4, 5, ]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)

#3
mylist = [4, 5.3, "apple"]
#         0  1      2
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
print(mylist[2])

for x in mylist:
    print(x)
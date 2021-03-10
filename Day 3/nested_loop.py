list_data = [[1,2],[3,4]]
for i in range(2):
    for j in range(3):
        print("{}  {}".format(i,j) ,end=" ")
    print()

for i in list_data:
    for j in i:
        print(j*5)
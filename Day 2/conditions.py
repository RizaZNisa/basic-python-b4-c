#1
a = 10
b = 4

if a>b :
    print("a lebih besar dari pada b")
elif a<b :
    print("a kurang dari b")
elif a==b :
    print("a sama dengan b")
elif a!=b :
    print("a tidak sama dengan b")
else:
    print("tidak masuk semua kondisi")

#2
a = 4
b = 4

if a>b :
    print("a lebih besar dari pada b")
elif a<b :
    print("a kurang dari b")
elif a==b :
    print("a sama dengan b")
elif a!=b :
    print("a tidak sama dengan b")
else:
    print("tidak masuk semua kondisi")

#3
a = 2
b = 4

if a==b :
    print("a sama dengan b")
elif a!=b :
    print("a tidak sama dengan b")
else:
    print("tidak masuk semua kondisi")

#4
a = 4
b = 45

if a>b :
    print("a lebih besar dari pada b")
elif a<b :
    print("a kurang dari b")
else :
    print("a sama dengan b")

c = 4
d = 5
if c==d :
    print("c sama dengan d")
elif c!=d :
    print("c tidak sama dengan d")
else:
    print("tidak masuk semua kondisi")

#5 contoh penggunaan AND, jadi keduanya harus benar
e = 5
f = 5
if e == 5 and f == 5:
    print ("e dan f sama dengan 5")
else :
    print ("e dan f tidak sama dengan 5")

#6 contoh penggunaan OR, jadi salah satunya harus benar
e = 5
f = 3
if e == 5 or f == 5:
    print ("e dan f sama dengan 5")
else :
    print ("e dan f tidak sama dengan 5")

#6 NOT
g = 3
if not g == 4:
    print("g bukan 4")
else :
    print("g itu 4")
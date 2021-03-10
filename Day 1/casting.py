#utk change / perubahan type data

#float to int
x = 1.9999
print(x)
print(type(x))

y = int(x)      #hanya perubahan / bukan pembulatan
print(y)
print(type(y))  #hasilnya 1 bukan 2

#int to float
a = 1
print (a)
print (type(a))

b = float(a)
print(b)
print(type(b))  #hanya ditambha .0 jadi 1.0

#string to int
umur = "22"
print(umur)
print(type(umur))

umur_integer = int(umur)
print(umur_integer)
print(type(umur_integer))

print("==============================")
panjang = "10" #str = type data untuk tulisan/ huruf, bukan angka, tidak bisa dikalikan
lebar = 2
print(panjang*2)    #tidak bisa krn beda type data, jadinya 10 ada 2 bukan 20
print(panjang*lebar)

#str to int
panjang2 = int(panjang)
print(panjang2)
print(type(panjang2))
print(panjang2*lebar)


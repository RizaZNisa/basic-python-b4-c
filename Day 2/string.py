# STRING OPERATIONS
# Get the character at position 1 (the first character has the position 0)
# H e l l o ,   W o r l  d  !  #spasi dan tanda baca juga termasuk
# 0 1 2 3 4 5 6 7 8 9 10 11 12


a = "Hello, World!"
print (a[1])
print (a[0:5])      #menampilkan huruf ke 0 sampai 5
print (a[:5])
print (a[7:])
print (a[:])        #menampilkan semua huruf
print (len(a))      #jumlah keseluruhan huruf, tanda baca, spasi

# dua variable string
a = "Hello"
b = "World"
c = a+b
print(c)        #hasilnya dempet
c = a+" "+b     #menggunakan spasi
print(c)
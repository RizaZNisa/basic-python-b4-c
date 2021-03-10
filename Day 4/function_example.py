#1
nama_buah = []

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print("------")

def tambah(nama):
    nama_buah.append(nama)
    print_nama_buah()

tambah("jeruk")
tambah("apel")
tambah("melon")
tambah("pisang")

#2
#Create a program to calculate the area and circumference of a circle using the function

def luas(r):
    total = 22/7*r*r
    return total

print(luas(10))

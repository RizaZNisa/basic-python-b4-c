#That means we are able to ask the user for input as a STRING.

# cara 1
name = input("Masukkan nama kamu : ")
umur = input("Masukkan umur kamu : ")

#perlu spasi jika menggunakan + dan hanya untuk type data STRING
print("Nama saya adalah " + name + " sedangkan umur saya adalah " + umur + " tahun")   

# tidak perlu spasi jika menggunakan ,
#print("Nama saya adalah" ,name, "sedangkan umur saya adalah" ,umur, "tahun"))  

# cara 2
print("Nama : "+name)
print("Umur : "+umur)

# type data
print(type(name))
print(type(umur))

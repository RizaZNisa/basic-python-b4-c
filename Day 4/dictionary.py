#A dictionary is a collection which is unordered, changeable and indexed
#In Python dictionaries are written with curly brackets, and they have keys and values.

pelanggan = {
    "Nama" : "Awan",
    "Umur" : 18
}

pelanggan2 = {
    "Nama" : "Hendra",
    "Umur" : 20
}

#change value of dictionary
pelanggan ["Umur"] = 22

print("Nama: {}" . format(pelanggan["Nama"]))
print("Usia: {}" . format(pelanggan["Umur"]))
print("Nama: {}" . format(pelanggan2["Nama"]))
print("Usia: {}" . format(pelanggan2["Umur"])) 

# loop through dictionary

for x in pelanggan:
    print(x)
    print(pelanggan[x])
    print("-------")

for x in pelanggan2:
    print(x)
    print(pelanggan2[x])
    print("-------")

for x in pelanggan:
    print(x)
    print(pelanggan[x])
    print(pelanggan2[x])
    print("-------")

# list of dictionary
daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan2)

for pelanggan in daftar_pelanggan:
    print("Nama: {}" . format(pelanggan["Nama"]))
    print("Usia: {}" . format(pelanggan["Umur"]))
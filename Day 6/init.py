class person:
    # cunstructor
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

p1 = person("Riza",22)
p2 = person("Nisa",18)
print("Nama saya adalah "+p1.nama)
print("Umur saya adalah",p1.umur)
print("Nama saya adalah "+p2.nama)
print("Umur saya adalah",p2.umur)
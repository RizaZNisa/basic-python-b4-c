class person:
    # cunstructor
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    # method / function
    def sapa(self):
        print("hallo! Nama saya adalah "+self.nama)
        print("dan Umur saya",self.umur,"tahun")

p1 = person("Riza",22)
p2 = person("Nisa",18)
p1.sapa()
p2.sapa()
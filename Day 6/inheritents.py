class person: #superclass
    # cunstructor
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

class spesial_id(person): #subclass
    # cunstructor
    def __init__(self,nama,umur,alamat,status):
        self.alamat = alamat
        self.status = status
        # penurunan sifat/data
        person.__init__(self,nama,umur)
    def tampil(self):
        print(self.nama)
        print(self.umur)
        print(self.alamat)
        print(self.status)

p1 = spesial_id("Riza",27,"Bogor","Mahasiswa")
p1.tampil()
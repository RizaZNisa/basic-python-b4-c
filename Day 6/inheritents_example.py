class enemy:
    def __init__(self,nama):
        self.nama = nama

class gerakan(enemy):
    def __init__(self,nama,serangan,suara_hewan,damage):
        self.serangan = serangan
        self.suara_hewan = suara_hewan
        self.damage = damage

        enemy.__init__(self,nama)
    def serang(self):
        print(self.serangan)
    def suara(self):
        print(self.suara_hewan)
    def kesakitan(self):
        print(self.damage)

burung = gerakan("Falcon","Menukik","Eok..","Auch!!")
singa = gerakan("Lion","Mencakar","Gaooo..","Humm!!")
while True:
    print("1. serang")
    print("2. diam")
    print("3. panggil")
    pilih = int(input("Masukkan pilihan: "))
    print("============================")
    if pilih == 1 :
        print("1. Lion")
        print("2. Falcon")
        serang = int(input("Serang ke: "))
        print("============================")
        if serang == 1:
            singa.kesakitan()
        elif serang == 2:
            burung.kesakitan()
        print("============================")
    elif pilih == 2 :
        print(singa.serang())
        print(burung.serang())
        print("============================")
    elif pilih == 3 :
        print("1. Lion")
        print("2. Falcon")
        panggil = int(input("Serang ke: "))
        print("============================")
        if panggil == 1:
            singa.suara()
        elif panggil == 2:
            burung.suara()
        print("============================")

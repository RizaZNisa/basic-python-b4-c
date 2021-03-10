def luas(p,l,r):
    # luas kotak
    kota = p*l
    # luas lingkaran
    ling = 3.14*r*r
    return kota,ling

luas = luas(10,5,7)
tanya = int(input("pilih hitungan :"))
if tanya == 1 :
    print(luas[0])
elif tanya == 2 :
    print(luas[1])
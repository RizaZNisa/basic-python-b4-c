while True:
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Bersihkan Daftar Kontak")
    print("4. Keluar")
    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        read = open("file.txt","r")
        data = read.readlines()
        for i in range(0,len(data),2):
            print("Nama : {}Telp : {}".format(data[i],data[i+1]))
        read.close()
    elif pilihan == 2:
        create = open("file.txt","a")
        nama = input("Masukkan nama : ")
        telepon = input("Nomor telp    : ")
        create.write(nama+"\n")
        create.write(telepon+"\n")
        create.close()
    elif pilihan == 3:
        clear = open("file.txt","w")
        clear.close()  
        print("Data berhasil di refresh!")
    elif pilihan == 4:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia\n")
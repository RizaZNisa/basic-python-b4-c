# menghitung luas lingkaran
pi = 22/7
r = int(input("Jari-jari lingkaran : "))

#luas lingkaran = pi x r x r
print(("Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2").format(r, pi*r*r))
print(("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2").format(r, pi*r*r))
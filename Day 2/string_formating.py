age = 36.12345678
text = "Umur saya adalah {}".format (age) 
print(text)

#2f hanya 2 angka dibelakang koma
text = "Umur saya adalah {:.2f}".format (age) 
print(text)

age = 36
tinggi = 170.12344567
text = "Umur saya adalah {} dan tinggi saya adalah {:.2f}".format (age, tinggi) 
print(text)

p = 5
l = 2
print("luasnya adalah {}".format(p*l))
print(type(p))

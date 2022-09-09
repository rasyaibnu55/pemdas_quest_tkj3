#rumus volume balok
print("\.n1.volume balok")
panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai timggi: "))
volume_balok = panjang * lebar * tinggi

print("volume balok adalah",volume_balok)

#rumus volume kubus
print("\.n2.volume kubus")
sisi = int(input("masukan nilai sisi: "))
volume_kubus = sisi * sisi *sisi

print("volume kubus adalah",volume_kubus)

#rumus volume limas
print("\.n3.volume limas")
sisi_1 = ("masukan nilai sisi_1")
tinggi_1 = ("masukan nilai tinggi_1")
luas_1 = ("masukan nilai luas_1")
luas_1 = sisi_1 * sisi_1
volume_limas = luas_1 * tinggi_1

print ("volume limas adalah",volume_limas)

# rumus volume tabung
print("\.n4.volume tabung")
r = int(input("masukan nilai r: "))
tinggi_t = int(input("masukan nilai tinggi_t: "))
volume_tabung = 22/7 * r * r * tinggi_t

print ("volume tabung adalah",volume_tabung)

# celcius ke reamur
print ("\.n5.celcius ke reamur")
c = int(input("masukan nilai celcius: "))
reamur = 4/5 * c

print ("celcius ke reamur adalah",reamur)

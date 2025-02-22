# VİDEO-2
faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade) + 12)
# print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade = vade + 12

print("Seçtiğiniz vade sonucu yeni vade: " + str(vade))
print("Seçtiğiniz vade sonucu yeni vade: {vadeSayisi}".format(vadeSayisi = vade))
print(f"Seçtiğiniz vade sonucu yeni vade: {vade}")

isim =  "Salih"
# isim = input("İsminizi giriniz: ")
metin = "Merhaba, {name}".format(name = isim)
print(metin)
# metin = "Merhaba, {name}".format(name = Ahmet)

# f-string
metin = f"Hoşgeldiniz {1 + 1}"
print(metin)

dizi = ["İhtiyaç Kredisi",
        10,
        5.2,
        True
        ]
print(dizi)

krediler = ["İhtiyaç Kredisi",
          "Taşıt Kredisi",
          "Konut Kredisi"
          ]
print(type(krediler))

print(krediler[0])

print(len(krediler)) # length

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X kKredisi")
print(krediler)

krediler.pop(0) # Remove and return item at index (default last).
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi") # ilk bulduğunu siler
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for 
# i = 0 i < 10


for _ in range(10):
    print("xx")
    print(_)

print("***************")

for i in range(5, 10):
    print(i)

print("***************")

for i in range(0, 51, 10): # range(başlangıç, max, adım)
    print(i)               # integer olacak float olmaz

print("***************")

krediler = ["İhtiyaç Kredisi",
            "Taşıt Kredisi",
            "Konut Kredisi"
            ]

for kredi in krediler:
    print(kredi)

print("***************")

for i in range(len(krediler)):
   print(krediler[i])

# sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("***************")

while True:
    print("x")
    break
print("***************")

i = 0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i += 1

print("***** Son Döngü *****")
i = 0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

# fonksiyonlar

fiyat = 100
indirim = 20

def calculate():
    print(100 - 20)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba, {name}")


calculate()
calculateWithParams(100, 30)
sayHello("Salih")


def calculateAndReturn(price, discount):
    return price - discount

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat)
# VİDEO-1
# string --> metinsel ifade
baslik = "Tasit Kredisi"
print(baslik)

baslik = "Ihtiyaç kredisi"
print(baslik)


# int(integer) --> tamsayı
vade = 36 
ekVade = 6
vade2 = "36"

# float, decimal, double --> ondalıklı sayı
aylikOdeme = 200.5

# bool, boolean --> true veya false
yukselisteMi = False

# matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % --> mod operator
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


# mantıksal operatörler

print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and

print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


# karar yapıları 
# if-else
sayi1 = 100
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır

# indent --> bir 'tab' kadar boşluk bırakarak blok oluşturma
if sayi1 >= sayi2:
    print("sayi1 sayi2'den büyüktür.")
    print("hala if bloğunun içindeyim!")
elif sayi1 == sayi2:
    print("iki sayı eşittir.")
else:
    print("sayi1 sayi2'den küçüktür.")

# Her if elif else bloğundan bir cevap çıkar (>= ve == durumunda biri önce gelen çalışır)

print("burası if bloğunun dışıdır.")

print("*******************")

if sayi1 >= sayi2:
    print("sayi1 sayi2'den büyüktür.")
if sayi1 == sayi2:
    print("iki sayı eşittir.")
else:
    print("sayi1 sayi2'den küçüktür.")
# yeni if yeni blok oluşturur (burada hem >= yazdırır hem de ==)

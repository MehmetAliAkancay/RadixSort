import time

onlukListe="10lukliste.txt"
yuzlukListe="100lükliste.txt"
yuzbinlikListe="100000likliste.txt"

def DosyaOku(dosyaAdi):
    sayilar = []
    dosya=open(dosyaAdi,"r") 
    
    for i in dosya:
        sayilar.append(float(i)) 
    RadixSort(sayilar)      
                
def RadixSort(dizi):
    baslangicZamani=time.time()
    maksimum = max(dizi)
    basamak = 0.001
    while maksimum / basamak >= 1:
        CountingSort(dizi, basamak)
        basamak *= 10
    zaman=SureHesapla(baslangicZamani)
    KonsolaYazdir(dizi)
    print("Algoritmanın çalışma süresi:",zaman)
        
def CountingSort(dizi, basamak1):
    n = len(dizi)
    siralanmisDizi = [0] * (n)
    count = [0] * (10)
    
    for i in range(0, n):
        indis = int(dizi[i] / basamak1)
        count[indis % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        indis = int(dizi[i] / basamak1)
        siralanmisDizi[count[indis % 10] - 1] = dizi[i]
        count[indis % 10] -= 1
        i -= 1
    i = 0
    
    for i in range(0, len(dizi)):
        dizi[i] = siralanmisDizi[i]

def KonsolaYazdir(dizi):
        for i in range(len(dizi)):    #siralanan listenin ekrana yazildigi fonksiyon
            print(dizi[i],end="\n")
        
def SureHesapla(baslangic):        
    bitisZamani=time.time()
    return bitisZamani-baslangic

def MenuYazdir():
    print("1)Onluk Liste için 1'e basınız...")
    print("2)Yüzlük Liste için 2'ye basınız...")
    print("3)Yüzbinlik Liste için 3'e basınız...")
    print("4)Çıkış yapmak için 4'e basınız...")
       
while(1):
    MenuYazdir()
    secim=input("Seçiminizi giriniz.(1/2/3/4):")
    match secim:
        case '1':
            DosyaOku(onlukListe)
        case '2':
            DosyaOku(yuzlukListe)
        case '3':
            DosyaOku(yuzbinlikListe)
        case '4':
            exit()
        case _:
            print("Hatalı değer girdiniz.")
    giris=True
    while(giris):
        secim2=input("Devam etmek istiyor musunuz?(E/e/H/h):")
        match secim2:
            case 'E'|'e':
                giris=False
            case 'H'|'h':
                exit()
            case _:
                print("Hatalı değer girdiniz.Lütfen(E/e/H/h) harflerinden birini giriniz!!!")


"""
    @memrearal
"""

#Listeyi rastgele şekilde üretebilmek için random modülü dahil ediyoruz.
import random
#Kullanıcıdan boyutu alarak kaç birimlik liste oluşturacağımızı öğreniyoruz.
boyut = int(input("Kaclik Liste: "))

Liste = []
Ciftler = []
Tekler = []
Siralilar = []

#Liste boyutu kadar random modülünden 1-100 arasında rastgele sayı alıp listeye ekliyoruz.
for i in range(0,boyut):
    sayi = random.randint(1,100)
    Liste.append(sayi)

#Kontrol etmek için listeyi yazdırıyoruz.
print("Liste: {}".format(Liste))


"""
    Sıralı bir şekilde ilerleyen tek ve çift sayıları bulmak için iki farklı yol kullandım.
    İlk yolu tek sayılar üzerinde gösterdim, ikinci yolu ise çift sayılar üzerinde.
"""

# Sıralı tek sayıları bulan algoritma.
# Kolayca C diline çevirilebilir şekilde yazıldı.

TeklerKey = 0
TeklerEklenecekKey = 0
Tekler = [[] for i in range(0, len(Liste))]
TeklereEklenecek = []
for i in range(0, len(Liste)):
    if(Liste[TeklerKey] % 2 != 0):
        TeklereEklenecek.append(Liste[TeklerKey])
    else:
        Tekler[TeklerEklenecekKey] = TeklereEklenecek
        TeklereEklenecek = []
        TeklerEklenecekKey += 1
    TeklerKey += 1

# Sıralı çift sayıları bulan algoritma
# Python dilindeki enumerate, iter ve next fonksiyonlarından yararlanılarak yazıldı.
# 50.satırda bulunan not logical operatörünü kaldırarak tek sayılar bulunabilir.

for key, element  in enumerate(Liste):
    bir = iter(Liste[key:])
    iki = next(bir)
    lis = []
    while not iki % 2:
        lis.append(iki)
        try:
            iki = next(bir)
        except StopIteration:
            break
    if len(lis)>0:
        Ciftler.append(lis)

# Sıralı artan sayıları bulan algoritma.
# Tek sayılarda kullanılan basitleştirilmiş sistem kullanılarak yazıldı.
#

SiraliKey = 1
SiralilaraEklenecekKey = 0
Siralilar = [[] for i in range(0, len(Liste))]
SiralilaraEklenecek = []
for i in range(0, len(Liste)):
    if(len(Liste)>SiraliKey):
        if Liste[SiraliKey] > Liste[SiraliKey-1]:
            if(Liste[SiraliKey] not in SiralilaraEklenecek):
                SiralilaraEklenecek.append(Liste[SiraliKey])
            if(Liste[SiraliKey-1] not in SiralilaraEklenecek):
                SiralilaraEklenecek.append(Liste[SiraliKey-1])
        else:
            Siralilar[SiralilaraEklenecekKey] = SiralilaraEklenecek
            SiralilaraEklenecek = []
            SiralilaraEklenecekKey += 1
        SiraliKey += 1
    else:
        Siralilar[SiralilaraEklenecekKey] = SiralilaraEklenecek
        SiralilaraEklenecek = []

# En uzun siralilari bulan algoritma.

ciftindis = 0
ciftmax = 0
for key,element in enumerate(Ciftler):
    if len(element) > ciftmax:
        ciftmax = len(element)
        ciftindis = key
tekindis = 0
tekmax = 0
for key,element in enumerate(Tekler):
    if len(element) > tekmax:
        tekmax = len(element)
        tekindis = key
siraliindis = 0
siralimax = 0
for key,element in enumerate(Siralilar):
    if len(element) > siralimax:
        siralimax = len(element)
        siraliindis = key


print("En Uzun Sıralı Çiftler: {}".format(Ciftler[ciftindis]))
print("En Uzun Sıralı Tekler: {}".format(Tekler[tekindis]))
print("En Uzun Sıralı Liste: {}".format(sorted(Siralilar[siraliindis])))

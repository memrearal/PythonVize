# 2021 Bahar Dönemi Python Vizesi Problem Çözümleri

### Soru1 :

Kendisine veirlen liste içerisindeki en uzun çift sayı içeren, en uzun tek sayı içeren, en uzun artan sıralı haldeki serileri (birbiri ardınca yer alan) bulan ve bu serileri ekrana yazdıran Python kodunu yazınız.

Not: Liste, verilen boyut sayısına göre liste üreteci kullanılarak rastgele olarak oluşturulacaktır.

Örnek:

liste = [3, 5, 6, 2, 4, 10, 18, 13, 15, 1, 5, 7, 3, 4, 7, 8, 12, 2, 14, 4, 1, 19, 17, 5, 5, 8, 6, 4, 3, 7, 8, 9, 11, 15, 18, 12, 19, 21, 22]

Ekran Çıktısı:

En uzun tek sayı serisi: [13, 15, 1, 5, 7, 3]
En uzun çift sayı serisi: [6, 2, 4, 10, 18]
En uzun sıralı sayı serisi: [3, 7, 8, 9, 11, 15, 18]

### Soru2 :

Bir liste veri tipi içinde farklı veri tiplerinde (int, str, list, tuple, set ve dict) elemanlar bulunmaktadır. Bu listenin elemanlarına sahip oldukları veri tiplerine göre aşağıdaki işlemler gerçekleştirilecektir.

**int veri tipi** --> Sayının tüm basamaklarının eşit olup olmadığı kontrol edilecek, eşit ise True, eşit değil ise False yazdırılacaktır.

**str veri tipi** --> **Tüm str veri tipindeki elemanlar dikkate alınarak** karakterlerin frekans değerleri hesaplanacak ve tüm liste tamamlandıktan sonra ekrana yazdırılacaktır.

**tuple veri tipi** --> Elemanın palindrome (tersi kendine eşit) olup olmadığı kontrol edilecek, palindrome ise True, değilse False yazdırılacaktır. **Tersine çevirme işleminde hazır fonksiyon kesinlikle kullanılmayacaktır.**

**list veri tipi** --> Liste artan şekilde sıralanacaktır. Hem ilk hali hem de sıralı hali yazdırılacaktır. **Sıralama işleminde hazır fonksiyon kesinlikle kullanılmayacaktır.**

**set veri tipi** --> **Tüm set veri tipindeki elemanlar dikkate alınacak ve sadece tek bir kümeye ait olan elemanlar** tutulacaktır. Tüm liste tamamlandıktan sonra ekrana yazdırılacaktır.

**dict veri tipi** --> Herhangi bir işlem yapılmayacak, sadece veri tipi ve uyarı mesajı yazılacaktır.

Yuakarıda belirtilen işlemleri gerçekleştiren ve ekran çıktılarını uygun şekilde oluşturan Python kodunu yazınız.

Örnek:

liste = ["test", 22, (3, 3, 2 ,4), [4, 1, 7, 8, 3 ,10], {10, 9, 2}, "pass", {3, 4}, (8, 1, 4, 1, 8), "python", [1, 6, 8], 444, {1, 3, 4, 10}, 5554, {1:"bir", 2: "iki"}]

**Ekran Çıktısı:**
Num: 22, Type: Int, Equal: True
Tuple: (3, 3, 2, 4), Type: Tuple, Palindrome: False,
List: [4, 1, 7, 8, 3, 10], Type: List, Sorted_List: [1,3,4,7,8,10]
Tuple: (8, 1, 4, 1, 8), Type: Tuple, Palindrome: True,
List: [1, 6, 8], Type: List, Sorted_List: [1,6,8]
Num: 444, Type: Int, Equal: True
Num: 5554, Type: Int, Equal: False
Type: <class 'dict'>, Not Operated
Frequency: {'t':3, 'e': 1, 's': 3, 'p': 2, 'a': 1, 'y': 1, 'h': 1, 'o': 1, 'n': 1}
Unique Set: [9,2,1]

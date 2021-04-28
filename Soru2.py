"""
	@memrearal
"""

# İşlem yapılacak liste:
liste = ["test", 22, (3, 3, 2, 4), [4, 1, 7, 8, 3, 10], {10, 9, 2}, "pass", {3, 4}, (8, 1, 4, 1, 8), "python", [1, 6, 8], 444, {1, 3, 4, 10}, 5554, {1:"bir" , 2: "iki"}]

stringler = ""
setler = []


for element in liste:
	if type(element) == str:
		# Tüm stringleri birbiri ardına ekleyip frekanslarını en son bulacağız.
		stringler = stringler + element;
	if type(element) == int:
		# Sayının tüm basamaklarının aynı olup olmadığını kontrol eder, aynıysa durum True döner, değilse False.
		durum = True
		for i in range(0,len(str(element))):
			if i != 0:
				if str(element)[i-1] != str(element)[i]:
					durum = False
		print("Num: {}, Type: 'Int', Equal: {}".format(element, durum));
	if type(element) == tuple:
		# Tuple içerisinde verilen sayıları stringe dönüştürüyoruz.
		tup = ''.join(str(element))
		# Stringe dönüşmüş sayıların palindrom olup olmadığına bakıyoruz.
		palindrom = True
		for i in range(0, int(len(tup)/2)):
			if tup[i] != tup[len(tup)-i-1]:
				palindrom = False
		print("Tuple: {}, Type: Tuple, Palindrome: {}".format(element, palindrom))
	if type(element) == list:
		SirasizListe = element
		#Liste içerisindeki elementleri insertation sort yaparak sıralıyoruz.
		for i in range(1, len(element)):
			yapistir = element[i]
			y = i - 1
			while y >= 0 and element[y] > yapistir:
				element[y + 1] = element[y]
				y -= 1
			element[y + 1] = yapistir
		print("List: {}, Type: List, Sorted_List: {}".format(SirasizListe, element))
	if type(element) == set:
		# Setleri listeye dönüştürüyoruz.
		setler.append(list(element))
	if type(element) == dict:
		# Dictionary veri tipindeki elementler için uyarı mesajı yazdırıyoruz.
		print("Type <class 'dict'>, Not Operated")

# Stringlerin frekansını buluyoruz.
frekanslar = {}
for i in stringler:
	if i in frekanslar:
		frekanslar[i] += 1
	else:
		frekanslar[i] = 1

# Setlerin içindeki elementleri listeye eklemiştik.
# Nested list şeklindeki setler listesinde birden fazla listede bulunup bulunmadığını kontrol ediyoruz.
unikler = []
for Indis, ArananSet in enumerate(setler):
	kalanSetler = setler
	kalanSetler.pop(Indis)
	for element in ArananSet:
		if any(element in kalan for kalan in kalanSetler) == False:
			unikler.append(element)
print("Frequency: {}".format(frekanslar))
print("Unique Set: {}".format(unikler))

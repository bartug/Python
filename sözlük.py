
#sözlük = {]  type(sözlük) ==> class 'dict' çıktısını verir bize
# kelimeler = {"kitap":"book"} => burada aslında 1 öğre vardır

sözlük = {"kitap":"book",
	  "bilgisayar":"computer",
	  "programlama":"programming",
	  "dil":"language",
	  "defter":"notebook"}
#print(sözlük["kitap"]) # ile book çıktısını alırım
# adres defteri yapabilirim isim verince numara getirir gibi
# sözlük içinde sözlük yapabilirim kişiler ={ "..": {..:..}} gibi
# sözlük["bişey] = " diğer şey" ile ekleme yapabilirim

##şimdi fonksiyonlar yazıcam

def ara(sözcük):
	hata = "{} kelimesi sözlükte yok!"
	print(sözlük.get(sözcük,hata.format(sözcük)))

def ekle(sözcük,anlam):
	mesaj="{} kelimesi sözlüğe eklendi"
	sözlük[sözcük]=anlam
	print(mesaj.format(sözcük))

def sil(sözcük):
	try:
		sözcük.pop(sözcük)
	except KeyError as err:
		print(err,"kelimesi bulunamadı")
	else:
		print("{} kelimesi sözlükten silindi".format(sözcük))
print('0. çıkış')
print('1. Sözlükte kelime ara')
print('2. Sözlüğe kelime ekle')
print('3. Sözlükten kelime sil')

while True:
	no = input('Yapmak istediğiniz işlemin numarasını girin: ')
	
	if no == '0':
		break
	elif no == '1':
		sözcük = input('Aradığınız sözcük: ')
		ara(sözcük)
	elif no == '2':
		sözcük = input('Ekleyeceğiniz sözcük: ')
		anlam = input('Eklediğiniz sözcüğün anlamı: ')
		ekle(sözcük, anlam)
	elif no == '3':
		sözcük = input('Sileceğiniz sözcük: ')
		sil(sözcük)
	else:
		print('yanlıs islem')

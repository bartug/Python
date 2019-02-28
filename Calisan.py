class Çalışan():
	personel=[]

	def __init__(self,isim):
		self.isim = isim
		self.kabiliyetleri=[]
		self.personel_ekle()


	def personel_ekle(self):
		self.personel.append(self.isim)
		print('{} adlı kişi personele eklendi'.format(self.isim))
	
	@classmethod
	def personel_sayısını_görüntüle(cls):
		print(len(cls.personel))
	
	@classmethod
	def personeli_görüntüle(cls):
		print('Personel listesi:')
		for kişi in cls.personel:
			print(kişi)	
	
	def kabiliyet_ekle(self,kabiliyet):
		self.kabiliyetleri.append(kabiliyet)

	def kabiliyetleri_görüntüle(self):
		print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
		for kabiliyet in self.kabiliyetleri:
			print(kabiliyet)

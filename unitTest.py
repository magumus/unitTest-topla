import os
import unittest
import importlib.util
import tabulate

# Test edilecek klasörün yolu
KLASOR_YOLU = 'test/'

# Unit test sınıfı
class ToplaTest(unittest.TestCase):
    def test_topla(self):
        dogru_sonuclar = []
        yanlis_sonuclar = []

        for dosya in os.listdir(KLASOR_YOLU):
            if dosya.endswith('.py'):
                dosya_yolu = os.path.join(KLASOR_YOLU, dosya)
                spec = importlib.util.spec_from_file_location(dosya, dosya_yolu)
                modul = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modul)

                
                if not hasattr(modul, 'topla'):
                    yanlis_sonuclar.append((dosya, "Eksik İçerik"))
                    continue
                    

                # Sonuçları test et
                try:
                    if modul.topla(2, 3) == 5 and modul.topla(0, 0) == 0 and modul.topla(-2, 5) == 3:
                        dogru_sonuclar.append((dosya, "Doğru"))
                    else:
                        yanlis_sonuclar.append((dosya, "Yanlış"))
                except Exception as e:
                    yanlis_sonuclar.append((dosya, "Hata"))

        # Sonuçları tablo olarak göster
        tablo = [["Dosya", "Sonuç"]]
        tablo.extend(dogru_sonuclar)
        tablo.extend(yanlis_sonuclar)
        print(tabulate.tabulate(tablo, headers="firstrow"))

if __name__ == '__main__':
    unittest.main()
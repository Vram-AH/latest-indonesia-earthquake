import requests
from bs4 import BeautifulSoup

class LatestEarthquake:
    def __init__(self):
        self.description = 'To get the latest earthquake in indonesia from BMKG.go.id'
        self.result = None

    def ekstraksi_data(self):
        """
        Tanggal: 12 Mei 2022
        Waktu: 14:22:12 WIB
        Magnitudo: 5.2
        Kedalaman: 116 km
        Lokasi: LS=0.06, BT=123.48
        Pusat Gempa: Pusat gempa berada di laut 74 km Barat Daya Bolaanguki-BolSel
        Dirasakan: Dirasakan (Skala MMI): II-III Gorontalo, II - III Kab. Pulau Taliabu, II - III Luwuk
        :return:
        """
        try:
            content = requests.get('https://bmkg.go.id')
        except Exception:
            return None

        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser')

            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            tanggal = result[0]
            waktu = result[1]

            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')
            i = 0
            magnitudo = None
            kedalaman = None
            ls = None
            bt = None
            dirasakan = None

            for res in result:
                if i == 1:
                    magnitudo = res.text
                elif i == 2:
                    kedalaman = res.text
                elif i == 3:
                    koordinat = res.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif i == 4:
                    lokasi = res.text
                elif i == 5:
                    dirasakan = res.text
                i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls': ls, 'bt': bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan
            self.result = hasil
        else:
            return None



    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data gempa terkini")
            return

        print('Gempa Terakhir Berdasakan BMKG')
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo {self.result['magnitudo']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"Koordinat: LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"Lokasi {self.result['lokasi']}")
        print(f"Dirasakan {self.result['dirasakan']}")

    def run(self):
        self.ekstraksi_data()
        self.tampilkan_data()


if __name__ == '__main__':
    indonesian_earthquake = LatestEarthquake()
    print('Deskripsi package', indonesian_earthquake.description)
    indonesian_earthquake.run()
    #indonesian_earthquake.ekstraksi_data()
    #indonesian_earthquake.tampilkan_data()

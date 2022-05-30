import requests
from bs4 import BeautifulSoup

"""
Method = fungsi
Field / Atribute = variable
Constructor = method yang dipanggil pertama kali saat object diciptakan yang digunakan untuk mendeklarasikan semua field pada class ini
"""


class Disaster:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url

    def show_description(self):
        print(self.description)

    def scraping_data(self):
        print('scraping_data not yet implemented')

    def tampilkan_data(self):
        print('tampilkan_data not yet implemented')

    def run(self):
        self.scraping_data()
        self.tampilkan_data()


class LatestFlood(Disaster):
    def __init__(self, url):
        super(LatestFlood, self).__init__(url, '\nNOT YET IMPLEMENTED, but it should return last flood in Indonesia')


class LatestEarthquake(Disaster):
    def __init__(self, url):
        super(LatestEarthquake, self).__init__(url, 'To get the latest earthquake in indonesia from BMKG.go.id')

    def scraping_data(self):
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
            content = requests.get(self.url)
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


if __name__ == '__main__':
    indonesian_earthquake = LatestEarthquake('https://bmkg.go.id')
    indonesian_earthquake.show_description()
    indonesian_earthquake.run()

    indonesian_flood = LatestFlood('NOT YET')
    indonesian_flood.show_description()
    indonesian_flood.run()

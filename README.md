# latest-indonesia-earthquake
This package will gate the latest earthquake from BMKG | Meteorological, Climatological, and Geophysical Agency

## How it works?
This package will scrape from [BMKG](https://bmkg.go.id) to get the latest earthquake happened in indonesia

This package will use BeautifullSoup4 and Request, to produce output from JSON and ready to used in Web or Mobile applications

 ## How to use
'''
import gempaterkini

if __name__ == '__main__':
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
'''

# Author
Vram Adel Handrio
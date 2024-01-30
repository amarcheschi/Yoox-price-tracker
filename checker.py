import os
from pathlib import Path
import screenshot
import ocr

p = Path("items")
dirs = directories = [x for x in p.iterdir()]

for item in dirs:
    with open(item,"r+",encoding='UTF8') as file:
        url = file.readline().strip()
        saved_price = file.readline().strip()
        screenshot.check(url)
        price = ocr.extract_price("tmp")
        if(price != saved_price):
            print("il prezzo di "+url+" è cambiato dall'ultima rilevazione")
        else:
            print("il prezzo dell' articolo "+url+" non è cambiato")
os.remove("tmp.png")

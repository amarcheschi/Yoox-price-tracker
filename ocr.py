import easyocr
import re

def extract_price(file):
    reader = easyocr.Reader(['it','en'])
    result = reader.readtext(file+".png")
    pattern =  r"EUR [^,]+,\d{2}"

    risultati = re.search(pattern, str(result))
    if risultati:
        return(risultati[0])
    else:
        print(result)
        return("NULL")

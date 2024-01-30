import screenshot
import ocr
import os
import shutil

filename,url = screenshot.screen()
print("nome =",filename+"\nurl =",url)
print("adesso estraggo il prezzo")
price = ocr.extract_price(filename)
print(price)
if not os.path.exists("items"):
    os.makedirs("items")
item_filepath = os.path.join("items",filename+".json")
f = open(item_filepath,"w",encoding='UTF8')
f.write(url+"\n"+price)

#se si vuole mettere le immagini generate assieme ai json, il checker deve essere corretto controllando solo i file .json e non anche i .png
#destination_file_path = os.path.join("items", os.path.basename(filename+".png"))
#shutil.move(filename+".png", destination_file_path)

f.close()





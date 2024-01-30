from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

def screen():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    url = input("inserisci indirizzo dell'elemento di cui tracciare il prezzo: ")
    driver.get(url)
    index_it = url.find("/it/")
    if index_it != -1:
        index_start = index_it + len("/it/")
        index_item = url.find('item#')  
        if index_item != -1:
            extracted_part = url[index_start:index_item-1]
        else:
            extracted_part = url[index_start:]
    else:
        print("Pattern non trovato nell'URL")
    filename=extracted_part
    print("salvo l'immagine della pagina...")
    print("nome = "+filename)
    driver.save_screenshot(filename+".png")
    print("finito!")
    driver.quit()
    return filename,url

def check(url):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    print("scarico la pagina, attendere...")
    driver.get(url)
    driver.save_screenshot("tmp.png")
    driver.quit()
    return 0
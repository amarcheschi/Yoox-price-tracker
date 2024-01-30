# Yoox-price-tracker

i made it in a few hours so it might not be the most polished thing out there. A guy I know told me tot ry to scrape yoox prices, he told me it would have been hard since they try to obfuscate the html. So, anyway, i started blasting. I scrape the page, i take a screenshot in selenium, then extract the price of an item (it works only in italian yoox, you need to change the /it/ to /de/ or /fr/ or anything like that for other countries) with an ocr, it saves it to a file and you can check if it has changed with the checker.py

#More detailed instructions
python required
easyocr required
if something else needs to be installed, install it
use main to add new items of which you want to track the price
use checker to see if the price of any of them has changed
the json with the prices is saved in a folder "items" inside the folder where you run main.py
if you want to run checker.py at startup, you should win+r, type shell:startup and make a cmd script there to run /path/to/checker.py


import pyautogui as pag
from random import randint
import listinhas as lls

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
pes_img = pag.screenshot()

def url_deal():
    url_dealer = randint(1,5)
    if url_dealer ==1:
        print('Tente encontrar Instagran')
    if url_dealer ==2:
        print('Tente encontrar Facebook')
    if url_dealer ==3:     
        print('Tente encontrar Linkedin')
    if url_dealer ==4:  
        print('Tente encontrar Aliexpress')
    if url_dealer ==5:     
        print('Tente encontrar Orkut')
    
url_deal()


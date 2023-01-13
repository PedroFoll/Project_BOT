import webbrowser
import pyautogui as pag
from time import sleep
from helpers import *
import listinhas as lls


url = lls.url
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

print("Entrando na classe")
class Locate_logo():
        print("Dentro da classe")        
        locate= None
        def find_logo_google(locate=locate):
                import random
                print('dentro da função')
                while locate is None:                                              
                        try:
                                webbrowser.get('chrome').open_new_tab(random.choice(url))
                                sleep(5)
                                locate = pag.locateCenterOnScreen("images/.jpeg", confidence= 0.9)
                                if locate is not None:
                                        print('clickando')
                                        pag.click(locate)
                        except Exception as error:
                                print(error)
                        else:
                                if locate is not None:
                                        print('Salvando imagem')
                                        save_shot = pag.screenshot()
                                        save_shot.save('savedImage/print.jpeg')
                                        print('Bateu a foto')
                                        break
        find_logo_google()
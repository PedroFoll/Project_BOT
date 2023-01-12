import webbrowser
import pyautogui as pag
from time import sleep
from variables import *



url = 'google.com'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)

class Locate_logo():
        
        locate= ''
        def find_logo_google(locate = locate):
                c = 0
                while c < 5:
                        c+=1
                        c1 = str(c)
                        
                        sleep(5)
                        try:
                                locate = pag.locateCenterOnScreen("images/teste_google.jpeg", confidence= 0.9)
                                print(locate)
                                if locate is not None:
                                        print('clickando')
                                        pag.click(locate)
                        except Exception as error:
                                print(error)
                        else:
                                print('Salvando imagem')
                                save_shot = pag.screenshot()
                                save_shot.save('savedImage/print'+c1+'.jpeg')
                                print('Bateu a foto')
                                
        find_logo_google()
import webbrowser
import pyautogui as pag
from time import sleep
from variables import *



url = 'google.com'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)

class Locate_logo():
        c = 0
        locate= ''
        def find_logo_google():
                while c < 5:
                        c+=1
                        sleep(5)
                        try:
                                locate= pag.locateCenterOnScreen("images/teste_google.jpeg", confidence= 0.9)
                                print(locate)
                                if locate is not None:
                                        print('clickando')
                                        pag.click(locate)
                        except Exception as error:
                                print(error)
                        else:
                                print('saindo')
                                break
                
        find_logo_google()

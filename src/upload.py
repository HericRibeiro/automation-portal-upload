from selenium import webdriver
from config import config
import pyautogui
import logging
import pandas as pd
import time


def upload(navegador: webdriver.Edge):
    df_empresas = pd.read_excel(config['caminho_excel'], sheet_name='Operadoras', dtype=str)

    for i in range(len(df_empresas)):
        empresa = df_empresas.iat[i, 0]  
        logging.info(f"✅ Procurando pela empresa: {empresa}")

        xpath_pasta = f'//a[contains(text(), "{empresa}")]'
        try:
            navegador.find_element('xpath', config['xpath_menu']).click()
            time.sleep(2)

            elemento = navegador.find_element('xpath', xpath_pasta)
            elemento.click()
            print(f"✅ Pasta encontrada e acessada: {empresa}")
            time.sleep(2)

            navegador.find_element('xpath', config['xpath_pasta']).click()
            time.sleep(1)

            navegador.find_element('xpath', config['xpath_sub_pasta']).click()
            time.sleep(1)

            navegador.find_element('xpath', config['xpath_apagar_anterior']).click()
            time.sleep(1)

            pyautogui.press('ENTER')
            time.sleep(1)

            navegador.find_element('xpath', config['xpath_upload']).click()
            time.sleep(4)

            arquivo = empresa

            pyautogui.moveTo(x=750, y=90, duration=0.5)
            time.sleep(1.5)

            pyautogui.click()
            time.sleep(1.5)

            pyautogui.typewrite(config['caminho_excel'])
            time.sleep(1)

            pyautogui.press('ENTER')
            time.sleep(1)

            pyautogui.moveTo(x=330, y=715, duration=1)
            time.sleep(1.5)
            pyautogui.click()
            time.sleep(2)

            pyautogui.typewrite(arquivo)
            time.sleep(0.5)

            pyautogui.press('ENTER')
            time.sleep(6)

            navegador.find_element('xpath', config['xpath_rotulacao_arquivo']).click()
            time.sleep(2)

            navegador.find_element('xpath', config['xpath_formulario_confidencialidade']).click()
            time.sleep(1)

            navegador.find_element('xpath', config['xpath_confidencialidade']).click()
            time.sleep(1)

            navegador.find_element('xpath', config['xpath_opcao_confidencialidade']).click()
            navegador.find_element('xpath', config['xpath_rotular']).click()
            navegador.find_element('xpath', config['xpath_start_upload']).click()
            time.sleep(3)

            pyautogui.press('ENTER')
            time.sleep(3)

            print("✅ Feito:{}".format(empresa) )
            
        except Exception as e:
            logging.error(f"❌ Erro ao procurar pela prestadora '{empresa}': {e}")
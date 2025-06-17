from selenium import webdriver
from config import config
import logging
import time

def navegacao(navegador: webdriver.Edge):
    try:
        navegador.find_element('xpath', config['xpath_painel']).click()
        time.sleep(1)
        navegador.find_element('xpath', config['xpath_politicas']).click()
        time.sleep(1)
        navegador.find_element('xpath', config['xpath_menu']).click()
        time.sleep(1)
    except Exception as e:
        logging.error(f'❌ Falha na navegação: {e}')
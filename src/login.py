from selenium import webdriver
from config import config
import logging
import time

def login(navegador: webdriver.Edge):
    try:
        navegador.get(config['urlportal'])
        navegador.implicitly_wait(5)
        navegador.find_element('xpath', config['xpath_email']).send_keys(config['email'])
        time.sleep(1)
        navegador.find_element('xpath', config['xpath_enviar']).click()
        time.sleep(1)
        logging.info("✅ Login realizado com sucesso!")
    except Exception as e:
        logging.error(f"❌ Falha no login: {e}")
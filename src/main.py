from selenium import webdriver
from config import config
from logger import setup_logging
from login import login
from navegacao import navegacao
from renomear import renomear_arquivos
from upload import upload
import logging

def main():
    setup_logging()
    logging.info("✅ Iniciando automação!")
    navegador = webdriver.Edge()
    renomear_arquivos(config['caminho_arquivo'], config['caminho_excel'])
    login(navegador)
    navegacao(navegador)
    upload(navegador)
    navegador.quit()
    logging.info("✅ Navegador fechado")


if __name__ == "__main__":
    main()

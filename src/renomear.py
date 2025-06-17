from config import config
import pandas as pd
import logging
import os

def renomear_arquivos(diretorio, caminho_excel):
    try:
        logging.info("✅ Iniciando renomeação dos arquivos!")
        if not os.path.isdir(diretorio):
            raise FileNotFoundError(f"❌ O diretório especificado não foi encontrado: {diretorio}")

        if not os.path.isfile(caminho_excel):
            raise FileNotFoundError(f"❌ O arquivo Excel especificado não foi encontrado: {caminho_excel}")

        df = pd.read_excel(caminho_excel)

        if 'Nome Antigo' not in df.columns or 'Nome Novo' not in df.columns:
            raise ValueError("❌ O arquivo Excel deve conter as colunas 'Nome Antigo' e 'Nome Novo'.")

        for _, row in df.iterrows():
            nome_antigo = row['Nome Antigo']
            nome_novo = row['Nome Novo']
            
            if not nome_antigo.endswith('.csv'):
                nome_antigo += '.csv'
            if not nome_novo.endswith('.csv'):
                nome_novo += '.csv'

            caminho_antigo = os.path.join(diretorio, nome_antigo)
            caminho_novo = os.path.join(diretorio, nome_novo)

            if os.path.exists(caminho_antigo):
                os.rename(caminho_antigo, caminho_novo)
                logging.info(f"Renomeado: {nome_antigo} -> {nome_novo}")
            else:
                logging.warning(f"❌ Arquivo não encontrado: {nome_antigo}")

        logging.info("✅ Renomeação bem sucedida!")
    except Exception as e:
        logging.error(f"❌ Falha na renomeação dos arquivos: {e}")
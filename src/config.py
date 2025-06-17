import os
from dotenv import load_dotenv

load_dotenv()

config = {
    # Dados de acesso
    "email": os.getenv("mail"),

    # Caminhos de arquivos
    "caminho_excel": os.getenv("arquivo"),
    "caminho_arquivo": os.getenv("diretorioArquivo"),
    "caminho_driver": os.getenv("CAMINHO_DRIVER_NAVEGADOR"),
    "pasta_erros": os.getenv("PASTA_ERROS"),
    "pasta_logs": os.getenv("PASTA_LOGS"),
    # URL do portal
    "urlPortal": os.getenv("url"),

    # XPaths usados no Selenium
    "xpath_email": os.getenv("XPATH_EMAIL"),
    "xpath_enviar": os.getenv("XPATH_ENVIAR"),
    "xpath_painel": os.getenv("XPATH_PAINEL_CAMPANHAS_AIA"),
    "xpath_politicas": os.getenv("XPATH_POLITICAS"),
    "xpath_menu": os.getenv("XPATH_MENU"),
    "xpath_campanha": os.getenv("CAMPANHA"),
    "xpath_terminais_ativos": os.getenv("TERMINAIS_ATIVOS"),
    "xpath_apagar_anterior": os.getenv("APAGAR_ANTERIOR"),
    "xpath_upload": os.getenv("UPLOAD"),
    "xpath_rotulacao_arquivo": os.getenv("ROTULACAO"),
    "xpath_formulario_confidencialidade": os.getenv("FORMULARIO_CONFIDENCIALIDADE"),
    "xpath_confidencialidade": os.getenv("CONFIDENCIALIDADE"),
    "xpath_opcao_confidencialidade": os.getenv("OPCAO_FOR"),
    "xpath_rotular": os.getenv("ROTULAR"),
    "xpath_start_upload": os.getenv("START_UPLOAD"),
    "xpath_pasta": os.getenv("XPATH_PASTA"),
    "xpath_sub_pasta": os.getenv("XPATH_SUB_PASTA"),

    # Outros parâmetros
    "nomes": os.getenv("name"),
}


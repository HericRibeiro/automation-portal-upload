import logging
import os
from logging.handlers import RotatingFileHandler
from config import config

def setup_logging():
    if not os.path.exists(config["pasta_logs"]):
        os.makedirs(config["pasta_logs"])

    log_format = (
        "%(asctime)s - %(levelname)s - %(module)s - "
        "linha:%(lineno)d - %(message)s"
    )

    logging.basicConfig(
        level=logging.INFO,  
        format=log_format,
        handlers=[
            RotatingFileHandler(
                os.path.join(config["pasta_logs"], "automacao.log"),
                maxBytes=5 * 1024 * 1024,
                backupCount=10,
                encoding="utf-8",
            ),
            logging.StreamHandler()
        ],
    )

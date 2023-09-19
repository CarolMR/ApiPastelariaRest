from dotenv import load_dotenv, find_dotenv
import os
# Carrega o arquivo .env
dotenv_file = find_dotenv()

load_dotenv(dotenv_file)

# Configurações da APP
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")
from dotenv import load_dotenv
import os

load_dotenv()


HOST = os.getenv("HOST")
USER = os.getenv("USER_DB")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
PORT = int(os.getenv("PORT",5432))
HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")


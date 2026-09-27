from dotenv import load_dotenv
import os

load_dotenv()
PSQL_USER=os.getenv("PSQL_USER")
PSQL_PASSWORD=os.getenv("PSQL_PASSWORD")
PSQL_DB=os.getenv("PSQL_DATABASE")
PSQL_HOST=os.getenv("PSQL_HOST")
PSQL_PORT=os.getenv("PSQL_PORT")
SECRET=os.getenv("SECRET")
ALGORITHM=os.getenv("ALGORITHM")
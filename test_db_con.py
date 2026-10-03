import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()
psql_connection_string = URL.create(
    "postgresql+psycopg2",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=int(os.environ.get("DB_PORT", 5432)),
    database=os.environ["DB_NAME"],
)
engine=create_engine(psql_connection_string)
connection=engine.connect()
result=connection.execute(text("SELECT 1"))
print(result.fetchone())
connection.close()
print("connection successful")

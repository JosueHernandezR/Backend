import databases
import sqlalchemy
from functools import lru_cache
from app.core.config import settings
from db.table import metadata

@lru_cache()

def DATABASE_URL(
    connection: str = settings.DB_CONNECTION ,
    username: str   = settings.DB_USER,
    password: str   = settings.DB_PASSWORD,
    host: str       = settings.DB_HOST,
    port: str       = settings.DB_PORT,
    database: str   = settings.DB_NAME,
):
    return str(connection+"://"+username+":"+password+"@"+host+":"+port+"/"+database)

database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Postgres:
    user     = os.getenv("POSTGRES_USER","Urahume")
    password = os.getenv("POSTGRES_PASSWORD","PahChin")
    host     = os.getenv("POSTGRES_HOST", "Hanagaki")
    port     = os.getenv("POSTGRES_PORT", 420)
    database = os.getenv("POSTGRES_DB", "Deku")
    
    @property
    def url(self):
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

engine = create_engine(Postgres().url, connect_args={})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

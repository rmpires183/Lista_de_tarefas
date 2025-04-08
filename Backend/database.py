from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declatative_base
from sqlalchemy.orm import sessionmaker

#Conexão com PostgresSQL
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:ssenha@localhost/lista_de_tarefas"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declatative_base()
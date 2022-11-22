# 디비 엔진 생성
from sqlalchemy import create_engine

# 선언
from sqlalchemy.ext.declarative import declarative_base

# session orm
from sqlalchemy.orm import sessionmaker

# os
import os

# json
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets = json.loads(open(SECRET_FILE).read())

DB = secrets['DB']

USER = DB['user']
PASSWORD = DB['password']
HOST = DB['host']
PORT = DB['port']
DATABASE = DB['database']

DB_URL = f"mysql+pymysql://{USER}:{PASSWORD}:{HOST}:{PORT}/{DATABASE}?charset=utf8" 

engine = create_engine(DB_URL, echo=True, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
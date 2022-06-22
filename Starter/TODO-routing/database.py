from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_ALCHEMY_DATABSE_URL = "postgresql://postgres:muhammad@localhost:5432/COCHARGE"

engine = create_engine(
    SQL_ALCHEMY_DATABSE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

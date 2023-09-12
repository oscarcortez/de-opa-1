from DB.url_factory import UrlFactory
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .url_factory import UrlFactory

uf = UrlFactory('postgres')
engine = create_engine(uf.get_url())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
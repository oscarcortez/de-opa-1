from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import yaml

api = FastAPI(
    title="Kryptobot",
    description="My own API powered by FastAPI",
    version="1.0.6")


@api.get("/content")
async def show_content():
    url = "postgresql://postgres:123456@db/opa_binance"

    engine = create_engine(
        url,
        pool_pre_ping=True,
    )
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    try:
        with open('config/local_settings.yaml', "r") as file:
            _ = yaml.safe_load(file)
        db = SessionLocal()
        return db.execute(text("SELECT * FROM streaming_data")).scalar()
    except Exception as e:
        raise e

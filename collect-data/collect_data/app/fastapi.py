from fastapi import FastAPI
from sqlalchemy import create_engine




api = FastAPI(
    title="Kryptobot",
    description="My own API powered by FastAPI.",
    version="1.0.6")

url = "postgresql://postgres:123456@localhost:5432/opa_binance"

engine = create_engine(url)
connection = engine.connect()



@api.get("/content")
async def show_content():
    connection.execute("SELECT * FROM streaming_data")
    users = connection.fetchall()
    return {"users": users}

connection.close()

# @api.get("/")
# async def root():
#  return {"greeting":"Hello world"}








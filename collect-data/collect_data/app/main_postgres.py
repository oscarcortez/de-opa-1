from fastapi import FastAPI

api = FastAPI(
    title="Kryptobot",
    description="My own API powered by FastAPI.",
    version="1.0.6")


@api.get('/')

def get_index():
    return {'data': 'hello world'}
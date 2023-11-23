from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ..routers.streaming_data import router as StreamingRouter

app = FastAPI()
app.title = "Kryptobot"
app.description = "Kriptobot API"
app.version = "1.0.0"

app.include_router(StreamingRouter)


@app.get('/', tags=['home'])
def default():
    return HTMLResponse(content='<h1>API is running</h1>', status_code=200)

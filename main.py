from fastapi import FastAPI
import uvicorn
from core.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.server_port, reload=True)

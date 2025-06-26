# main.py

from fastapi import FastAPI
from src.routes import router  # Absolute import

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8420, reload=True)
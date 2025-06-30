from fastapi import FastAPI
import uvicorn
from core.config import settings
from api.v1 import task, auth, task_list
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(task.router)
app.include_router(task_list.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.server_port, reload=True)

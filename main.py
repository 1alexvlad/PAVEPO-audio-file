from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from files.router import router_file
from auth.router import router as router_user

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_user)
app.include_router(router_file)
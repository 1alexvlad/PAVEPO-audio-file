from fastapi import FastAPI
from files.router import router_file

app = FastAPI()

app.include_router(router_file)

from fastapi import FastAPI

from {{cookiecutter.project_slug}}.server.dev_routes import router as dev_router

app: FastAPI = FastAPI()

app.include_router(dev_router, prefix="/dev")


@app.get("/")
async def root():
    return {"message": "Hello World"}

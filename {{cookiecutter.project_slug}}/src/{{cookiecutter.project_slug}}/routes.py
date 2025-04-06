from fastapi import FastAPI
from starlette.responses import JSONResponse


def add_routes(app: FastAPI):
    @app.get("/health")
    def health():
        return JSONResponse({"status": "ok"})

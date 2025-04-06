import logging

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_exception_handlers(app: FastAPI):
    pass

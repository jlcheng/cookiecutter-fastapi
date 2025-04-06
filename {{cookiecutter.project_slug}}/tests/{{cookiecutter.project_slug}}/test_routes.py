from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from {{cookiecutter.project_slug}}.main_app import app as _app

pytestmark = pytest.mark.anyio


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def app() -> FastAPI:
    return _app


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Provides an AsyncClient configured for the test app."""
    base_url = "https://example.com"
    async with AsyncClient(transport=ASGITransport(app=app), base_url=base_url) as client:
        yield client


class TestRoutes:
    async def test_health(self, async_client: AsyncClient):
        response = await async_client.get("/health")

        assert response.status_code == 200

from __future__ import annotations

import os
from collections.abc import AsyncGenerator

import pytest
from dotenv import load_dotenv
from stitchdb.storage import AsyncStorageClient


def pytest_configure(config) -> None:
    load_dotenv(dotenv_path="tests/tests.env")


@pytest.fixture
async def storage() -> AsyncGenerator[AsyncStorageClient]:
    url = os.environ.get("STITCHDB_TEST_URL")
    assert url is not None, "Must provide STITCHDB_TEST_URL environment variable"
    key = os.environ.get("STITCHDB_TEST_KEY")
    assert key is not None, "Must provide STITCHDB_TEST_KEY environment variable"
    async with AsyncStorageClient(
        url,
        {
            "apiKey": key,
            "Authorization": f"Bearer {key}",
        },
    ) as client:
        client.session.timeout = None
        yield client

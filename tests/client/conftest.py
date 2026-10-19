from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

from stitchdb import Client, create_client


def pytest_configure(config) -> None:
    load_dotenv(dotenv_path="tests/tests.env")


@pytest.fixture(scope="session")
def stitchdb() -> Client:
    url = os.environ.get("STITCHDB_TEST_URL")
    assert url is not None, "Must provide STITCHDB_TEST_URL environment variable"
    key = os.environ.get("STITCHDB_TEST_KEY")
    assert key is not None, "Must provide STITCHDB_TEST_KEY environment variable"
    return create_client(url, key)

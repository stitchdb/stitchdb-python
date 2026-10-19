from __future__ import annotations

from typing import Literal, Union, overload

from stitchdb.storage._async import AsyncStorageClient
from stitchdb.storage._async.bucket import AsyncStorageBucketAPI
from stitchdb.storage._async.file_api import AsyncBucket
from stitchdb.storage._sync import SyncStorageClient
from stitchdb.storage._sync.bucket import SyncStorageBucketAPI
from stitchdb.storage._sync.file_api import SyncBucket
from stitchdb.storage.constants import DEFAULT_TIMEOUT
from stitchdb.storage.version import __version__

__all__ = [
    "create_client",
    "__version__",
    "AsyncStorageClient",
    "AsyncBucket",
    "AsyncStorageBucketAPI",
    "SyncStorageClient",
    "SyncBucket",
    "SyncStorageBucketAPI",
]


@overload
def create_client(
    url: str, headers: dict[str, str], *, is_async: Literal[True]
) -> AsyncStorageClient: ...


@overload
def create_client(
    url: str, headers: dict[str, str], *, is_async: Literal[False]
) -> SyncStorageClient: ...


def create_client(
    url: str, headers: dict[str, str], *, is_async: bool, timeout: int = DEFAULT_TIMEOUT
) -> Union[AsyncStorageClient, SyncStorageClient]:
    if is_async:
        return AsyncStorageClient(url, headers, timeout)
    else:
        return SyncStorageClient(url, headers, timeout)

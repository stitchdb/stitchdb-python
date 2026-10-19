from stitchdb.postgrest import APIError as PostgrestAPIError
from stitchdb.postgrest import APIResponse as PostgrestAPIResponse
from stitchdb.realtime import AuthorizationError, NotConnectedError
from stitchdb.storage.utils import StorageException
from stitchdb.auth.errors import (
    AuthApiError,
    AuthError,
    AuthImplicitGrantRedirectError,
    AuthInvalidCredentialsError,
    AuthRetryableError,
    AuthSessionMissingError,
    AuthUnknownError,
    AuthWeakPasswordError,
)
from stitchdb.functions.errors import (
    FunctionsError,
    FunctionsHttpError,
    FunctionsRelayError,
)

# Async Client
from ._async.auth_client import AsyncStitchAuthClient
from ._async.client import AsyncClient
from ._async.client import AsyncStorageClient as AsyncStitchStorageClient
from ._async.client import create_client as acreate_client
from ._async.client import create_client as create_async_client

# Sync Client
from ._sync.auth_client import SyncStitchAuthClient as StitchAuthClient
from ._sync.client import Client, create_client
from ._sync.client import SyncStorageClient as StitchStorageClient

# Lib
from .lib.client_options import AsyncClientOptions
from .lib.client_options import AsyncClientOptions as AClientOptions
from .lib.client_options import SyncClientOptions as ClientOptions

# Version
from .version import __version__

__all__ = [
    "AsyncStitchAuthClient",
    "acreate_client",
    "create_async_client",
    "AClientOptions",
    "AsyncClient",
    "AsyncClientOptions",
    "AsyncStitchStorageClient",
    "StitchAuthClient",
    "create_client",
    "Client",
    "ClientOptions",
    "StitchStorageClient",
    "PostgrestAPIError",
    "PostgrestAPIResponse",
    "StorageException",
    "__version__",
    "AuthApiError",
    "AuthError",
    "AuthImplicitGrantRedirectError",
    "AuthInvalidCredentialsError",
    "AuthRetryableError",
    "AuthSessionMissingError",
    "AuthWeakPasswordError",
    "AuthUnknownError",
    "FunctionsHttpError",
    "FunctionsRelayError",
    "FunctionsError",
    "AuthorizationError",
    "NotConnectedError",
]

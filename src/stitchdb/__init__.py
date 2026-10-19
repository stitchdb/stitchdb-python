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
from ._async.auth_client import AsyncStitchAuthClient as AStitchAuthClient
from ._async.client import AsyncClient
from ._async.client import AsyncClient as AClient
from ._async.client import AsyncStorageClient as AStitchStorageClient
from ._async.client import StitchException as AStitchException
from ._async.client import StitchException as AsyncStitchException
from ._async.client import create_client as acreate_client
from ._async.client import create_client as create_async_client

# Sync Client
from ._sync.auth_client import SyncStitchAuthClient as StitchAuthClient
from ._sync.client import Client, StitchException, create_client
from ._sync.client import StitchException as SyncStitchException
from ._sync.client import SyncStorageClient as StitchStorageClient

# Lib
from .lib.client_options import AsyncClientOptions
from .lib.client_options import AsyncClientOptions as AClientOptions
from .lib.client_options import SyncClientOptions as ClientOptions

# Version
from .version import __version__

__all__ = (
    "acreate_client",
    "create_async_client",
    "AClient",
    "AStitchAuthClient",
    "AStitchStorageClient",
    "AClientOptions",
    "AsyncClient",
    "AsyncClientOptions",
    "create_client",
    "Client",
    "StitchAuthClient",
    "StitchStorageClient",
    "ClientOptions",
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
    "StitchException",
    "AStitchException",
    "AsyncStitchException",
    "SyncStitchException",
)

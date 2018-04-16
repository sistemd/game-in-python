from typing import Any
from . import exceptions
from .packages import ssl_match_hostname
from . import packages
from .connection import (
    HTTPException as HTTPException,
    BaseSSLError as BaseSSLError,
    ConnectionError as ConnectionError,
)
from . import request
from . import response
from . import connection
from .util import connection as _connection
from .util import retry
from .util import timeout
from .util import url

ClosedPoolError = exceptions.ClosedPoolError
ProtocolError = exceptions.ProtocolError
EmptyPoolError = exceptions.EmptyPoolError
HostChangedError = exceptions.HostChangedError
LocationValueError = exceptions.LocationValueError
MaxRetryError = exceptions.MaxRetryError
ProxyError = exceptions.ProxyError
ReadTimeoutError = exceptions.ReadTimeoutError
SSLError = exceptions.SSLError
TimeoutError = exceptions.TimeoutError
InsecureRequestWarning = exceptions.InsecureRequestWarning
CertificateError = ssl_match_hostname.CertificateError
port_by_scheme = connection.port_by_scheme
DummyConnection = connection.DummyConnection
HTTPConnection = connection.HTTPConnection
HTTPSConnection = connection.HTTPSConnection
VerifiedHTTPSConnection = connection.VerifiedHTTPSConnection
RequestMethods = request.RequestMethods
HTTPResponse = response.HTTPResponse
is_connection_dropped = _connection.is_connection_dropped
Retry = retry.Retry
Timeout = timeout.Timeout
get_host = url.get_host

xrange = ...  # type: Any
log = ...  # type: Any

class ConnectionPool:
    scheme = ...  # type: Any
    QueueCls = ...  # type: Any
    host = ...  # type: Any
    port = ...  # type: Any
    def __init__(self, host, port=...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    def close(self): ...

class HTTPConnectionPool(ConnectionPool, RequestMethods):
    scheme = ...  # type: Any
    ConnectionCls = ...  # type: Any
    strict = ...  # type: Any
    timeout = ...  # type: Any
    retries = ...  # type: Any
    pool = ...  # type: Any
    block = ...  # type: Any
    proxy = ...  # type: Any
    proxy_headers = ...  # type: Any
    num_connections = ...  # type: Any
    num_requests = ...  # type: Any
    conn_kw = ...  # type: Any
    def __init__(self, host, port=..., strict=..., timeout=..., maxsize=..., block=..., headers=..., retries=..., _proxy=..., _proxy_headers=..., **conn_kw) -> None: ...
    def close(self): ...
    def is_same_host(self, url): ...
    def urlopen(self, method, url, body=..., headers=..., retries=..., redirect=..., assert_same_host=..., timeout=..., pool_timeout=..., release_conn=..., **response_kw): ...

class HTTPSConnectionPool(HTTPConnectionPool):
    scheme = ...  # type: Any
    ConnectionCls = ...  # type: Any
    key_file = ...  # type: Any
    cert_file = ...  # type: Any
    cert_reqs = ...  # type: Any
    ca_certs = ...  # type: Any
    ssl_version = ...  # type: Any
    assert_hostname = ...  # type: Any
    assert_fingerprint = ...  # type: Any
    def __init__(self, host, port=..., strict=..., timeout=..., maxsize=..., block=..., headers=..., retries=..., _proxy=..., _proxy_headers=..., key_file=..., cert_file=..., cert_reqs=..., ca_certs=..., ssl_version=..., assert_hostname=..., assert_fingerprint=..., **conn_kw) -> None: ...

def connection_from_url(url, **kw): ...

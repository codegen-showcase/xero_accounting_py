import httpx
import typing

from make_api_request import AsyncBaseClient, AuthBearer, SyncBaseClient
from xero_accounting_py.environment import (
    DEFAULT,
    Environment,
    ServerGroup,
    _get_base_url,
)
from xero_accounting_py.resources.accounting import (
    AccountingClient,
    AsyncAccountingClient,
)
from xero_accounting_py.resources.projects import AsyncProjectsClient, ProjectsClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: ServerGroup = DEFAULT,
        oauth_token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url={
                "accounting": _get_base_url(
                    environment, "accounting", Environment.ACCOUNTING.value
                ),
                "projects": _get_base_url(
                    environment, "projects", Environment.PROJECTS.value
                ),
            },
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
            auths={"OAuth2": AuthBearer(token=oauth_token)},
        )
        self.accounting = AccountingClient(base_client=self._base_client)
        self.projects = ProjectsClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: ServerGroup = DEFAULT,
        oauth_token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url={
                "accounting": _get_base_url(
                    environment, "accounting", Environment.ACCOUNTING.value
                ),
                "projects": _get_base_url(
                    environment, "projects", Environment.PROJECTS.value
                ),
            },
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
            auths={"OAuth2": AuthBearer(token=oauth_token)},
        )
        self.accounting = AsyncAccountingClient(base_client=self._base_client)
        self.projects = AsyncProjectsClient(base_client=self._base_client)

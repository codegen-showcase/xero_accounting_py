from make_api_request import AsyncBaseClient, SyncBaseClient
from xero_accounting_py.resources.projects.projects1 import (
    AsyncProjects1Client,
    Projects1Client,
)
from xero_accounting_py.resources.projects.projects_users import (
    AsyncProjectsUsersClient,
    ProjectsUsersClient,
)


class ProjectsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.projects1 = Projects1Client(base_client=self._base_client)
        self.projects_users = ProjectsUsersClient(base_client=self._base_client)


class AsyncProjectsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.projects1 = AsyncProjects1Client(base_client=self._base_client)
        self.projects_users = AsyncProjectsUsersClient(base_client=self._base_client)

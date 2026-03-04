# projects.projects_users

## Module Functions

### Retrieves a list of all project users <a name="list"></a>

Allows you to retrieve the users on a projects.

**API Endpoint**: `GET /ProjectsUsers`

#### Parameters

| Parameter        | Required | Description                                                                                                                            | Example    |
| ---------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                                             | `"string"` |
| `page`           |    ✗     | set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.                             | `1`        |
| `page_size`      |    ✗     | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | `100`      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.projects_users.list(
    xero_tenant_id="string", page=1, page_size=100
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.projects_users.list(
    xero_tenant_id="string", page=1, page_size=100
)
```

#### Response

##### Type

[ProjectUsers](/xero_accounting_py/types/models/project_users.py)

##### Example

```python
{}
```

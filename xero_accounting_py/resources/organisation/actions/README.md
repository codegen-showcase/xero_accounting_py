# organisation.actions

## Module Functions

### Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation. <a name="list"></a>

**API Endpoint**: `GET /Organisation/Actions`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.organisation.actions.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.organisation.actions.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Response

##### Type

[Actions](/xero_accounting_py/types/models/actions.py)

##### Example

```python
{}
```

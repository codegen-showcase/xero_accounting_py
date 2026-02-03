# organisation

## Module Functions

### Retrieves Xero organisation details <a name="list"></a>

**API Endpoint**: `GET /Organisation`

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
res = client.organisation.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
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
res = await client.organisation.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Response

##### Type

[Organisations](/xero_accounting_py/types/models/organisations.py)

##### Example

```python
{}
```

## Submodules

- [actions](actions/README.md) - actions
- [cis_settings](cis_settings/README.md) - cis_settings

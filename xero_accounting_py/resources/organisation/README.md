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

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.organisation.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
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

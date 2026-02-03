# currencies

## Module Functions

### Retrieves currencies for your Xero organisation <a name="list"></a>

**API Endpoint**: `GET /Currencies`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element    | `"Code ASC"`            |
| `where`          |    ✗     | Filter by an any element   | `"Code==\"USD\""`       |

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
res = client.currencies.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Code ASC", where='Code=="USD"'
)
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
res = await client.currencies.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Code ASC", where='Code=="USD"'
)
```

#### Response

##### Type

[Currencies](/xero_accounting_py/types/models/currencies.py)

##### Example

```python
{}
```

### Create a new currency for a Xero organisation <a name="create"></a>

**API Endpoint**: `PUT /Currencies`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `code`           |    ✗     |                            | `"AED"`                 |
| `description`    |    ✗     | Name of Currency           | `"string"`              |

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
res = client.currencies.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", code="USD", description="United States Dollar"
)
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
res = await client.currencies.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", code="USD", description="United States Dollar"
)
```

#### Response

##### Type

[Currencies](/xero_accounting_py/types/models/currencies.py)

##### Example

```python
{}
```

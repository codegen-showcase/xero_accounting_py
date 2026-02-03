# contacts.history

## Module Functions

### Retrieves history records for a specific contact <a name="list"></a>

**API Endpoint**: `GET /Contacts/{ContactID}/History`

#### Parameters

| Parameter        | Required | Description                     | Example                                  |
| ---------------- | :------: | ------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant      | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.contacts.history.list(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
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
res = await client.contacts.history.list(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[HistoryRecords](/xero_accounting_py/types/models/history_records.py)

##### Example

```python
{}
```

### Creates a new history record for a specific contact <a name="create"></a>

**API Endpoint**: `PUT /Contacts/{ContactID}/History`

#### Parameters

| Parameter         | Required | Description                     | Example                                   |
| ----------------- | :------: | ------------------------------- | ----------------------------------------- |
| `contact_id`      |    ✓     | Unique identifier for a Contact | `"00000000-0000-0000-0000-000000000000"`  |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant      | `"YOUR_XERO_TENANT_ID"`                   |
| `history_records` |    ✗     |                                 | `[{"date_utc": "/Date(1573755038314)/"}]` |

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
res = client.contacts.history.create(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    history_records=[{"details": "Hello World"}],
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
res = await client.contacts.history.create(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    history_records=[{"details": "Hello World"}],
)
```

#### Response

##### Type

[HistoryRecords](/xero_accounting_py/types/models/history_records.py)

##### Example

```python
{}
```

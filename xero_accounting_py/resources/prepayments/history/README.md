# prepayments.history

## Module Functions

### Retrieves history record for a specific prepayment <a name="list"></a>

**API Endpoint**: `GET /Prepayments/{PrepaymentID}/History`

#### Parameters

| Parameter        | Required | Description                        | Example                                  |
| ---------------- | :------: | ---------------------------------- | ---------------------------------------- |
| `prepayment_id`  |    ✓     | Unique identifier for a PrePayment | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant         | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.prepayments.history.list(
    prepayment_id="00000000-0000-0000-0000-000000000000",
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
res = await client.prepayments.history.list(
    prepayment_id="00000000-0000-0000-0000-000000000000",
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

### Creates a history record for a specific prepayment <a name="create_record"></a>

**API Endpoint**: `PUT /Prepayments/{PrepaymentID}/History`

#### Parameters

| Parameter         | Required | Description                        | Example                                   |
| ----------------- | :------: | ---------------------------------- | ----------------------------------------- |
| `prepayment_id`   |    ✓     | Unique identifier for a PrePayment | `"00000000-0000-0000-0000-000000000000"`  |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant         | `"YOUR_XERO_TENANT_ID"`                   |
| `history_records` |    ✗     |                                    | `[{"date_utc": "/Date(1573755038314)/"}]` |

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
res = client.prepayments.history.create_record(
    prepayment_id="00000000-0000-0000-0000-000000000000",
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
res = await client.prepayments.history.create_record(
    prepayment_id="00000000-0000-0000-0000-000000000000",
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

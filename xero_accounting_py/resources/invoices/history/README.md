# invoices.history

## Module Functions

### Retrieves history records for a specific invoice <a name="list"></a>

**API Endpoint**: `GET /Invoices/{InvoiceID}/History`

#### Parameters

| Parameter        | Required | Description                      | Example                                  |
| ---------------- | :------: | -------------------------------- | ---------------------------------------- |
| `invoice_id`     |    ✓     | Unique identifier for an Invoice | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant       | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.invoices.history.list(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.invoices.history.list(
    invoice_id="00000000-0000-0000-0000-000000000000",
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

### Creates a history record for a specific invoice <a name="create_record"></a>

**API Endpoint**: `PUT /Invoices/{InvoiceID}/History`

#### Parameters

| Parameter         | Required | Description                      | Example                                   |
| ----------------- | :------: | -------------------------------- | ----------------------------------------- |
| `invoice_id`      |    ✓     | Unique identifier for an Invoice | `"00000000-0000-0000-0000-000000000000"`  |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant       | `"YOUR_XERO_TENANT_ID"`                   |
| `history_records` |    ✗     |                                  | `[{"date_utc": "/Date(1573755038314)/"}]` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.invoices.history.create_record(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    history_records=[{"details": "Hello World"}],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.invoices.history.create_record(
    invoice_id="00000000-0000-0000-0000-000000000000",
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

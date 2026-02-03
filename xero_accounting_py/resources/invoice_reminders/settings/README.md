# invoice_reminders.settings

## Module Functions

### Retrieves invoice reminder settings <a name="list"></a>

**API Endpoint**: `GET /InvoiceReminders/Settings`

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
res = client.invoice_reminders.settings.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
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
res = await client.invoice_reminders.settings.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Response

##### Type

[InvoiceReminders](/xero_accounting_py/types/models/invoice_reminders.py)

##### Example

```python
{}
```

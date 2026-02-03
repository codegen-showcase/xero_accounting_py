# invoices.email

## Module Functions

### Sends a copy of a specific invoice to related contact via email <a name="send"></a>

**API Endpoint**: `POST /Invoices/{InvoiceID}/Email`

#### Parameters

| Parameter        | Required | Description                                             | Example                                  |
| ---------------- | :------: | ------------------------------------------------------- | ---------------------------------------- |
| `invoice_id`     |    ✓     | Unique identifier for an Invoice                        | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                              | `"YOUR_XERO_TENANT_ID"`                  |
| `status`         |    ✗     | Need at least one field to create an empty JSON payload | `"string"`                               |

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
res = client.invoices.email.send(
    invoice_id="00000000-0000-0000-0000-000000000000",
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
res = await client.invoices.email.send(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

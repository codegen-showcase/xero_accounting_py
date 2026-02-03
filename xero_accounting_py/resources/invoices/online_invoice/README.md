# invoices.online_invoice

## Module Functions

### Retrieves a URL to an online invoice <a name="get"></a>

**API Endpoint**: `GET /Invoices/{InvoiceID}/OnlineInvoice`

#### Parameters

| Parameter        | Required | Description                      | Example                                  |
| ---------------- | :------: | -------------------------------- | ---------------------------------------- |
| `invoice_id`     |    ✓     | Unique identifier for an Invoice | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant       | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.invoices.online_invoice.get(
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
res = await client.invoices.online_invoice.get(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[OnlineInvoices](/xero_accounting_py/types/models/online_invoices.py)

##### Example

```python
{}
```

# repeating_invoices.attachments

## Module Functions

### Retrieves attachments from a specific repeating invoice <a name="list"></a>

**API Endpoint**: `GET /RepeatingInvoices/{RepeatingInvoiceID}/Attachments`

#### Parameters

| Parameter              | Required | Description                               | Example                                  |
| ---------------------- | :------: | ----------------------------------------- | ---------------------------------------- |
| `repeating_invoice_id` |    ✓     | Unique identifier for a Repeating Invoice | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`       |    ✓     | Xero identifier for Tenant                | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.repeating_invoices.attachments.list(
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.repeating_invoices.attachments.list(
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Attachments](/xero_accounting_py/types/models/attachments.py)

##### Example

```python
{}
```

### Retrieves a specific attachment from a specific repeating invoice <a name="get_by_id"></a>

**API Endpoint**: `GET /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter              | Required | Description                                                                            | Example                                  |
| ---------------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`        |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`         |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `repeating_invoice_id` |    ✓     | Unique identifier for a Repeating Invoice                                              | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`       |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.repeating_invoices.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.repeating_invoices.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

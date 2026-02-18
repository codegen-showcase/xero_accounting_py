# purchase_orders.attachments

## Module Functions

### Retrieves attachments for a specific purchase order <a name="list"></a>

**API Endpoint**: `GET /PurchaseOrders/{PurchaseOrderID}/Attachments`

#### Parameters

| Parameter           | Required | Description                             | Example                                  |
| ------------------- | :------: | --------------------------------------- | ---------------------------------------- |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant              | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.attachments.list(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.attachments.list(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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

### Retrieves specific attachment for a specific purchase order using a unique attachment Id <a name="get_by_id"></a>

**API Endpoint**: `GET /PurchaseOrders/{PurchaseOrderID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter           | Required | Description                                                                            | Example                                  |
| ------------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`     |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`      |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order                                                | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves specific purchase order as PDF files using a unique purchase order Id <a name="get_as_pdf"></a>

**API Endpoint**: `GET /PurchaseOrders/{PurchaseOrderID}/pdf`

#### Parameters

| Parameter           | Required | Description                             | Example                                  |
| ------------------- | :------: | --------------------------------------- | ---------------------------------------- |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant              | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.attachments.get_as_pdf(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.attachments.get_as_pdf(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

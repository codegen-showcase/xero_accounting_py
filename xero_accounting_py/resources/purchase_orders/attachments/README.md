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

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.purchase_orders.attachments.list(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
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

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.purchase_orders.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves a specific attachment for a specific purchase order by filename <a name="get_by_filename"></a>

**API Endpoint**: `GET /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}`

#### Parameters

| Parameter           | Required | Description                                                                            | Example                                  |
| ------------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `content_type`      |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `file_name`         |    ✓     | Name of the attachment                                                                 | `"xero-dev.jpg"`                         |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order                                                | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.purchase_orders.attachments.get_by_filename(
    content_type="image/jpg",
    file_name="xero-dev.jpg",
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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
res = await client.purchase_orders.attachments.get_by_filename(
    content_type="image/jpg",
    file_name="xero-dev.jpg",
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

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.purchase_orders.attachments.get_as_pdf(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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
res = await client.purchase_orders.attachments.get_as_pdf(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Updates a specific attachment for a specific purchase order by filename <a name="update_by_filename"></a>

**API Endpoint**: `POST /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}`

#### Parameters

| Parameter           | Required | Description                             | Example                                  |
| ------------------- | :------: | --------------------------------------- | ---------------------------------------- |
| `data`              |    ✓     |                                         | `"string"`                               |
| `file_name`         |    ✓     | Name of the attachment                  | `"xero-dev.jpg"`                         |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant              | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.purchase_orders.attachments.update_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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
res = await client.purchase_orders.attachments.update_by_filename(
    data="string",
    file_name="xero-dev.jpg",
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

### Creates attachment for a specific purchase order <a name="create_by_filename"></a>

**API Endpoint**: `PUT /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}`

#### Parameters

| Parameter           | Required | Description                             | Example                                  |
| ------------------- | :------: | --------------------------------------- | ---------------------------------------- |
| `data`              |    ✓     |                                         | `"string"`                               |
| `file_name`         |    ✓     | Name of the attachment                  | `"xero-dev.jpg"`                         |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant              | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.purchase_orders.attachments.create_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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
res = await client.purchase_orders.attachments.create_by_filename(
    data="string",
    file_name="xero-dev.jpg",
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

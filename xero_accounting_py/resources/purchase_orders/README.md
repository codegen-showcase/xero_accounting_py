# purchase_orders

## Module Functions

### Retrieves purchase orders <a name="list"></a>

**API Endpoint**: `GET /PurchaseOrders`

#### Parameters

| Parameter        | Required | Description                                                                                                                                                                                                                                                           | Example                     |
| ---------------- | :------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                                                                                                                                                                            | `"YOUR_XERO_TENANT_ID"`     |
| `date_from`      |    ✗     | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31                                                                                                                                                              | `"2019-12-01"`              |
| `date_to`        |    ✗     | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31                                                                                                                                                              | `"2019-12-31"`              |
| `order`          |    ✗     | Order by an any element                                                                                                                                                                                                                                               | `"PurchaseOrderNumber ASC"` |
| `page`           |    ✗     | To specify a page, append the page parameter to the URL e.g. ?page=1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page=2 and continuing this process until no more results are returned. | `1`                         |
| `page_size`      |    ✗     | Number of records to retrieve per page                                                                                                                                                                                                                                | `100`                       |
| `status`         |    ✗     | Filter by purchase order status                                                                                                                                                                                                                                       | `"SUBMITTED"`               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date_from="2019-12-01",
    date_to="2019-12-31",
    order="PurchaseOrderNumber ASC",
    page=1,
    page_size=100,
    status="SUBMITTED",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date_from="2019-12-01",
    date_to="2019-12-31",
    order="PurchaseOrderNumber ASC",
    page=1,
    page_size=100,
    status="SUBMITTED",
)
```

#### Response

##### Type

[PurchaseOrders](/xero_accounting_py/types/models/purchase_orders.py)

##### Example

```python
{}
```

### Retrieves a specific purchase order using a unique purchase order Id <a name="get"></a>

**API Endpoint**: `GET /PurchaseOrders/{PurchaseOrderID}`

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
res = client.purchase_orders.get(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.get(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[PurchaseOrders](/xero_accounting_py/types/models/purchase_orders.py)

##### Example

```python
{}
```

### Updates or creates one or more purchase orders <a name="update_or_create"></a>

**API Endpoint**: `POST /PurchaseOrders`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                 |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `pagination`       |    ✗     |                                                                                               | `{}`                    |
| `└─ item_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page`          |    ✗     |                                                                                               | `123`                   |
| `└─ page_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page_size`     |    ✗     |                                                                                               | `123`                   |
| `purchase_orders`  |    ✗     |                                                                                               | `[]`                    |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                               | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    purchase_orders=[
        {
            "date": "2019-03-13",
            "line_items": [
                {
                    "account_code": "710",
                    "description": "Foobar",
                    "quantity": 1.0,
                    "unit_amount": 20.0,
                }
            ],
        }
    ],
    summarize_errors=True,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    purchase_orders=[
        {
            "date": "2019-03-13",
            "line_items": [
                {
                    "account_code": "710",
                    "description": "Foobar",
                    "quantity": 1.0,
                    "unit_amount": 20.0,
                }
            ],
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[PurchaseOrders](/xero_accounting_py/types/models/purchase_orders.py)

##### Example

```python
{}
```

### Updates a specific purchase order <a name="update"></a>

**API Endpoint**: `POST /PurchaseOrders/{PurchaseOrderID}`

#### Parameters

| Parameter           | Required | Description                                     | Example                                  |
| ------------------- | :------: | ----------------------------------------------- | ---------------------------------------- |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order         | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                      | `"YOUR_XERO_TENANT_ID"`                  |
| `pagination`        |    ✗     |                                                 | `{}`                                     |
| `└─ item_count`     |    ✗     |                                                 | `123`                                    |
| `└─ page`           |    ✗     |                                                 | `123`                                    |
| `└─ page_count`     |    ✗     |                                                 | `123`                                    |
| `└─ page_size`      |    ✗     |                                                 | `123`                                    |
| `purchase_orders`   |    ✗     |                                                 | `[]`                                     |
| `warnings`          |    ✗     | Displays array of warning messages from the API | `[{}]`                                   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.update(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    purchase_orders=[
        {
            "attention_to": "Peter Parker",
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.update(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    purchase_orders=[
        {
            "attention_to": "Peter Parker",
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
        }
    ],
)
```

#### Response

##### Type

[PurchaseOrders](/xero_accounting_py/types/models/purchase_orders.py)

##### Example

```python
{}
```

### Creates one or more purchase orders <a name="create"></a>

**API Endpoint**: `PUT /PurchaseOrders`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                 |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `pagination`       |    ✗     |                                                                                               | `{}`                    |
| `└─ item_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page`          |    ✗     |                                                                                               | `123`                   |
| `└─ page_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page_size`     |    ✗     |                                                                                               | `123`                   |
| `purchase_orders`  |    ✗     |                                                                                               | `[]`                    |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                               | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    purchase_orders=[
        {
            "date": "2019-03-13",
            "line_items": [
                {
                    "account_code": "710",
                    "description": "Foobar",
                    "quantity": 1.0,
                    "unit_amount": 20.0,
                }
            ],
        }
    ],
    summarize_errors=True,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    purchase_orders=[
        {
            "date": "2019-03-13",
            "line_items": [
                {
                    "account_code": "710",
                    "description": "Foobar",
                    "quantity": 1.0,
                    "unit_amount": 20.0,
                }
            ],
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[PurchaseOrders](/xero_accounting_py/types/models/purchase_orders.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history

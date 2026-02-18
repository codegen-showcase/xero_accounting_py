# purchase_orders.history

## Module Functions

### Retrieves history for a specific purchase order <a name="list"></a>

**API Endpoint**: `GET /PurchaseOrders/{PurchaseOrderID}/History`

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
res = client.purchase_orders.history.list(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.history.list(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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

### Creates a history record for a specific purchase orders <a name="create_record"></a>

**API Endpoint**: `PUT /PurchaseOrders/{PurchaseOrderID}/History`

#### Parameters

| Parameter           | Required | Description                             | Example                                   |
| ------------------- | :------: | --------------------------------------- | ----------------------------------------- |
| `purchase_order_id` |    ✓     | Unique identifier for an Purchase Order | `"00000000-0000-0000-0000-000000000000"`  |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant              | `"YOUR_XERO_TENANT_ID"`                   |
| `history_records`   |    ✗     |                                         | `[{"date_utc": "/Date(1573755038314)/"}]` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.purchase_orders.history.create_record(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    history_records=[{"details": "Hello World"}],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.purchase_orders.history.create_record(
    purchase_order_id="00000000-0000-0000-0000-000000000000",
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

# receipts

## Module Functions

### Retrieves draft expense claim receipts for any user <a name="list"></a>

**API Endpoint**: `GET /Receipts`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                 |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element                                                                          | `"ReceiptNumber ASC"`   |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                     |
| `where`          |    ✗     | Filter by an any element                                                                         | `"Status==\"DRAFT\""`   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.receipts.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="ReceiptNumber ASC",
    unitdp=4,
    where='Status=="DRAFT"',
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.receipts.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="ReceiptNumber ASC",
    unitdp=4,
    where='Status=="DRAFT"',
)
```

#### Response

##### Type

[Receipts](/xero_accounting_py/types/models/receipts.py)

##### Example

```python
{}
```

### Retrieves a specific draft expense claim receipt by using a unique receipt Id <a name="get"></a>

**API Endpoint**: `GET /Receipts/{ReceiptID}`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                                  |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `receipt_id`     |    ✓     | Unique identifier for a Receipt                                                                  | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.receipts.get(
    receipt_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.receipts.get(
    receipt_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Response

##### Type

[Receipts](/xero_accounting_py/types/models/receipts.py)

##### Example

```python
{}
```

### Updates a specific draft expense claim receipts <a name="update"></a>

**API Endpoint**: `POST /Receipts/{ReceiptID}`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                                  |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `receipt_id`     |    ✓     | Unique identifier for a Receipt                                                                  | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `receipts`       |    ✗     |                                                                                                  | `[]`                                     |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.receipts.update(
    receipt_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    receipts=[
        {
            "reference": "Foobar",
            "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
        }
    ],
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.receipts.update(
    receipt_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    receipts=[
        {
            "reference": "Foobar",
            "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
        }
    ],
    unitdp=4,
)
```

#### Response

##### Type

[Receipts](/xero_accounting_py/types/models/receipts.py)

##### Example

```python
{}
```

### Creates draft expense claim receipts for any user <a name="create"></a>

**API Endpoint**: `PUT /Receipts`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                 |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"` |
| `receipts`       |    ✗     |                                                                                                  | `[]`                    |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                     |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.receipts.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    receipts=[
        {
            "line_amount_types": "NoTax",
            "status": "DRAFT",
            "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
        }
    ],
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.receipts.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    receipts=[
        {
            "line_amount_types": "NoTax",
            "status": "DRAFT",
            "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
        }
    ],
    unitdp=4,
)
```

#### Response

##### Type

[Receipts](/xero_accounting_py/types/models/receipts.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history

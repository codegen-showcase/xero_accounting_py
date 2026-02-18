# items

## Module Functions

### Deletes a specific item <a name="delete"></a>

**API Endpoint**: `DELETE /Items/{ItemID}`

#### Parameters

| Parameter        | Required | Description                   | Example                                  |
| ---------------- | :------: | ----------------------------- | ---------------------------------------- |
| `item_id`        |    ✓     | Unique identifier for an Item | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant    | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.items.delete(
    item_id="00000000-0000-0000-0000-000000000000", xero_tenant_id="YOUR_XERO_TENANT_ID"
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.items.delete(
    item_id="00000000-0000-0000-0000-000000000000", xero_tenant_id="YOUR_XERO_TENANT_ID"
)
```

### Retrieves items <a name="list"></a>

**API Endpoint**: `GET /Items`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                 |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element                                                                          | `"Code ASC"`            |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                     |
| `where`          |    ✗     | Filter by an any element                                                                         | `"IsSold==true"`        |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.items.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Code ASC",
    unitdp=4,
    where="IsSold==true",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.items.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Code ASC",
    unitdp=4,
    where="IsSold==true",
)
```

#### Response

##### Type

[Items](/xero_accounting_py/types/models/items.py)

##### Example

```python
{}
```

### Retrieves a specific item using a unique item Id <a name="get"></a>

**API Endpoint**: `GET /Items/{ItemID}`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                                  |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `item_id`        |    ✓     | Unique identifier for an Item                                                                    | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.items.get(
    item_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.items.get(
    item_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Response

##### Type

[Items](/xero_accounting_py/types/models/items.py)

##### Example

```python
{}
```

### Updates or creates one or more items <a name="update_or_create"></a>

**API Endpoint**: `POST /Items`

#### Parameters

| Parameter          | Required | Description                                                                                      | Example                                                             |
| ------------------ | :------: | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                                             |
| `items`            |    ✗     |                                                                                                  | `[{"code": "string", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors    | `True`                                                              |
| `unitdp`           |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                                                 |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.items.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    items=[
        {
            "code": "ItemCode123",
            "description": "Item Description ABC",
            "name": "ItemName XYZ",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.items.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    items=[
        {
            "code": "ItemCode123",
            "description": "Item Description ABC",
            "name": "ItemName XYZ",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Response

##### Type

[Items](/xero_accounting_py/types/models/items.py)

##### Example

```python
{}
```

### Updates a specific item <a name="update"></a>

**API Endpoint**: `POST /Items/{ItemID}`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                                                             |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| `item_id`        |    ✓     | Unique identifier for an Item                                                                    | `"00000000-0000-0000-0000-000000000000"`                            |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                                             |
| `items`          |    ✗     |                                                                                                  | `[{"code": "string", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                                                 |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.items.update(
    item_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    items=[{"code": "ItemCode123", "description": "Description 123"}],
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.items.update(
    item_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    items=[{"code": "ItemCode123", "description": "Description 123"}],
    unitdp=4,
)
```

#### Response

##### Type

[Items](/xero_accounting_py/types/models/items.py)

##### Example

```python
{}
```

### Creates one or more items <a name="create"></a>

**API Endpoint**: `PUT /Items`

#### Parameters

| Parameter          | Required | Description                                                                                      | Example                                                             |
| ------------------ | :------: | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                                             |
| `items`            |    ✗     |                                                                                                  | `[{"code": "string", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors    | `True`                                                              |
| `unitdp`           |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                                                 |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.items.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    items=[
        {
            "code": "code123",
            "description": "Foobar",
            "inventory_asset_account_code": "140",
            "name": "Item Name XYZ",
            "purchase_details": {"cogs_account_code": "500"},
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.items.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    items=[
        {
            "code": "code123",
            "description": "Foobar",
            "inventory_asset_account_code": "140",
            "name": "Item Name XYZ",
            "purchase_details": {"cogs_account_code": "500"},
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Response

##### Type

[Items](/xero_accounting_py/types/models/items.py)

##### Example

```python
{}
```

## Submodules

- [history](history/README.md) - history

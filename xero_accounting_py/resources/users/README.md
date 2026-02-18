# users

## Module Functions

### Retrieves users <a name="list"></a>

**API Endpoint**: `GET /Users`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element    | `"LastName ASC"`        |
| `where`          |    ✗     | Filter by an any element   | `"IsSubscriber==true"`  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.users.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="LastName ASC",
    where="IsSubscriber==true",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.users.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="LastName ASC",
    where="IsSubscriber==true",
)
```

#### Response

##### Type

[Users](/xero_accounting_py/types/models/users.py)

##### Example

```python
{}
```

### Retrieves a specific user <a name="get"></a>

**API Endpoint**: `GET /Users/{UserID}`

#### Parameters

| Parameter        | Required | Description                  | Example                                  |
| ---------------- | :------: | ---------------------------- | ---------------------------------------- |
| `user_id`        |    ✓     | Unique identifier for a User | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant   | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.users.get(
    user_id="00000000-0000-0000-0000-000000000000", xero_tenant_id="YOUR_XERO_TENANT_ID"
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.users.get(
    user_id="00000000-0000-0000-0000-000000000000", xero_tenant_id="YOUR_XERO_TENANT_ID"
)
```

#### Response

##### Type

[Users](/xero_accounting_py/types/models/users.py)

##### Example

```python
{}
```

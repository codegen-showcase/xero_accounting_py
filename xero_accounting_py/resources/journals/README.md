# journals

## Module Functions

### Retrieves journals <a name="list"></a>

**API Endpoint**: `GET /Journals`

#### Parameters

| Parameter        | Required | Description                                                                                                       | Example                 |
| ---------------- | :------: | ----------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                        | `"YOUR_XERO_TENANT_ID"` |
| `offset`         |    ✗     | Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned | `10`                    |
| `payments_only`  |    ✗     | Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default.                | `True`                  |

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
res = client.journals.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", offset=10, payments_only=True
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
res = await client.journals.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", offset=10, payments_only=True
)
```

#### Response

##### Type

[Journals](/xero_accounting_py/types/models/journals.py)

##### Example

```python
{}
```

### Retrieves a specific journal using a unique journal Id. <a name="get"></a>

**API Endpoint**: `GET /Journals/{JournalID}`

#### Parameters

| Parameter        | Required | Description                     | Example                                  |
| ---------------- | :------: | ------------------------------- | ---------------------------------------- |
| `journal_id`     |    ✓     | Unique identifier for a Journal | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant      | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.journals.get(
    journal_id="00000000-0000-0000-0000-000000000000",
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
res = await client.journals.get(
    journal_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Journals](/xero_accounting_py/types/models/journals.py)

##### Example

```python
{}
```

### Retrieves a specific journal using a unique journal number. <a name="get_by_number"></a>

**API Endpoint**: `GET /Journals/{JournalNumber}`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `journal_number` |    ✓     | Number of a Journal        | `1000`                  |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |

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
res = client.journals.get_by_number(
    journal_number=1000, xero_tenant_id="YOUR_XERO_TENANT_ID"
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
res = await client.journals.get_by_number(
    journal_number=1000, xero_tenant_id="YOUR_XERO_TENANT_ID"
)
```

#### Response

##### Type

[Journals](/xero_accounting_py/types/models/journals.py)

##### Example

```python
{}
```

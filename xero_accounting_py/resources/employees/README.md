# employees

## Module Functions

### Retrieves employees used in Xero payrun <a name="list"></a>

This endpoint is deprecated and will be removed April 28, 2026

**API Endpoint**: `GET /Employees`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element    | `"LastName ASC"`        |
| `where`          |    ✗     | Filter by an any element   | `"Status==\"ACTIVE\""`  |

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
res = client.employees.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="LastName ASC", where='Status=="ACTIVE"'
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
res = await client.employees.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="LastName ASC", where='Status=="ACTIVE"'
)
```

#### Response

##### Type

[Employees](/xero_accounting_py/types/models/employees.py)

##### Example

```python
{}
```

### Retrieves a specific employee used in Xero payrun using a unique employee Id <a name="get"></a>

This endpoint is deprecated and will be removed April 28, 2026

**API Endpoint**: `GET /Employees/{EmployeeID}`

#### Parameters

| Parameter        | Required | Description                      | Example                                  |
| ---------------- | :------: | -------------------------------- | ---------------------------------------- |
| `employee_id`    |    ✓     | Unique identifier for a Employee | `"00000000-0000-0000-0000-000000000000"` |
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
res = client.employees.get(
    employee_id="00000000-0000-0000-0000-000000000000",
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
res = await client.employees.get(
    employee_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Employees](/xero_accounting_py/types/models/employees.py)

##### Example

```python
{}
```

### Creates a single new employees used in Xero payrun <a name="update_or_create"></a>

This endpoint is deprecated and will be removed April 28, 2026

**API Endpoint**: `POST /Employees`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                                                                               |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"`                                                               |
| `employees`        |    ✗     |                                                                                               | `[{"status_attribute_string": "ERROR", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                                                                                |

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
res = client.employees.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    employees=[
        {
            "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
            "first_name": "Nick",
            "last_name": "Fury",
        }
    ],
    summarize_errors=True,
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
res = await client.employees.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    employees=[
        {
            "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
            "first_name": "Nick",
            "last_name": "Fury",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[Employees](/xero_accounting_py/types/models/employees.py)

##### Example

```python
{}
```

### Creates new employees used in Xero payrun <a name="create"></a>

This endpoint is deprecated and will be removed April 28, 2026

**API Endpoint**: `PUT /Employees`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                                                                               |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"`                                                               |
| `employees`        |    ✗     |                                                                                               | `[{"status_attribute_string": "ERROR", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                                                                                |

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
res = client.employees.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    employees=[
        {
            "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
            "first_name": "Nick",
            "last_name": "Fury",
        }
    ],
    summarize_errors=True,
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
res = await client.employees.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    employees=[
        {
            "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
            "first_name": "Nick",
            "last_name": "Fury",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[Employees](/xero_accounting_py/types/models/employees.py)

##### Example

```python
{}
```

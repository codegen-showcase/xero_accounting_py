# quotes

## Module Functions

### Retrieves sales quotes <a name="list"></a>

**API Endpoint**: `GET /Quotes`

#### Parameters

| Parameter          | Required | Description                                                                                               | Example                                  |
| ------------------ | :------: | --------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                                | `"YOUR_XERO_TENANT_ID"`                  |
| `contact_id`       |    ✗     | Filter for quotes belonging to a particular contact                                                       | `"00000000-0000-0000-0000-000000000000"` |
| `date_from`        |    ✗     | Filter for quotes after a particular date                                                                 | `"2019-10-31"`                           |
| `date_to`          |    ✗     | Filter for quotes before a particular date                                                                | `"2019-10-31"`                           |
| `expiry_date_from` |    ✗     | Filter for quotes expiring after a particular date                                                        | `"2019-10-31"`                           |
| `expiry_date_to`   |    ✗     | Filter for quotes before a particular date                                                                | `"2019-10-31"`                           |
| `order`            |    ✗     | Order by an any element                                                                                   | `"Status ASC"`                           |
| `page`             |    ✗     | e.g. page=1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote | `1`                                      |
| `quote_number`     |    ✗     | Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber=QU-0001)                                  | `"QU-0001"`                              |
| `status`           |    ✗     | Filter for quotes of a particular Status                                                                  | `"DRAFT"`                                |

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
res = client.quotes.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contact_id="00000000-0000-0000-0000-000000000000",
    date_from="2019-10-31",
    date_to="2019-10-31",
    expiry_date_from="2019-10-31",
    expiry_date_to="2019-10-31",
    order="Status ASC",
    page=1,
    quote_number="QU-0001",
    status="DRAFT",
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
res = await client.quotes.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contact_id="00000000-0000-0000-0000-000000000000",
    date_from="2019-10-31",
    date_to="2019-10-31",
    expiry_date_from="2019-10-31",
    expiry_date_to="2019-10-31",
    order="Status ASC",
    page=1,
    quote_number="QU-0001",
    status="DRAFT",
)
```

#### Response

##### Type

[Quotes](/xero_accounting_py/types/models/quotes.py)

##### Example

```python
{}
```

### Retrieves a specific quote using a unique quote Id <a name="get"></a>

**API Endpoint**: `GET /Quotes/{QuoteID}`

#### Parameters

| Parameter        | Required | Description                    | Example                                  |
| ---------------- | :------: | ------------------------------ | ---------------------------------------- |
| `quote_id`       |    ✓     | Unique identifier for an Quote | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant     | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.quotes.get(
    quote_id="00000000-0000-0000-0000-000000000000",
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
res = await client.quotes.get(
    quote_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Quotes](/xero_accounting_py/types/models/quotes.py)

##### Example

```python
{}
```

### Retrieves a specific quote as a PDF file using a unique quote Id <a name="get_as_pdf"></a>

**API Endpoint**: `GET /Quotes/{QuoteID}/pdf`

#### Parameters

| Parameter        | Required | Description                    | Example                                  |
| ---------------- | :------: | ------------------------------ | ---------------------------------------- |
| `quote_id`       |    ✓     | Unique identifier for an Quote | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant     | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.quotes.get_as_pdf(
    quote_id="00000000-0000-0000-0000-000000000000",
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
res = await client.quotes.get_as_pdf(
    quote_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Updates or creates one or more quotes <a name="update_or_create"></a>

**API Endpoint**: `POST /Quotes`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                 |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `quotes`           |    ✗     |                                                                                               | `[]`                    |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |

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
res = client.quotes.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    quotes=[
        {
            "date": "2020-02-01",
            "line_items": [
                {
                    "account_code": "12775",
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

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.quotes.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    quotes=[
        {
            "date": "2020-02-01",
            "line_items": [
                {
                    "account_code": "12775",
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

[Quotes](/xero_accounting_py/types/models/quotes.py)

##### Example

```python
{}
```

### Updates a specific quote <a name="update"></a>

**API Endpoint**: `POST /Quotes/{QuoteID}`

#### Parameters

| Parameter        | Required | Description                    | Example                                  |
| ---------------- | :------: | ------------------------------ | ---------------------------------------- |
| `quote_id`       |    ✓     | Unique identifier for an Quote | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant     | `"YOUR_XERO_TENANT_ID"`                  |
| `quotes`         |    ✗     |                                | `[]`                                     |

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
res = client.quotes.update(
    quote_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    quotes=[{"date": "2020-02-01", "reference": "I am an update"}],
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
res = await client.quotes.update(
    quote_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    quotes=[{"date": "2020-02-01", "reference": "I am an update"}],
)
```

#### Response

##### Type

[Quotes](/xero_accounting_py/types/models/quotes.py)

##### Example

```python
{}
```

### Create one or more quotes <a name="create"></a>

**API Endpoint**: `PUT /Quotes`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                 |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `quotes`           |    ✗     |                                                                                               | `[]`                    |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |

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
res = client.quotes.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    quotes=[
        {
            "date": "2020-02-01",
            "line_items": [
                {
                    "account_code": "12775",
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

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.quotes.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    quotes=[
        {
            "date": "2020-02-01",
            "line_items": [
                {
                    "account_code": "12775",
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

[Quotes](/xero_accounting_py/types/models/quotes.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history

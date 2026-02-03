# credit_notes

## Module Functions

### Retrieves any credit notes <a name="list"></a>

**API Endpoint**: `GET /CreditNotes`

#### Parameters

| Parameter        | Required | Description                                                                                                           | Example                  |
| ---------------- | :------: | --------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                            | `"YOUR_XERO_TENANT_ID"`  |
| `order`          |    ✗     | Order by an any element                                                                                               | `"CreditNoteNumber ASC"` |
| `page`           |    ✗     | e.g. page=1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note | `1`                      |
| `page_size`      |    ✗     | Number of records to retrieve per page                                                                                | `100`                    |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts                      | `4`                      |
| `where`          |    ✗     | Filter by an any element                                                                                              | `"Status==\"DRAFT\""`    |

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
res = client.credit_notes.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="CreditNoteNumber ASC",
    page=1,
    page_size=100,
    unitdp=4,
    where='Status=="DRAFT"',
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
res = await client.credit_notes.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="CreditNoteNumber ASC",
    page=1,
    page_size=100,
    unitdp=4,
    where='Status=="DRAFT"',
)
```

#### Response

##### Type

[CreditNotes](/xero_accounting_py/types/models/credit_notes.py)

##### Example

```python
{}
```

### Retrieves a specific credit note using a unique credit note Id <a name="get"></a>

**API Endpoint**: `GET /CreditNotes/{CreditNoteID}`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                                  |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note                                                              | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |

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
res = client.credit_notes.get(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
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
res = await client.credit_notes.get(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Response

##### Type

[CreditNotes](/xero_accounting_py/types/models/credit_notes.py)

##### Example

```python
{}
```

### Updates or creates one or more credit notes <a name="update_or_create"></a>

**API Endpoint**: `POST /CreditNotes`

#### Parameters

| Parameter          | Required | Description                                                                                      | Example                 |
| ------------------ | :------: | ------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"` |
| `credit_notes`     |    ✗     |                                                                                                  | `[]`                    |
| `pagination`       |    ✗     |                                                                                                  | `{}`                    |
| `└─ item_count`    |    ✗     |                                                                                                  | `123`                   |
| `└─ page`          |    ✗     |                                                                                                  | `123`                   |
| `└─ page_count`    |    ✗     |                                                                                                  | `123`                   |
| `└─ page_size`     |    ✗     |                                                                                                  | `123`                   |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors    | `True`                  |
| `unitdp`           |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                     |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                                  | `[{}]`                  |

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
res = client.credit_notes.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    credit_notes=[
        {
            "date": "2019-01-05",
            "line_items": [
                {
                    "account_code": "400",
                    "description": "Foobar",
                    "quantity": 2.0,
                    "unit_amount": 20.0,
                }
            ],
            "reference": "HelloWorld",
            "status": "AUTHORISED",
            "type_": "ACCPAYCREDIT",
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

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.credit_notes.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    credit_notes=[
        {
            "date": "2019-01-05",
            "line_items": [
                {
                    "account_code": "400",
                    "description": "Foobar",
                    "quantity": 2.0,
                    "unit_amount": 20.0,
                }
            ],
            "reference": "HelloWorld",
            "status": "AUTHORISED",
            "type_": "ACCPAYCREDIT",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Response

##### Type

[CreditNotes](/xero_accounting_py/types/models/credit_notes.py)

##### Example

```python
{}
```

### Updates a specific credit note <a name="update"></a>

**API Endpoint**: `POST /CreditNotes/{CreditNoteID}`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                                  |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note                                                              | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `credit_notes`   |    ✗     |                                                                                                  | `[]`                                     |
| `pagination`     |    ✗     |                                                                                                  | `{}`                                     |
| `└─ item_count`  |    ✗     |                                                                                                  | `123`                                    |
| `└─ page`        |    ✗     |                                                                                                  | `123`                                    |
| `└─ page_count`  |    ✗     |                                                                                                  | `123`                                    |
| `└─ page_size`   |    ✗     |                                                                                                  | `123`                                    |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |
| `warnings`       |    ✗     | Displays array of warning messages from the API                                                  | `[{}]`                                   |

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
res = client.credit_notes.update(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    credit_notes=[
        {
            "date": "2019-01-05",
            "line_items": [
                {
                    "account_code": "400",
                    "description": "Foobar",
                    "quantity": 2.0,
                    "unit_amount": 20.0,
                }
            ],
            "reference": "HelloWorld",
            "sent_to_contact": True,
            "status": "AUTHORISED",
            "type_": "ACCPAYCREDIT",
        }
    ],
    unitdp=4,
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
res = await client.credit_notes.update(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    credit_notes=[
        {
            "date": "2019-01-05",
            "line_items": [
                {
                    "account_code": "400",
                    "description": "Foobar",
                    "quantity": 2.0,
                    "unit_amount": 20.0,
                }
            ],
            "reference": "HelloWorld",
            "sent_to_contact": True,
            "status": "AUTHORISED",
            "type_": "ACCPAYCREDIT",
        }
    ],
    unitdp=4,
)
```

#### Response

##### Type

[CreditNotes](/xero_accounting_py/types/models/credit_notes.py)

##### Example

```python
{}
```

### Creates a new credit note <a name="create"></a>

**API Endpoint**: `PUT /CreditNotes`

#### Parameters

| Parameter          | Required | Description                                                                                      | Example                 |
| ------------------ | :------: | ------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"` |
| `credit_notes`     |    ✗     |                                                                                                  | `[]`                    |
| `pagination`       |    ✗     |                                                                                                  | `{}`                    |
| `└─ item_count`    |    ✗     |                                                                                                  | `123`                   |
| `└─ page`          |    ✗     |                                                                                                  | `123`                   |
| `└─ page_count`    |    ✗     |                                                                                                  | `123`                   |
| `└─ page_size`     |    ✗     |                                                                                                  | `123`                   |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors    | `True`                  |
| `unitdp`           |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                     |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                                  | `[{}]`                  |

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
res = client.credit_notes.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    credit_notes=[
        {
            "date": "2019-01-05",
            "line_items": [
                {
                    "account_code": "400",
                    "description": "Foobar",
                    "quantity": 2.0,
                    "unit_amount": 20.0,
                }
            ],
            "type_": "ACCPAYCREDIT",
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

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.credit_notes.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    credit_notes=[
        {
            "date": "2019-01-05",
            "line_items": [
                {
                    "account_code": "400",
                    "description": "Foobar",
                    "quantity": 2.0,
                    "unit_amount": 20.0,
                }
            ],
            "type_": "ACCPAYCREDIT",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Response

##### Type

[CreditNotes](/xero_accounting_py/types/models/credit_notes.py)

##### Example

```python
{}
```

## Submodules

- [allocations](allocations/README.md) - allocations
- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history
- [pdf](pdf/README.md) - pdf

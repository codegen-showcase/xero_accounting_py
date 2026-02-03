# manual_journals

## Module Functions

### Retrieves manual journals <a name="list"></a>

**API Endpoint**: `GET /ManualJournals`

#### Parameters

| Parameter        | Required | Description                                                                                                              | Example                 |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                               | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element                                                                                                  | `"Date ASC"`            |
| `page`           |    ✗     | e.g. page=1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment | `1`                     |
| `page_size`      |    ✗     | Number of records to retrieve per page                                                                                   | `100`                   |
| `where`          |    ✗     | Filter by an any element                                                                                                 | `"Status==\"DRAFT\""`   |

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
res = client.manual_journals.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Date ASC",
    page=1,
    page_size=100,
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
res = await client.manual_journals.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Date ASC",
    page=1,
    page_size=100,
    where='Status=="DRAFT"',
)
```

#### Response

##### Type

[ManualJournals](/xero_accounting_py/types/models/manual_journals.py)

##### Example

```python
{}
```

### Retrieves a specific manual journal <a name="get"></a>

**API Endpoint**: `GET /ManualJournals/{ManualJournalID}`

#### Parameters

| Parameter           | Required | Description                           | Example                                  |
| ------------------- | :------: | ------------------------------------- | ---------------------------------------- |
| `manual_journal_id` |    ✓     | Unique identifier for a ManualJournal | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant            | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.manual_journals.get(
    manual_journal_id="00000000-0000-0000-0000-000000000000",
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
res = await client.manual_journals.get(
    manual_journal_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[ManualJournals](/xero_accounting_py/types/models/manual_journals.py)

##### Example

```python
{}
```

### Updates or creates a single manual journal <a name="update_or_create"></a>

**API Endpoint**: `POST /ManualJournals`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                                                                                                                               |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"`                                                                                                               |
| `manual_journals`  |    ✗     |                                                                                               | `[{"has_attachments": True, "narration": "string", "status_attribute_string": "ERROR", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `pagination`       |    ✗     |                                                                                               | `{}`                                                                                                                                  |
| `└─ item_count`    |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `└─ page`          |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `└─ page_count`    |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `└─ page_size`     |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                                                                                                                                |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                               | `[{}]`                                                                                                                                |

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
res = client.manual_journals.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    manual_journals=[
        {
            "date": "2019-03-14",
            "journal_lines": [
                {
                    "account_code": "400",
                    "description": "Money Movement",
                    "line_amount": 100.0,
                },
                {
                    "account_code": "400",
                    "description": "Prepayment of things",
                    "line_amount": -100.0,
                    "tracking": [{"name": "North", "option": "Region"}],
                },
            ],
            "narration": "Journal Desc",
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
res = await client.manual_journals.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    manual_journals=[
        {
            "date": "2019-03-14",
            "journal_lines": [
                {
                    "account_code": "400",
                    "description": "Money Movement",
                    "line_amount": 100.0,
                },
                {
                    "account_code": "400",
                    "description": "Prepayment of things",
                    "line_amount": -100.0,
                    "tracking": [{"name": "North", "option": "Region"}],
                },
            ],
            "narration": "Journal Desc",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[ManualJournals](/xero_accounting_py/types/models/manual_journals.py)

##### Example

```python
{}
```

### Updates a specific manual journal <a name="update"></a>

**API Endpoint**: `POST /ManualJournals/{ManualJournalID}`

#### Parameters

| Parameter           | Required | Description                                     | Example                                                                                                                               |
| ------------------- | :------: | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `manual_journal_id` |    ✓     | Unique identifier for a ManualJournal           | `"00000000-0000-0000-0000-000000000000"`                                                                                              |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                      | `"YOUR_XERO_TENANT_ID"`                                                                                                               |
| `manual_journals`   |    ✗     |                                                 | `[{"has_attachments": True, "narration": "string", "status_attribute_string": "ERROR", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `pagination`        |    ✗     |                                                 | `{}`                                                                                                                                  |
| `└─ item_count`     |    ✗     |                                                 | `123`                                                                                                                                 |
| `└─ page`           |    ✗     |                                                 | `123`                                                                                                                                 |
| `└─ page_count`     |    ✗     |                                                 | `123`                                                                                                                                 |
| `└─ page_size`      |    ✗     |                                                 | `123`                                                                                                                                 |
| `warnings`          |    ✗     | Displays array of warning messages from the API | `[{}]`                                                                                                                                |

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
res = client.manual_journals.update(
    manual_journal_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    manual_journals=[
        {
            "journal_lines": [
                {
                    "account_code": "string",
                    "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                    "is_blank": False,
                    "line_amount": -2569.0,
                    "tax_amount": 0.0,
                }
            ],
            "manual_journal_id": "00000000-0000-0000-0000-000000000000",
            "narration": "Hello Xero",
        }
    ],
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
res = await client.manual_journals.update(
    manual_journal_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    manual_journals=[
        {
            "journal_lines": [
                {
                    "account_code": "string",
                    "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                    "is_blank": False,
                    "line_amount": -2569.0,
                    "tax_amount": 0.0,
                }
            ],
            "manual_journal_id": "00000000-0000-0000-0000-000000000000",
            "narration": "Hello Xero",
        }
    ],
)
```

#### Response

##### Type

[ManualJournals](/xero_accounting_py/types/models/manual_journals.py)

##### Example

```python
{}
```

### Creates one or more manual journals <a name="create"></a>

**API Endpoint**: `PUT /ManualJournals`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                                                                                                                               |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"`                                                                                                               |
| `manual_journals`  |    ✗     |                                                                                               | `[{"has_attachments": True, "narration": "string", "status_attribute_string": "ERROR", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `pagination`       |    ✗     |                                                                                               | `{}`                                                                                                                                  |
| `└─ item_count`    |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `└─ page`          |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `└─ page_count`    |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `└─ page_size`     |    ✗     |                                                                                               | `123`                                                                                                                                 |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                                                                                                                                |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                               | `[{}]`                                                                                                                                |

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
res = client.manual_journals.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    manual_journals=[
        {
            "date": "2019-03-14",
            "journal_lines": [
                {
                    "account_code": "400",
                    "description": "Money Movement",
                    "line_amount": 100.0,
                },
                {
                    "account_code": "400",
                    "description": "Prepayment of things",
                    "line_amount": -100.0,
                    "tracking": [{"name": "North", "option": "Region"}],
                },
            ],
            "narration": "Journal Desc",
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
res = await client.manual_journals.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    manual_journals=[
        {
            "date": "2019-03-14",
            "journal_lines": [
                {
                    "account_code": "400",
                    "description": "Money Movement",
                    "line_amount": 100.0,
                },
                {
                    "account_code": "400",
                    "description": "Prepayment of things",
                    "line_amount": -100.0,
                    "tracking": [{"name": "North", "option": "Region"}],
                },
            ],
            "narration": "Journal Desc",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[ManualJournals](/xero_accounting_py/types/models/manual_journals.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history

# credit_notes.history

## Module Functions

### Retrieves history records of a specific credit note <a name="list"></a>

**API Endpoint**: `GET /CreditNotes/{CreditNoteID}/History`

#### Parameters

| Parameter        | Required | Description                         | Example                                  |
| ---------------- | :------: | ----------------------------------- | ---------------------------------------- |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant          | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.credit_notes.history.list(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.credit_notes.history.list(
    credit_note_id="00000000-0000-0000-0000-000000000000",
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

### Retrieves history records of a specific credit note <a name="create_record"></a>

**API Endpoint**: `PUT /CreditNotes/{CreditNoteID}/History`

#### Parameters

| Parameter         | Required | Description                         | Example                                   |
| ----------------- | :------: | ----------------------------------- | ----------------------------------------- |
| `credit_note_id`  |    ✓     | Unique identifier for a Credit Note | `"00000000-0000-0000-0000-000000000000"`  |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant          | `"YOUR_XERO_TENANT_ID"`                   |
| `history_records` |    ✗     |                                     | `[{"date_utc": "/Date(1573755038314)/"}]` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.credit_notes.history.create_record(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    history_records=[{"details": "Hello World"}],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.credit_notes.history.create_record(
    credit_note_id="00000000-0000-0000-0000-000000000000",
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

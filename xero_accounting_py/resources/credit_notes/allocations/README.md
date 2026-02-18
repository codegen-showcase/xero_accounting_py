# credit_notes.allocations

## Module Functions

### Deletes an Allocation from a Credit Note <a name="delete"></a>

**API Endpoint**: `DELETE /CreditNotes/{CreditNoteID}/Allocations/{AllocationID}`

#### Parameters

| Parameter        | Required | Description                             | Example                                  |
| ---------------- | :------: | --------------------------------------- | ---------------------------------------- |
| `allocation_id`  |    ✓     | Unique identifier for Allocation object | `"00000000-0000-0000-0000-000000000000"` |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note     | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant              | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.credit_notes.allocations.delete(
    allocation_id="00000000-0000-0000-0000-000000000000",
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.credit_notes.allocations.delete(
    allocation_id="00000000-0000-0000-0000-000000000000",
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Allocation](/xero_accounting_py/types/models/allocation.py)

##### Example

```python
{"amount": 123.0, "date": "string", "invoice": {"has_attachments": False, "has_errors": False, "updated_date_utc": "/Date(1573755038314)/"}}
```

### Creates allocation for a specific credit note <a name="create"></a>

**API Endpoint**: `PUT /CreditNotes/{CreditNoteID}/Allocations`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                                  |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `credit_note_id`   |    ✓     | Unique identifier for a Credit Note                                                           | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"`                  |
| `allocations`      |    ✗     |                                                                                               | `[]`                                     |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                                   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.credit_notes.allocations.create(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    allocations=[
        {
            "amount": 1.0,
            "date": "2019-03-05",
            "invoice": {
                "invoice_id": "c45720a1-ade3-4a38-a064-d15489be6841",
                "line_items": [
                    {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "line_item_id": "00000000-0000-0000-0000-000000000000",
                        "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                    }
                ],
            },
        }
    ],
    summarize_errors=True,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.credit_notes.allocations.create(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    allocations=[
        {
            "amount": 1.0,
            "date": "2019-03-05",
            "invoice": {
                "invoice_id": "c45720a1-ade3-4a38-a064-d15489be6841",
                "line_items": [
                    {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "line_item_id": "00000000-0000-0000-0000-000000000000",
                        "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                    }
                ],
            },
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[Allocations](/xero_accounting_py/types/models/allocations.py)

##### Example

```python
{}
```

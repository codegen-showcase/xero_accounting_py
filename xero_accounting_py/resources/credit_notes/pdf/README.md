# credit_notes.pdf

## Module Functions

### Retrieves credit notes as PDF files <a name="get"></a>

**API Endpoint**: `GET /CreditNotes/{CreditNoteID}/pdf`

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
res = client.credit_notes.pdf.get(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.credit_notes.pdf.get(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

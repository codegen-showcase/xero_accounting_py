# bank_transactions.attachments

## Module Functions

### Retrieves any attachments from a specific bank transactions <a name="list"></a>

**API Endpoint**: `GET /BankTransactions/{BankTransactionID}/Attachments`

#### Parameters

| Parameter             | Required | Description                                             | Example                                  |
| --------------------- | :------: | ------------------------------------------------------- | ---------------------------------------- |
| `bank_transaction_id` |    ✓     | Xero generated unique identifier for a bank transaction | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`      |    ✓     | Xero identifier for Tenant                              | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transactions.attachments.list(
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transactions.attachments.list(
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Attachments](/xero_accounting_py/types/models/attachments.py)

##### Example

```python
{}
```

### Retrieves specific attachments from a specific BankTransaction using a unique attachment Id <a name="get_by_id"></a>

**API Endpoint**: `GET /BankTransactions/{BankTransactionID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter             | Required | Description                                                                            | Example                                  |
| --------------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`       |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `bank_transaction_id` |    ✓     | Xero generated unique identifier for a bank transaction                                | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`        |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `xero_tenant_id`      |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transactions.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transactions.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

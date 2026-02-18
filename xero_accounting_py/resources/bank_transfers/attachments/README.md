# bank_transfers.attachments

## Module Functions

### Retrieves attachments from a specific bank transfer <a name="list"></a>

**API Endpoint**: `GET /BankTransfers/{BankTransferID}/Attachments`

#### Parameters

| Parameter          | Required | Description                                          | Example                                  |
| ------------------ | :------: | ---------------------------------------------------- | ---------------------------------------- |
| `bank_transfer_id` |    ✓     | Xero generated unique identifier for a bank transfer | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                           | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transfers.attachments.list(
    bank_transfer_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transfers.attachments.list(
    bank_transfer_id="00000000-0000-0000-0000-000000000000",
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

### Retrieves a specific attachment from a specific bank transfer using a unique attachment ID <a name="get_by_id"></a>

**API Endpoint**: `GET /BankTransfers/{BankTransferID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter          | Required | Description                                                                            | Example                                  |
| ------------------ | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`    |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `bank_transfer_id` |    ✓     | Xero generated unique identifier for a bank transfer                                   | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`     |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transfers.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    bank_transfer_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transfers.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    bank_transfer_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

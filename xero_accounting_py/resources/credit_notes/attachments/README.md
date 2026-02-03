# credit_notes.attachments

## Module Functions

### Retrieves attachments for a specific credit notes <a name="list"></a>

**API Endpoint**: `GET /CreditNotes/{CreditNoteID}/Attachments`

#### Parameters

| Parameter        | Required | Description                         | Example                                  |
| ---------------- | :------: | ----------------------------------- | ---------------------------------------- |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant          | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.credit_notes.attachments.list(
    credit_note_id="00000000-0000-0000-0000-000000000000",
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
res = await client.credit_notes.attachments.list(
    credit_note_id="00000000-0000-0000-0000-000000000000",
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

### Retrieves a specific attachment from a specific credit note using a unique attachment Id <a name="get_by_id"></a>

**API Endpoint**: `GET /CreditNotes/{CreditNoteID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`  |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`   |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note                                                    | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.credit_notes.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    credit_note_id="00000000-0000-0000-0000-000000000000",
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
res = await client.credit_notes.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    credit_note_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves a specific attachment on a specific credit note by file name <a name="get_by_filename"></a>

**API Endpoint**: `GET /CreditNotes/{CreditNoteID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `content_type`   |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note                                                    | `"00000000-0000-0000-0000-000000000000"` |
| `file_name`      |    ✓     | Name of the attachment                                                                 | `"xero-dev.jpg"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.credit_notes.attachments.get_by_filename(
    content_type="image/jpg",
    credit_note_id="00000000-0000-0000-0000-000000000000",
    file_name="xero-dev.jpg",
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
res = await client.credit_notes.attachments.get_by_filename(
    content_type="image/jpg",
    credit_note_id="00000000-0000-0000-0000-000000000000",
    file_name="xero-dev.jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Updates attachments on a specific credit note by file name <a name="update_by_filename"></a>

**API Endpoint**: `POST /CreditNotes/{CreditNoteID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                         | Example                                  |
| ---------------- | :------: | ----------------------------------- | ---------------------------------------- |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note | `"00000000-0000-0000-0000-000000000000"` |
| `data`           |    ✓     |                                     | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment              | `"xero-dev.jpg"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant          | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.credit_notes.attachments.update_by_filename(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    data="string",
    file_name="xero-dev.jpg",
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
res = await client.credit_notes.attachments.update_by_filename(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    data="string",
    file_name="xero-dev.jpg",
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

### Creates an attachment for a specific credit note <a name="create_by_filename"></a>

**API Endpoint**: `PUT /CreditNotes/{CreditNoteID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                                                                     | Example                                  |
| ---------------- | :------: | ------------------------------------------------------------------------------- | ---------------------------------------- |
| `credit_note_id` |    ✓     | Unique identifier for a Credit Note                                             | `"00000000-0000-0000-0000-000000000000"` |
| `data`           |    ✓     |                                                                                 | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment                                                          | `"xero-dev.jpg"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                      | `"YOUR_XERO_TENANT_ID"`                  |
| `include_online` |    ✗     | Allows an attachment to be seen by the end customer within their online invoice | `True`                                   |

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
res = client.credit_notes.attachments.create_by_filename(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    data="string",
    file_name="xero-dev.jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    include_online=True,
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
res = await client.credit_notes.attachments.create_by_filename(
    credit_note_id="00000000-0000-0000-0000-000000000000",
    data="string",
    file_name="xero-dev.jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    include_online=True,
)
```

#### Response

##### Type

[Attachments](/xero_accounting_py/types/models/attachments.py)

##### Example

```python
{}
```

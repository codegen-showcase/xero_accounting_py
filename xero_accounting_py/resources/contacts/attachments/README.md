# contacts.attachments

## Module Functions

### Retrieves attachments for a specific contact in a Xero organisation <a name="list"></a>

**API Endpoint**: `GET /Contacts/{ContactID}/Attachments`

#### Parameters

| Parameter        | Required | Description                     | Example                                  |
| ---------------- | :------: | ------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant      | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.contacts.attachments.list(
    contact_id="00000000-0000-0000-0000-000000000000",
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
res = await client.contacts.attachments.list(
    contact_id="00000000-0000-0000-0000-000000000000",
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

### Retrieves a specific attachment from a specific contact using a unique attachment Id <a name="get_by_id"></a>

**API Endpoint**: `GET /Contacts/{ContactID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`  |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `contact_id`     |    ✓     | Unique identifier for a Contact                                                        | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`   |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
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
res = client.contacts.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    contact_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
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
res = await client.contacts.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    contact_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves a specific attachment from a specific contact by file name <a name="get_by_filename"></a>

**API Endpoint**: `GET /Contacts/{ContactID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact                                                        | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`   |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
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
res = client.contacts.attachments.get_by_filename(
    contact_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
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
res = await client.contacts.attachments.get_by_filename(
    contact_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    file_name="xero-dev.jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### POST /Contacts/{ContactID}/Attachments/{FileName} <a name="update_by_filename"></a>

**API Endpoint**: `POST /Contacts/{ContactID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                     | Example                                  |
| ---------------- | :------: | ------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact | `"00000000-0000-0000-0000-000000000000"` |
| `data`           |    ✓     |                                 | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment          | `"xero-dev.jpg"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant      | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.contacts.attachments.update_by_filename(
    contact_id="00000000-0000-0000-0000-000000000000",
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
res = await client.contacts.attachments.update_by_filename(
    contact_id="00000000-0000-0000-0000-000000000000",
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

### PUT /Contacts/{ContactID}/Attachments/{FileName} <a name="create_by_filename"></a>

**API Endpoint**: `PUT /Contacts/{ContactID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                     | Example                                  |
| ---------------- | :------: | ------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact | `"00000000-0000-0000-0000-000000000000"` |
| `data`           |    ✓     |                                 | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment          | `"xero-dev.jpg"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant      | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.contacts.attachments.create_by_filename(
    contact_id="00000000-0000-0000-0000-000000000000",
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
res = await client.contacts.attachments.create_by_filename(
    contact_id="00000000-0000-0000-0000-000000000000",
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

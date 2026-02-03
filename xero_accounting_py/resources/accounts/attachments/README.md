# accounts.attachments

## Module Functions

### Retrieves attachments for a specific accounts by using a unique account Id <a name="list"></a>

**API Endpoint**: `GET /Accounts/{AccountID}/Attachments`

#### Parameters

| Parameter        | Required | Description                          | Example                                  |
| ---------------- | :------: | ------------------------------------ | ---------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.accounts.attachments.list(
    account_id="00000000-0000-0000-0000-000000000000",
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
res = await client.accounts.attachments.list(
    account_id="00000000-0000-0000-0000-000000000000",
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

### Retrieves a specific attachment from a specific account using a unique attachment Id <a name="get_by_id"></a>

**API Endpoint**: `GET /Accounts/{AccountID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object                                                   | `"00000000-0000-0000-0000-000000000000"` |
| `attachment_id`  |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
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
res = client.accounts.attachments.get_by_id(
    account_id="00000000-0000-0000-0000-000000000000",
    attachment_id="00000000-0000-0000-0000-000000000000",
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
res = await client.accounts.attachments.get_by_id(
    account_id="00000000-0000-0000-0000-000000000000",
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves an attachment for a specific account by filename <a name="get_by_filename"></a>

**API Endpoint**: `GET /Accounts/{AccountID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object                                                   | `"00000000-0000-0000-0000-000000000000"` |
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
res = client.accounts.attachments.get_by_filename(
    account_id="00000000-0000-0000-0000-000000000000",
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
res = await client.accounts.attachments.get_by_filename(
    account_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    file_name="xero-dev.jpg",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Updates attachment on a specific account by filename <a name="update_by_filename"></a>

**API Endpoint**: `POST /Accounts/{AccountID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                          | Example                                  |
| ---------------- | :------: | ------------------------------------ | ---------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object | `"00000000-0000-0000-0000-000000000000"` |
| `data`           |    ✓     |                                      | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment               | `"xero-dev.jpg"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.accounts.attachments.update_by_filename(
    account_id="00000000-0000-0000-0000-000000000000",
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
res = await client.accounts.attachments.update_by_filename(
    account_id="00000000-0000-0000-0000-000000000000",
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

### Creates an attachment on a specific account <a name="create_by_filename"></a>

**API Endpoint**: `PUT /Accounts/{AccountID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                          | Example                                  |
| ---------------- | :------: | ------------------------------------ | ---------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object | `"00000000-0000-0000-0000-000000000000"` |
| `data`           |    ✓     |                                      | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment               | `"xero-dev.jpg"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.accounts.attachments.create_by_filename(
    account_id="00000000-0000-0000-0000-000000000000",
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
res = await client.accounts.attachments.create_by_filename(
    account_id="00000000-0000-0000-0000-000000000000",
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

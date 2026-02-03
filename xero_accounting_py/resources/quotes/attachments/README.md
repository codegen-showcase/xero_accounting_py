# quotes.attachments

## Module Functions

### Retrieves attachments for a specific quote <a name="list"></a>

**API Endpoint**: `GET /Quotes/{QuoteID}/Attachments`

#### Parameters

| Parameter        | Required | Description                    | Example                                  |
| ---------------- | :------: | ------------------------------ | ---------------------------------------- |
| `quote_id`       |    ✓     | Unique identifier for an Quote | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant     | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.quotes.attachments.list(
    quote_id="00000000-0000-0000-0000-000000000000",
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
res = await client.quotes.attachments.list(
    quote_id="00000000-0000-0000-0000-000000000000",
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

### Retrieves a specific attachment from a specific quote using a unique attachment Id <a name="get_by_id"></a>

**API Endpoint**: `GET /Quotes/{QuoteID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`  |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`   |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `quote_id`       |    ✓     | Unique identifier for an Quote                                                         | `"00000000-0000-0000-0000-000000000000"` |
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
res = client.quotes.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
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
res = await client.quotes.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves a specific attachment from a specific quote by filename <a name="get_by_filename"></a>

**API Endpoint**: `GET /Quotes/{QuoteID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `content_type`   |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `file_name`      |    ✓     | Name of the attachment                                                                 | `"xero-dev.jpg"`                         |
| `quote_id`       |    ✓     | Unique identifier for an Quote                                                         | `"00000000-0000-0000-0000-000000000000"` |
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
res = client.quotes.attachments.get_by_filename(
    content_type="image/jpg",
    file_name="xero-dev.jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
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
res = await client.quotes.attachments.get_by_filename(
    content_type="image/jpg",
    file_name="xero-dev.jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Updates a specific attachment from a specific quote by filename <a name="update_by_filename"></a>

**API Endpoint**: `POST /Quotes/{QuoteID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                    | Example                                  |
| ---------------- | :------: | ------------------------------ | ---------------------------------------- |
| `data`           |    ✓     |                                | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment         | `"xero-dev.jpg"`                         |
| `quote_id`       |    ✓     | Unique identifier for an Quote | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant     | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.quotes.attachments.update_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
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
res = await client.quotes.attachments.update_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
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

### Creates attachment for a specific quote <a name="create_by_filename"></a>

**API Endpoint**: `PUT /Quotes/{QuoteID}/Attachments/{FileName}`

#### Parameters

| Parameter        | Required | Description                    | Example                                  |
| ---------------- | :------: | ------------------------------ | ---------------------------------------- |
| `data`           |    ✓     |                                | `"string"`                               |
| `file_name`      |    ✓     | Name of the attachment         | `"xero-dev.jpg"`                         |
| `quote_id`       |    ✓     | Unique identifier for an Quote | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant     | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.quotes.attachments.create_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
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
res = await client.quotes.attachments.create_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    quote_id="00000000-0000-0000-0000-000000000000",
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

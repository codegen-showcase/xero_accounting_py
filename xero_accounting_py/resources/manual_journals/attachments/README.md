# manual_journals.attachments

## Module Functions

### Retrieves attachment for a specific manual journal <a name="list"></a>

**API Endpoint**: `GET /ManualJournals/{ManualJournalID}/Attachments`

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
res = client.manual_journals.attachments.list(
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
res = await client.manual_journals.attachments.list(
    manual_journal_id="00000000-0000-0000-0000-000000000000",
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

### Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id <a name="get_by_id"></a>

**API Endpoint**: `GET /ManualJournals/{ManualJournalID}/Attachments/{AttachmentID}`

#### Parameters

| Parameter           | Required | Description                                                                            | Example                                  |
| ------------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `attachment_id`     |    ✓     | Unique identifier for Attachment object                                                | `"00000000-0000-0000-0000-000000000000"` |
| `content_type`      |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `manual_journal_id` |    ✓     | Unique identifier for a ManualJournal                                                  | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.manual_journals.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
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
res = await client.manual_journals.attachments.get_by_id(
    attachment_id="00000000-0000-0000-0000-000000000000",
    content_type="image/jpg",
    manual_journal_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves a specific attachment from a specific manual journal by file name <a name="get_by_filename"></a>

**API Endpoint**: `GET /ManualJournals/{ManualJournalID}/Attachments/{FileName}`

#### Parameters

| Parameter           | Required | Description                                                                            | Example                                  |
| ------------------- | :------: | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| `content_type`      |    ✓     | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | `"image/jpg"`                            |
| `file_name`         |    ✓     | Name of the attachment                                                                 | `"xero-dev.jpg"`                         |
| `manual_journal_id` |    ✓     | Unique identifier for a ManualJournal                                                  | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                                                             | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.manual_journals.attachments.get_by_filename(
    content_type="image/jpg",
    file_name="xero-dev.jpg",
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
res = await client.manual_journals.attachments.get_by_filename(
    content_type="image/jpg",
    file_name="xero-dev.jpg",
    manual_journal_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Updates a specific attachment from a specific manual journal by file name <a name="update_by_filename"></a>

**API Endpoint**: `POST /ManualJournals/{ManualJournalID}/Attachments/{FileName}`

#### Parameters

| Parameter           | Required | Description                           | Example                                  |
| ------------------- | :------: | ------------------------------------- | ---------------------------------------- |
| `data`              |    ✓     |                                       | `"string"`                               |
| `file_name`         |    ✓     | Name of the attachment                | `"xero-dev.jpg"`                         |
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
res = client.manual_journals.attachments.update_by_filename(
    data="string",
    file_name="xero-dev.jpg",
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
res = await client.manual_journals.attachments.update_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    manual_journal_id="00000000-0000-0000-0000-000000000000",
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

### Creates a specific attachment for a specific manual journal by file name <a name="create_by_filename"></a>

**API Endpoint**: `PUT /ManualJournals/{ManualJournalID}/Attachments/{FileName}`

#### Parameters

| Parameter           | Required | Description                           | Example                                  |
| ------------------- | :------: | ------------------------------------- | ---------------------------------------- |
| `data`              |    ✓     |                                       | `"string"`                               |
| `file_name`         |    ✓     | Name of the attachment                | `"xero-dev.jpg"`                         |
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
res = client.manual_journals.attachments.create_by_filename(
    data="string",
    file_name="xero-dev.jpg",
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
res = await client.manual_journals.attachments.create_by_filename(
    data="string",
    file_name="xero-dev.jpg",
    manual_journal_id="00000000-0000-0000-0000-000000000000",
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

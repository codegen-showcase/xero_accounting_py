# contact_groups.contacts

## Module Functions

### Deletes all contacts from a specific contact group <a name="delete_all"></a>

**API Endpoint**: `DELETE /ContactGroups/{ContactGroupID}/Contacts`

#### Parameters

| Parameter          | Required | Description                           | Example                                  |
| ------------------ | :------: | ------------------------------------- | ---------------------------------------- |
| `contact_group_id` |    ✓     | Unique identifier for a Contact Group | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant            | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.contact_groups.contacts.delete_all(
    contact_group_id="00000000-0000-0000-0000-000000000000",
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
res = await client.contact_groups.contacts.delete_all(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Deletes a specific contact from a contact group using a unique contact Id <a name="delete"></a>

**API Endpoint**: `DELETE /ContactGroups/{ContactGroupID}/Contacts/{ContactID}`

#### Parameters

| Parameter          | Required | Description                           | Example                                  |
| ------------------ | :------: | ------------------------------------- | ---------------------------------------- |
| `contact_group_id` |    ✓     | Unique identifier for a Contact Group | `"00000000-0000-0000-0000-000000000000"` |
| `contact_id`       |    ✓     | Unique identifier for a Contact       | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant            | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.contact_groups.contacts.delete(
    contact_group_id="00000000-0000-0000-0000-000000000000",
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
res = await client.contact_groups.contacts.delete(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Creates contacts to a specific contact group <a name="create"></a>

**API Endpoint**: `PUT /ContactGroups/{ContactGroupID}/Contacts`

#### Parameters

| Parameter          | Required | Description                                     | Example                                  |
| ------------------ | :------: | ----------------------------------------------- | ---------------------------------------- |
| `contact_group_id` |    ✓     | Unique identifier for a Contact Group           | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                      | `"YOUR_XERO_TENANT_ID"`                  |
| `contacts`         |    ✗     |                                                 | `[]`                                     |
| `pagination`       |    ✗     |                                                 | `{}`                                     |
| `└─ item_count`    |    ✗     |                                                 | `123`                                    |
| `└─ page`          |    ✗     |                                                 | `123`                                    |
| `└─ page_count`    |    ✗     |                                                 | `123`                                    |
| `└─ page_size`     |    ✗     |                                                 | `123`                                    |
| `warnings`         |    ✗     | Displays array of warning messages from the API | `[{}]`                                   |

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
res = client.contact_groups.contacts.create(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[
        {"contact_id": "a3675fc4-f8dd-4f03-ba5b-f1870566bcd7"},
        {"contact_id": "4e1753b9-018a-4775-b6aa-1bc7871cfee3"},
    ],
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
res = await client.contact_groups.contacts.create(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[
        {"contact_id": "a3675fc4-f8dd-4f03-ba5b-f1870566bcd7"},
        {"contact_id": "4e1753b9-018a-4775-b6aa-1bc7871cfee3"},
    ],
)
```

#### Response

##### Type

[Contacts](/xero_accounting_py/types/models/contacts.py)

##### Example

```python
{}
```

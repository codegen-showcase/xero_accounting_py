# contact_groups

## Module Functions

### Retrieves the contact Id and name of each contact group <a name="list"></a>

**API Endpoint**: `GET /ContactGroups`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element    | `"Name ASC"`            |
| `where`          |    ✗     | Filter by an any element   | `"Status==\"ACTIVE\""`  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contact_groups.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.contact_groups.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
)
```

#### Response

##### Type

[ContactGroups](/xero_accounting_py/types/models/contact_groups.py)

##### Example

```python
{}
```

### Retrieves a specific contact group by using a unique contact group Id <a name="get"></a>

**API Endpoint**: `GET /ContactGroups/{ContactGroupID}`

#### Parameters

| Parameter          | Required | Description                           | Example                                  |
| ------------------ | :------: | ------------------------------------- | ---------------------------------------- |
| `contact_group_id` |    ✓     | Unique identifier for a Contact Group | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant            | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contact_groups.get(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.contact_groups.get(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[ContactGroups](/xero_accounting_py/types/models/contact_groups.py)

##### Example

```python
{}
```

### Updates a specific contact group <a name="update"></a>

**API Endpoint**: `POST /ContactGroups/{ContactGroupID}`

#### Parameters

| Parameter          | Required | Description                           | Example                                  |
| ------------------ | :------: | ------------------------------------- | ---------------------------------------- |
| `contact_group_id` |    ✓     | Unique identifier for a Contact Group | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant            | `"YOUR_XERO_TENANT_ID"`                  |
| `contact_groups`   |    ✗     |                                       | `[]`                                     |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contact_groups.update(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contact_groups=[{"name": "Suppliers"}],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.contact_groups.update(
    contact_group_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contact_groups=[{"name": "Suppliers"}],
)
```

#### Response

##### Type

[ContactGroups](/xero_accounting_py/types/models/contact_groups.py)

##### Example

```python
{}
```

### Creates a contact group <a name="create"></a>

**API Endpoint**: `PUT /ContactGroups`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `contact_groups` |    ✗     |                            | `[]`                    |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contact_groups.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", contact_groups=[{"name": "VIPs"}]
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.contact_groups.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", contact_groups=[{"name": "VIPs"}]
)
```

#### Response

##### Type

[ContactGroups](/xero_accounting_py/types/models/contact_groups.py)

##### Example

```python
{}
```

## Submodules

- [contacts](contacts/README.md) - contacts

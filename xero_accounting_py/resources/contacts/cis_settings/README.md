# contacts.cis_settings

## Module Functions

### Retrieves CIS settings for a specific contact in a Xero organisation <a name="list"></a>

**API Endpoint**: `GET /Contacts/{ContactID}/CISSettings`

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
res = client.contacts.cis_settings.list(
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
res = await client.contacts.cis_settings.list(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[CisSettings](/xero_accounting_py/types/models/cis_settings.py)

##### Example

```python
{}
```

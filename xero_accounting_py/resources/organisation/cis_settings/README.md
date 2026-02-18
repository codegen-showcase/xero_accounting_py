# organisation.cis_settings

## Module Functions

### Retrieves the CIS settings for the Xero organistaion. <a name="list"></a>

**API Endpoint**: `GET /Organisation/{OrganisationID}/CISSettings`

#### Parameters

| Parameter         | Required | Description                                    | Example                                  |
| ----------------- | :------: | ---------------------------------------------- | ---------------------------------------- |
| `organisation_id` |    ✓     | The unique Xero identifier for an organisation | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant                     | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.organisation.cis_settings.list(
    organisation_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.organisation.cis_settings.list(
    organisation_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[CisOrgSettings](/xero_accounting_py/types/models/cis_org_settings.py)

##### Example

```python
{}
```

# branding_themes

## Module Functions

### Retrieves all the branding themes <a name="list"></a>

**API Endpoint**: `GET /BrandingThemes`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |

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
res = client.branding_themes.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
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
res = await client.branding_themes.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Response

##### Type

[BrandingThemes](/xero_accounting_py/types/models/branding_themes.py)

##### Example

```python
{}
```

### Retrieves a specific branding theme using a unique branding theme Id <a name="get"></a>

**API Endpoint**: `GET /BrandingThemes/{BrandingThemeID}`

#### Parameters

| Parameter           | Required | Description                            | Example                                  |
| ------------------- | :------: | -------------------------------------- | ---------------------------------------- |
| `branding_theme_id` |    ✓     | Unique identifier for a Branding Theme | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant             | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.branding_themes.get(
    branding_theme_id="00000000-0000-0000-0000-000000000000",
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
res = await client.branding_themes.get(
    branding_theme_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[BrandingThemes](/xero_accounting_py/types/models/branding_themes.py)

##### Example

```python
{}
```

## Submodules

- [payment_services](payment_services/README.md) - payment_services

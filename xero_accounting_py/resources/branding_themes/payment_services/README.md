# branding_themes.payment_services

## Module Functions

### Retrieves the payment services for a specific branding theme <a name="list"></a>

**API Endpoint**: `GET /BrandingThemes/{BrandingThemeID}/PaymentServices`

#### Parameters

| Parameter           | Required | Description                            | Example                                  |
| ------------------- | :------: | -------------------------------------- | ---------------------------------------- |
| `branding_theme_id` |    ✓     | Unique identifier for a Branding Theme | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant             | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.branding_themes.payment_services.list(
    branding_theme_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.branding_themes.payment_services.list(
    branding_theme_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[PaymentServices](/xero_accounting_py/types/models/payment_services.py)

##### Example

```python
{}
```

### Creates a new custom payment service for a specific branding theme <a name="create"></a>

**API Endpoint**: `POST /BrandingThemes/{BrandingThemeID}/PaymentServices`

#### Parameters

| Parameter           | Required | Description                            | Example                                  |
| ------------------- | :------: | -------------------------------------- | ---------------------------------------- |
| `branding_theme_id` |    ✓     | Unique identifier for a Branding Theme | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant             | `"YOUR_XERO_TENANT_ID"`                  |
| `payment_services`  |    ✗     |                                        | `[{}]`                                   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.branding_themes.payment_services.create(
    branding_theme_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    payment_services=[
        {
            "pay_now_text": "Time To Pay",
            "payment_service_id": "54b3b4f6-0443-4fba-bcd1-61ec0c35ca55",
            "payment_service_name": "PayUpNow",
            "payment_service_type": "Custom",
            "payment_service_url": "https://www.payupnow.com/",
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.branding_themes.payment_services.create(
    branding_theme_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    payment_services=[
        {
            "pay_now_text": "Time To Pay",
            "payment_service_id": "54b3b4f6-0443-4fba-bcd1-61ec0c35ca55",
            "payment_service_name": "PayUpNow",
            "payment_service_type": "Custom",
            "payment_service_url": "https://www.payupnow.com/",
        }
    ],
)
```

#### Response

##### Type

[PaymentServices](/xero_accounting_py/types/models/payment_services.py)

##### Example

```python
{}
```

# payment_services

## Module Functions

### Retrieves payment services <a name="list"></a>

**API Endpoint**: `GET /PaymentServices`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.payment_services.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.payment_services.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Response

##### Type

[PaymentServices](/xero_accounting_py/types/models/payment_services.py)

##### Example

```python
{}
```

### Creates a payment service <a name="create"></a>

**API Endpoint**: `PUT /PaymentServices`

#### Parameters

| Parameter          | Required | Description                | Example                 |
| ------------------ | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `payment_services` |    ✗     |                            | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.payment_services.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    payment_services=[
        {
            "pay_now_text": "Time To Pay",
            "payment_service_name": "PayUpNow",
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
res = await client.payment_services.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    payment_services=[
        {
            "pay_now_text": "Time To Pay",
            "payment_service_name": "PayUpNow",
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

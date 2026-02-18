# tax_rates

## Module Functions

### Retrieves tax rates <a name="list"></a>

**API Endpoint**: `GET /TaxRates`

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
res = client.tax_rates.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.tax_rates.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
)
```

#### Response

##### Type

[TaxRates](/xero_accounting_py/types/models/tax_rates.py)

##### Example

```python
{}
```

### Retrieves a specific tax rate according to given TaxType code <a name="get"></a>

**API Endpoint**: `GET /TaxRates/{TaxType}`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `tax_type`       |    ✓     | A valid TaxType code       | `"INPUT2"`              |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.tax_rates.get(tax_type="INPUT2", xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.tax_rates.get(
    tax_type="INPUT2", xero_tenant_id="YOUR_XERO_TENANT_ID"
)
```

#### Response

##### Type

[TaxRates](/xero_accounting_py/types/models/tax_rates.py)

##### Example

```python
{}
```

### Updates tax rates <a name="update"></a>

**API Endpoint**: `POST /TaxRates`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `tax_rates`      |    ✗     |                            | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.tax_rates.update(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    tax_rates=[
        {
            "name": "State Tax NY",
            "report_tax_type": "INPUT",
            "status": "DELETED",
            "tax_components": [{"name": "State Tax", "rate": 2.25}],
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.tax_rates.update(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    tax_rates=[
        {
            "name": "State Tax NY",
            "report_tax_type": "INPUT",
            "status": "DELETED",
            "tax_components": [{"name": "State Tax", "rate": 2.25}],
        }
    ],
)
```

#### Response

##### Type

[TaxRates](/xero_accounting_py/types/models/tax_rates.py)

##### Example

```python
{}
```

### Creates one or more tax rates <a name="create"></a>

**API Endpoint**: `PUT /TaxRates`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `tax_rates`      |    ✗     |                            | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.tax_rates.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    tax_rates=[
        {
            "name": "CA State Tax",
            "tax_components": [{"name": "State Tax", "rate": 2.25}],
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.tax_rates.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    tax_rates=[
        {
            "name": "CA State Tax",
            "tax_components": [{"name": "State Tax", "rate": 2.25}],
        }
    ],
)
```

#### Response

##### Type

[TaxRates](/xero_accounting_py/types/models/tax_rates.py)

##### Example

```python
{}
```

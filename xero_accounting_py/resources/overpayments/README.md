# overpayments

## Module Functions

### Retrieves overpayments <a name="list"></a>

**API Endpoint**: `GET /Overpayments`

#### Parameters

| Parameter        | Required | Description                                                                                                           | Example                    |
| ---------------- | :------: | --------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                            | `"YOUR_XERO_TENANT_ID"`    |
| `order`          |    ✗     | Order by an any element                                                                                               | `"Status ASC"`             |
| `page`           |    ✗     | e.g. page=1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment | `1`                        |
| `page_size`      |    ✗     | Number of records to retrieve per page                                                                                | `100`                      |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts                      | `4`                        |
| `where`          |    ✗     | Filter by an any element                                                                                              | `"Status==\"AUTHORISED\""` |

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
res = client.overpayments.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Status ASC",
    page=1,
    page_size=100,
    unitdp=4,
    where='Status=="AUTHORISED"',
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
res = await client.overpayments.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Status ASC",
    page=1,
    page_size=100,
    unitdp=4,
    where='Status=="AUTHORISED"',
)
```

#### Response

##### Type

[Overpayments](/xero_accounting_py/types/models/overpayments.py)

##### Example

```python
{}
```

### Retrieves a specific overpayment using a unique overpayment Id <a name="get"></a>

**API Endpoint**: `GET /Overpayments/{OverpaymentID}`

#### Parameters

| Parameter        | Required | Description                         | Example                                  |
| ---------------- | :------: | ----------------------------------- | ---------------------------------------- |
| `overpayment_id` |    ✓     | Unique identifier for a Overpayment | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant          | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.overpayments.get(
    overpayment_id="00000000-0000-0000-0000-000000000000",
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
res = await client.overpayments.get(
    overpayment_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Overpayments](/xero_accounting_py/types/models/overpayments.py)

##### Example

```python
{}
```

## Submodules

- [allocations](allocations/README.md) - allocations
- [history](history/README.md) - history

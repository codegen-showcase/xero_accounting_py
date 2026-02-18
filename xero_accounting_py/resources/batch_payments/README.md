# batch_payments

## Module Functions

### Retrieves either one or many batch payments for invoices <a name="list"></a>

**API Endpoint**: `GET /BatchPayments`

#### Parameters

| Parameter        | Required | Description                | Example                    |
| ---------------- | :------: | -------------------------- | -------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"`    |
| `order`          |    ✗     | Order by an any element    | `"Date ASC"`               |
| `where`          |    ✗     | Filter by an any element   | `"Status==\"AUTHORISED\""` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.batch_payments.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Date ASC", where='Status=="AUTHORISED"'
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.batch_payments.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Date ASC", where='Status=="AUTHORISED"'
)
```

#### Response

##### Type

[BatchPayments](/xero_accounting_py/types/models/batch_payments.py)

##### Example

```python
{}
```

### Retrieves a specific batch payment using a unique batch payment Id <a name="get"></a>

**API Endpoint**: `GET /BatchPayments/{BatchPaymentID}`

#### Parameters

| Parameter          | Required | Description                        | Example                                  |
| ------------------ | :------: | ---------------------------------- | ---------------------------------------- |
| `batch_payment_id` |    ✓     | Unique identifier for BatchPayment | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant         | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.batch_payments.get(
    batch_payment_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.batch_payments.get(
    batch_payment_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[BatchPayments](/xero_accounting_py/types/models/batch_payments.py)

##### Example

```python
{}
```

### Updates a specific batch payment for invoices and credit notes <a name="delete"></a>

**API Endpoint**: `POST /BatchPayments`

#### Parameters

| Parameter          | Required | Description                                                               | Example                                  |
| ------------------ | :------: | ------------------------------------------------------------------------- | ---------------------------------------- |
| `batch_payment_id` |    ✓     | The Xero generated unique identifier for the bank transaction (read-only) | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `status`           |    ✓     | The status of the batch payment.                                          | `"string"`                               |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.batch_payments.delete(
    batch_payment_id="9bf296e9-0748-4d29-a3dc-24dde1098030",
    status="DELETED",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.batch_payments.delete(
    batch_payment_id="9bf296e9-0748-4d29-a3dc-24dde1098030",
    status="DELETED",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[BatchPayments](/xero_accounting_py/types/models/batch_payments.py)

##### Example

```python
{}
```

### Updates a specific batch payment for invoices and credit notes <a name="update"></a>

**API Endpoint**: `POST /BatchPayments/{BatchPaymentID}`

#### Parameters

| Parameter          | Required | Description                        | Example                                  |
| ------------------ | :------: | ---------------------------------- | ---------------------------------------- |
| `batch_payment_id` |    ✓     | Unique identifier for BatchPayment | `"00000000-0000-0000-0000-000000000000"` |
| `status`           |    ✓     | The status of the batch payment.   | `"string"`                               |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant         | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.batch_payments.update(
    batch_payment_id="00000000-0000-0000-0000-000000000000",
    status="DELETED",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.batch_payments.update(
    batch_payment_id="00000000-0000-0000-0000-000000000000",
    status="DELETED",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[BatchPayments](/xero_accounting_py/types/models/batch_payments.py)

##### Example

```python
{}
```

### Creates one or many batch payments for invoices <a name="create"></a>

**API Endpoint**: `PUT /BatchPayments`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                 |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `batch_payments`   |    ✗     |                                                                                               | `[]`                    |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.batch_payments.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    batch_payments=[
        {
            "account": {"account_id": "00000000-0000-0000-0000-000000000000"},
            "date": "2018-08-01",
            "reference": "ref",
        }
    ],
    summarize_errors=True,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.batch_payments.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    batch_payments=[
        {
            "account": {"account_id": "00000000-0000-0000-0000-000000000000"},
            "date": "2018-08-01",
            "reference": "ref",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[BatchPayments](/xero_accounting_py/types/models/batch_payments.py)

##### Example

```python
{}
```

## Submodules

- [history](history/README.md) - history

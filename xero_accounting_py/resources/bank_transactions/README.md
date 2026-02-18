# bank_transactions

## Module Functions

### Retrieves any spent or received money transactions <a name="list"></a>

**API Endpoint**: `GET /BankTransactions`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                    |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | -------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`    |
| `order`          |    ✗     | Order by an any element                                                                          | `"Type ASC"`               |
| `page`           |    ✗     | Up to 100 bank transactions will be returned in a single API call with line items details        | `1`                        |
| `page_size`      |    ✗     | Number of records to retrieve per page                                                           | `100`                      |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                        |
| `where`          |    ✗     | Filter by an any element                                                                         | `"Status==\"AUTHORISED\""` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transactions.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Type ASC",
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

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transactions.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Type ASC",
    page=1,
    page_size=100,
    unitdp=4,
    where='Status=="AUTHORISED"',
)
```

#### Response

##### Type

[BankTransactions](/xero_accounting_py/types/models/bank_transactions.py)

##### Example

```python
{}
```

### Retrieves a single spent or received money transaction by using a unique bank transaction Id <a name="get"></a>

**API Endpoint**: `GET /BankTransactions/{BankTransactionID}`

#### Parameters

| Parameter             | Required | Description                                                                                      | Example                                  |
| --------------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `bank_transaction_id` |    ✓     | Xero generated unique identifier for a bank transaction                                          | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`      |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `unitdp`              |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transactions.get(
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transactions.get(
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Response

##### Type

[BankTransactions](/xero_accounting_py/types/models/bank_transactions.py)

##### Example

```python
{}
```

### Updates or creates one or more spent or received money transaction <a name="update_or_create"></a>

**API Endpoint**: `POST /BankTransactions`

#### Parameters

| Parameter           | Required | Description                                                                                      | Example                 |
| ------------------- | :------: | ------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"` |
| `bank_transactions` |    ✗     |                                                                                                  | `[]`                    |
| `pagination`        |    ✗     |                                                                                                  | `{}`                    |
| `└─ item_count`     |    ✗     |                                                                                                  | `123`                   |
| `└─ page`           |    ✗     |                                                                                                  | `123`                   |
| `└─ page_count`     |    ✗     |                                                                                                  | `123`                   |
| `└─ page_size`      |    ✗     |                                                                                                  | `123`                   |
| `summarize_errors`  |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors    | `True`                  |
| `unitdp`            |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                     |
| `warnings`          |    ✗     | Displays array of warning messages from the API                                                  | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transactions.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    bank_transactions=[
        {
            "bank_account": {"code": "088"},
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
            "type_": "SPEND",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transactions.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    bank_transactions=[
        {
            "bank_account": {"code": "088"},
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
            "type_": "SPEND",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Response

##### Type

[BankTransactions](/xero_accounting_py/types/models/bank_transactions.py)

##### Example

```python
{}
```

### Updates a single spent or received money transaction <a name="update"></a>

**API Endpoint**: `POST /BankTransactions/{BankTransactionID}`

#### Parameters

| Parameter             | Required | Description                                                                                      | Example                                  |
| --------------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `bank_transaction_id` |    ✓     | Xero generated unique identifier for a bank transaction                                          | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`      |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `bank_transactions`   |    ✗     |                                                                                                  | `[]`                                     |
| `pagination`          |    ✗     |                                                                                                  | `{}`                                     |
| `└─ item_count`       |    ✗     |                                                                                                  | `123`                                    |
| `└─ page`             |    ✗     |                                                                                                  | `123`                                    |
| `└─ page_count`       |    ✗     |                                                                                                  | `123`                                    |
| `└─ page_size`        |    ✗     |                                                                                                  | `123`                                    |
| `unitdp`              |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |
| `warnings`            |    ✗     | Displays array of warning messages from the API                                                  | `[{}]`                                   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transactions.update(
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    bank_transactions=[
        {
            "bank_account": {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "code": "088",
                "name": "Business Wells Fargo",
            },
            "bank_transaction_id": "00000000-0000-0000-0000-000000000000",
            "currency_code": "USD",
            "currency_rate": 1.0,
            "date": "2019-02-25",
            "is_reconciled": False,
            "line_amount_types": "Inclusive",
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
            "reference": "You just updated",
            "status": "AUTHORISED",
            "total_tax": 1.74,
            "type_": "SPEND",
            "updated_date_utc": "2019-02-26T12:39:27.813-08:00",
        }
    ],
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transactions.update(
    bank_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    bank_transactions=[
        {
            "bank_account": {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "code": "088",
                "name": "Business Wells Fargo",
            },
            "bank_transaction_id": "00000000-0000-0000-0000-000000000000",
            "currency_code": "USD",
            "currency_rate": 1.0,
            "date": "2019-02-25",
            "is_reconciled": False,
            "line_amount_types": "Inclusive",
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
            "reference": "You just updated",
            "status": "AUTHORISED",
            "total_tax": 1.74,
            "type_": "SPEND",
            "updated_date_utc": "2019-02-26T12:39:27.813-08:00",
        }
    ],
    unitdp=4,
)
```

#### Response

##### Type

[BankTransactions](/xero_accounting_py/types/models/bank_transactions.py)

##### Example

```python
{}
```

### Creates one or more spent or received money transaction <a name="create"></a>

**API Endpoint**: `PUT /BankTransactions`

#### Parameters

| Parameter           | Required | Description                                                                                      | Example                 |
| ------------------- | :------: | ------------------------------------------------------------------------------------------------ | ----------------------- |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"` |
| `bank_transactions` |    ✗     |                                                                                                  | `[]`                    |
| `pagination`        |    ✗     |                                                                                                  | `{}`                    |
| `└─ item_count`     |    ✗     |                                                                                                  | `123`                   |
| `└─ page`           |    ✗     |                                                                                                  | `123`                   |
| `└─ page_count`     |    ✗     |                                                                                                  | `123`                   |
| `└─ page_size`      |    ✗     |                                                                                                  | `123`                   |
| `summarize_errors`  |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors    | `True`                  |
| `unitdp`            |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                     |
| `warnings`          |    ✗     | Displays array of warning messages from the API                                                  | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transactions.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True, unitdp=4
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transactions.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True, unitdp=4
)
```

#### Response

##### Type

[BankTransactions](/xero_accounting_py/types/models/bank_transactions.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history

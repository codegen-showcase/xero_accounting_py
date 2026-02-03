# linked_transactions

## Module Functions

### Deletes a specific linked transactions (billable expenses) <a name="delete"></a>

**API Endpoint**: `DELETE /LinkedTransactions/{LinkedTransactionID}`

#### Parameters

| Parameter               | Required | Description                               | Example                                  |
| ----------------------- | :------: | ----------------------------------------- | ---------------------------------------- |
| `linked_transaction_id` |    ✓     | Unique identifier for a LinkedTransaction | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`        |    ✓     | Xero identifier for Tenant                | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.linked_transactions.delete(
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
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
res = await client.linked_transactions.delete(
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

### Retrieves linked transactions (billable expenses) <a name="list"></a>

**API Endpoint**: `GET /LinkedTransactions`

#### Parameters

| Parameter               | Required | Description                                                                                                                                 | Example                                  |
| ----------------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `xero_tenant_id`        |    ✓     | Xero identifier for Tenant                                                                                                                  | `"YOUR_XERO_TENANT_ID"`                  |
| `contact_id`            |    ✗     | Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer.                                  | `"00000000-0000-0000-0000-000000000000"` |
| `linked_transaction_id` |    ✗     | The Xero identifier for an Linked Transaction                                                                                               | `"00000000-0000-0000-0000-000000000000"` |
| `page`                  |    ✗     | Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page=1. | `1`                                      |
| `source_transaction_id` |    ✗     | Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice                                     | `"00000000-0000-0000-0000-000000000000"` |
| `status`                |    ✗     | Filter by the combination of ContactID and Status. Get the linked transactions associated to a customer and with a status                   | `"APPROVED"`                             |
| `target_transaction_id` |    ✗     | Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice                                 | `"00000000-0000-0000-0000-000000000000"` |

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
res = client.linked_transactions.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contact_id="00000000-0000-0000-0000-000000000000",
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
    page=1,
    source_transaction_id="00000000-0000-0000-0000-000000000000",
    status="APPROVED",
    target_transaction_id="00000000-0000-0000-0000-000000000000",
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
res = await client.linked_transactions.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contact_id="00000000-0000-0000-0000-000000000000",
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
    page=1,
    source_transaction_id="00000000-0000-0000-0000-000000000000",
    status="APPROVED",
    target_transaction_id="00000000-0000-0000-0000-000000000000",
)
```

#### Response

##### Type

[LinkedTransactions](/xero_accounting_py/types/models/linked_transactions.py)

##### Example

```python
{}
```

### Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id <a name="get"></a>

**API Endpoint**: `GET /LinkedTransactions/{LinkedTransactionID}`

#### Parameters

| Parameter               | Required | Description                               | Example                                  |
| ----------------------- | :------: | ----------------------------------------- | ---------------------------------------- |
| `linked_transaction_id` |    ✓     | Unique identifier for a LinkedTransaction | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`        |    ✓     | Xero identifier for Tenant                | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.linked_transactions.get(
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
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
res = await client.linked_transactions.get(
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[LinkedTransactions](/xero_accounting_py/types/models/linked_transactions.py)

##### Example

```python
{}
```

### Updates a specific linked transactions (billable expenses) <a name="update"></a>

**API Endpoint**: `POST /LinkedTransactions/{LinkedTransactionID}`

#### Parameters

| Parameter               | Required | Description                               | Example                                           |
| ----------------------- | :------: | ----------------------------------------- | ------------------------------------------------- |
| `linked_transaction_id` |    ✓     | Unique identifier for a LinkedTransaction | `"00000000-0000-0000-0000-000000000000"`          |
| `xero_tenant_id`        |    ✓     | Xero identifier for Tenant                | `"YOUR_XERO_TENANT_ID"`                           |
| `linked_transactions`   |    ✗     |                                           | `[{"updated_date_utc": "/Date(1573755038314)/"}]` |

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
res = client.linked_transactions.update(
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    linked_transactions=[
        {
            "source_line_item_id": "00000000-0000-0000-0000-000000000000",
            "source_transaction_id": "00000000-0000-0000-0000-000000000000",
        }
    ],
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
res = await client.linked_transactions.update(
    linked_transaction_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    linked_transactions=[
        {
            "source_line_item_id": "00000000-0000-0000-0000-000000000000",
            "source_transaction_id": "00000000-0000-0000-0000-000000000000",
        }
    ],
)
```

#### Response

##### Type

[LinkedTransactions](/xero_accounting_py/types/models/linked_transactions.py)

##### Example

```python
{}
```

### Creates linked transactions (billable expenses) <a name="create"></a>

**API Endpoint**: `PUT /LinkedTransactions`

#### Parameters

| Parameter                      | Required | Description                                                                                                                                                                                                                                                   | Example                                  |
| ------------------------------ | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `xero_tenant_id`               |    ✓     | Xero identifier for Tenant                                                                                                                                                                                                                                    | `"YOUR_XERO_TENANT_ID"`                  |
| `contact_id`                   |    ✗     | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED. | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `linked_transaction_id`        |    ✗     | The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9                                                                                                                                                    | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `source_line_item_id`          |    ✗     | The line item identifier from the source transaction.                                                                                                                                                                                                         | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `source_transaction_id`        |    ✗     | Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice                                                                                                                                                   | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `source_transaction_type_code` |    ✗     | The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction.                                                                                            | `"ACCPAY"`                               |
| `status`                       |    ✗     | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED. | `"APPROVED"`                             |
| `target_line_item_id`          |    ✗     | The line item identifier from the target transaction. It is possible to link multiple billable expenses to the same TargetLineItemID.                                                                                                                         | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `target_transaction_id`        |    ✗     | Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice                                                                                                                                                   | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `type_`                        |    ✗     | This will always be BILLABLEEXPENSE. More types may be added in future.                                                                                                                                                                                       | `"BILLABLEEXPENSE"`                      |
| `updated_date_utc`             |    ✗     | The last modified date in UTC format                                                                                                                                                                                                                          | `"/Date(1573755038314)/"`                |
| `validation_errors`            |    ✗     | Displays array of validation error messages from the API                                                                                                                                                                                                      | `[{}]`                                   |

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
res = client.linked_transactions.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", updated_date_utc="/Date(1573755038314)/"
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
res = await client.linked_transactions.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID", updated_date_utc="/Date(1573755038314)/"
)
```

#### Response

##### Type

[LinkedTransactions](/xero_accounting_py/types/models/linked_transactions.py)

##### Example

```python
{}
```

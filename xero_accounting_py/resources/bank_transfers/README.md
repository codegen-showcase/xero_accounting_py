# bank_transfers

## Module Functions

### Retrieves all bank transfers <a name="list"></a>

**API Endpoint**: `GET /BankTransfers`

#### Parameters

| Parameter        | Required | Description                | Example                  |
| ---------------- | :------: | -------------------------- | ------------------------ |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"`  |
| `order`          |    ✗     | Order by an any element    | `"Amount ASC"`           |
| `where`          |    ✗     | Filter by an any element   | `"HasAttachments==true"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transfers.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Amount ASC",
    where="HasAttachments==true",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transfers.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Amount ASC",
    where="HasAttachments==true",
)
```

#### Response

##### Type

[BankTransfers](/xero_accounting_py/types/models/bank_transfers.py)

##### Example

```python
{}
```

### Retrieves specific bank transfers by using a unique bank transfer Id <a name="get"></a>

**API Endpoint**: `GET /BankTransfers/{BankTransferID}`

#### Parameters

| Parameter          | Required | Description                                          | Example                                  |
| ------------------ | :------: | ---------------------------------------------------- | ---------------------------------------- |
| `bank_transfer_id` |    ✓     | Xero generated unique identifier for a bank transfer | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                           | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transfers.get(
    bank_transfer_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transfers.get(
    bank_transfer_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[BankTransfers](/xero_accounting_py/types/models/bank_transfers.py)

##### Example

```python
{}
```

### Creates a bank transfer <a name="create"></a>

**API Endpoint**: `PUT /BankTransfers`

#### Parameters

| Parameter        | Required | Description                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------- | :------: | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `bank_transfers` |    ✗     |                            | `[{"amount": 123.0, "created_date_utc": "/Date(1573755038314)/", "from_bank_account": {"account_id": "00000000-0000-0000-0000-000000000000", "code": "4400", "has_attachments": False, "name": "Food Sales", "updated_date_utc": "/Date(1573755038314)/"}, "from_is_reconciled": False, "has_attachments": False, "to_bank_account": {"account_id": "00000000-0000-0000-0000-000000000000", "code": "4400", "has_attachments": False, "name": "Food Sales", "updated_date_utc": "/Date(1573755038314)/"}, "to_is_reconciled": False}]` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.bank_transfers.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    bank_transfers=[
        {
            "amount": 50.0,
            "from_bank_account": {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "bank_account_number": "123455",
                "bank_account_type": "BANK",
                "class_": "ASSET",
                "code": "090",
                "currency_code": "USD",
                "enable_payments_to_account": False,
                "has_attachments": False,
                "name": "My Savings",
                "reporting_code": "ASS",
                "reporting_code_name": "Assets",
                "show_in_expense_claims": False,
                "status": "ACTIVE",
                "tax_type": "NONE",
                "type_": "BANK",
                "updated_date_utc": "2016-10-17T13:45:33.993-07:00",
            },
            "from_is_reconciled": True,
            "reference": "Sub 098801",
            "to_bank_account": {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "bank_account_number": "123455",
                "bank_account_type": "BANK",
                "class_": "ASSET",
                "code": "088",
                "currency_code": "USD",
                "enable_payments_to_account": False,
                "has_attachments": False,
                "name": "Business Wells Fargo",
                "reporting_code": "ASS",
                "reporting_code_name": "Assets",
                "show_in_expense_claims": False,
                "status": "ACTIVE",
                "tax_type": "NONE",
                "type_": "BANK",
                "updated_date_utc": "2016-06-03T08:31:14.517-07:00",
            },
            "to_is_reconciled": True,
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.bank_transfers.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    bank_transfers=[
        {
            "amount": 50.0,
            "from_bank_account": {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "bank_account_number": "123455",
                "bank_account_type": "BANK",
                "class_": "ASSET",
                "code": "090",
                "currency_code": "USD",
                "enable_payments_to_account": False,
                "has_attachments": False,
                "name": "My Savings",
                "reporting_code": "ASS",
                "reporting_code_name": "Assets",
                "show_in_expense_claims": False,
                "status": "ACTIVE",
                "tax_type": "NONE",
                "type_": "BANK",
                "updated_date_utc": "2016-10-17T13:45:33.993-07:00",
            },
            "from_is_reconciled": True,
            "reference": "Sub 098801",
            "to_bank_account": {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "bank_account_number": "123455",
                "bank_account_type": "BANK",
                "class_": "ASSET",
                "code": "088",
                "currency_code": "USD",
                "enable_payments_to_account": False,
                "has_attachments": False,
                "name": "Business Wells Fargo",
                "reporting_code": "ASS",
                "reporting_code_name": "Assets",
                "show_in_expense_claims": False,
                "status": "ACTIVE",
                "tax_type": "NONE",
                "type_": "BANK",
                "updated_date_utc": "2016-06-03T08:31:14.517-07:00",
            },
            "to_is_reconciled": True,
        }
    ],
)
```

#### Response

##### Type

[BankTransfers](/xero_accounting_py/types/models/bank_transfers.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history

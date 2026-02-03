# setup

## Module Functions

### Sets the chart of accounts, the conversion date and conversion balances <a name="create"></a>

**API Endpoint**: `POST /Setup`

#### Parameters

| Parameter             | Required | Description                                                                        | Example                                                                                                                                                                  |
| --------------------- | :------: | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `xero_tenant_id`      |    ✓     | Xero identifier for Tenant                                                         | `"YOUR_XERO_TENANT_ID"`                                                                                                                                                  |
| `accounts`            |    ✗     |                                                                                    | `[{"account_id": "00000000-0000-0000-0000-000000000000", "code": "string", "has_attachments": True, "name": "Food Sales", "updated_date_utc": "/Date(1573755038314)/"}]` |
| `conversion_balances` |    ✗     | Balance supplied for each account that has a value as at the conversion date.      | `[{}]`                                                                                                                                                                   |
| `conversion_date`     |    ✗     |                                                                                    | `{"month": 1, "year": 2020}`                                                                                                                                             |
| `└─ month`            |    ✗     | The month the organisation starts using Xero. Value is an integer between 1 and 12 | `1`                                                                                                                                                                      |
| `└─ year`             |    ✗     | The year the organisation starts using Xero. Value is an integer greater than 2006 | `2020`                                                                                                                                                                   |

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
res = client.setup.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    accounts=[
        {
            "code": "200",
            "name": "Sales",
            "reporting_code": "REV.TRA.GOO",
            "type_": "SALES",
        },
        {
            "code": "400",
            "name": "Advertising",
            "reporting_code": "EXP",
            "type_": "OVERHEADS",
        },
        {
            "code": "610",
            "name": "Accounts Receivable",
            "reporting_code": "ASS.CUR.REC.TRA",
            "system_account": "DEBTORS",
            "type_": "CURRENT",
        },
        {
            "code": "800",
            "name": "Accounts Payable",
            "reporting_code": "LIA.CUR.PAY",
            "system_account": "CREDITORS",
            "type_": "CURRLIAB",
        },
    ],
    conversion_balances=[{}],
    conversion_date={},
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
res = await client.setup.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    accounts=[
        {
            "code": "200",
            "name": "Sales",
            "reporting_code": "REV.TRA.GOO",
            "type_": "SALES",
        },
        {
            "code": "400",
            "name": "Advertising",
            "reporting_code": "EXP",
            "type_": "OVERHEADS",
        },
        {
            "code": "610",
            "name": "Accounts Receivable",
            "reporting_code": "ASS.CUR.REC.TRA",
            "system_account": "DEBTORS",
            "type_": "CURRENT",
        },
        {
            "code": "800",
            "name": "Accounts Payable",
            "reporting_code": "LIA.CUR.PAY",
            "system_account": "CREDITORS",
            "type_": "CURRLIAB",
        },
    ],
    conversion_balances=[{}],
    conversion_date={},
)
```

#### Response

##### Type

[ImportSummaryObject](/xero_accounting_py/types/models/import_summary_object.py)

##### Example

```python
{}
```

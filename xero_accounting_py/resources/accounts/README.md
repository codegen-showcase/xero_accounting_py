# accounts

## Module Functions

### Deletes a chart of accounts <a name="delete"></a>

**API Endpoint**: `DELETE /Accounts/{AccountID}`

#### Parameters

| Parameter        | Required | Description                          | Example                                  |
| ---------------- | :------: | ------------------------------------ | ---------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounts.delete(
    account_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.accounts.delete(
    account_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Accounts](/xero_accounting_py/types/models/accounts.py)

##### Example

```python
{}
```

### Retrieves the full chart of accounts <a name="list"></a>

**API Endpoint**: `GET /Accounts`

#### Parameters

| Parameter        | Required | Description                | Example                                                   |
| ---------------- | :------: | -------------------------- | --------------------------------------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"`                                   |
| `order`          |    ✗     | Order by an any element    | `"Name ASC"`                                              |
| `where`          |    ✗     | Filter by an any element   | `"Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounts.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Name ASC",
    where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.accounts.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Name ASC",
    where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
)
```

#### Response

##### Type

[Accounts](/xero_accounting_py/types/models/accounts.py)

##### Example

```python
{}
```

### Retrieves a single chart of accounts by using a unique account Id <a name="get"></a>

**API Endpoint**: `GET /Accounts/{AccountID}`

#### Parameters

| Parameter        | Required | Description                          | Example                                  |
| ---------------- | :------: | ------------------------------------ | ---------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounts.get(
    account_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.accounts.get(
    account_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Accounts](/xero_accounting_py/types/models/accounts.py)

##### Example

```python
{}
```

### Updates a chart of accounts <a name="update"></a>

**API Endpoint**: `POST /Accounts/{AccountID}`

#### Parameters

| Parameter        | Required | Description                          | Example                                                                                                                                                                 |
| ---------------- | :------: | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`     |    ✓     | Unique identifier for Account object | `"00000000-0000-0000-0000-000000000000"`                                                                                                                                |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                                                                                                                                                 |
| `accounts`       |    ✗     |                                      | `[{"account_id": "00000000-0000-0000-0000-000000000000", "code": "4400", "has_attachments": False, "name": "Food Sales", "updated_date_utc": "/Date(1573755038314)/"}]` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounts.update(
    account_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    accounts=[
        {
            "account_id": "99ce6032-0678-4aa0-8148-240c75fee33a",
            "class_": "EXPENSE",
            "code": "123456",
            "description": "GoodBye World",
            "enable_payments_to_account": False,
            "name": "BarFoo",
            "reporting_code": "EXP",
            "reporting_code_name": "Expense",
            "show_in_expense_claims": False,
            "tax_type": "INPUT",
            "type_": "EXPENSE",
            "updated_date_utc": "2019-02-21T16:29:47.96-08:00",
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.accounts.update(
    account_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    accounts=[
        {
            "account_id": "99ce6032-0678-4aa0-8148-240c75fee33a",
            "class_": "EXPENSE",
            "code": "123456",
            "description": "GoodBye World",
            "enable_payments_to_account": False,
            "name": "BarFoo",
            "reporting_code": "EXP",
            "reporting_code_name": "Expense",
            "show_in_expense_claims": False,
            "tax_type": "INPUT",
            "type_": "EXPENSE",
            "updated_date_utc": "2019-02-21T16:29:47.96-08:00",
        }
    ],
)
```

#### Response

##### Type

[Accounts](/xero_accounting_py/types/models/accounts.py)

##### Example

```python
{}
```

### Creates a new chart of accounts <a name="create"></a>

**API Endpoint**: `PUT /Accounts`

#### Parameters

| Parameter                    | Required | Description                                                                                                                                                        | Example                                  |
| ---------------------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `xero_tenant_id`             |    ✓     | Xero identifier for Tenant                                                                                                                                         | `"YOUR_XERO_TENANT_ID"`                  |
| `account_id`                 |    ✗     | The Xero identifier for an account – specified as a string following the endpoint name e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9                                  | `"00000000-0000-0000-0000-000000000000"` |
| `add_to_watchlist`           |    ✗     | Boolean – describes whether the account is shown in the watchlist widget on the dashboard                                                                          | `True`                                   |
| `bank_account_number`        |    ✗     | For bank accounts only (Account Type BANK)                                                                                                                         | `"string"`                               |
| `bank_account_type`          |    ✗     | For bank accounts only. See Bank Account types                                                                                                                     | `"BANK"`                                 |
| `class_`                     |    ✗     | See Account Class Types                                                                                                                                            | `"ASSET"`                                |
| `code`                       |    ✗     | Customer defined alpha numeric account code e.g 200 or SALES (max length = 10)                                                                                     | `"4400"`                                 |
| `currency_code`              |    ✗     |                                                                                                                                                                    | `"AED"`                                  |
| `description`                |    ✗     | Description of the Account. Valid for all types of accounts except bank accounts (max length = 4000)                                                               | `"string"`                               |
| `enable_payments_to_account` |    ✗     | Boolean – describes whether account can have payments applied to it                                                                                                | `True`                                   |
| `has_attachments`            |    ✗     | boolean to indicate if an account has an attachment (read only)                                                                                                    | `False`                                  |
| `name`                       |    ✗     | Name of account (max length = 150)                                                                                                                                 | `"Food Sales"`                           |
| `reporting_code`             |    ✗     | Shown if set                                                                                                                                                       | `"string"`                               |
| `reporting_code_name`        |    ✗     | Shown if set                                                                                                                                                       | `"string"`                               |
| `show_in_expense_claims`     |    ✗     | Boolean – describes whether account code is available for use with expense claims                                                                                  | `True`                                   |
| `status`                     |    ✗     | Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes                                                                              | `"ACTIVE"`                               |
| `system_account`             |    ✗     | If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null. | `"BANKCURRENCYGAIN"`                     |
| `tax_type`                   |    ✗     | The tax type from taxRates                                                                                                                                         | `"string"`                               |
| `type_`                      |    ✗     |                                                                                                                                                                    | `"BANK"`                                 |
| `updated_date_utc`           |    ✗     | Last modified date UTC format                                                                                                                                      | `"/Date(1573755038314)/"`                |
| `validation_errors`          |    ✗     | Displays array of validation error messages from the API                                                                                                           | `[{}]`                                   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounts.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    account_id="00000000-0000-0000-0000-000000000000",
    code="123456",
    description="Hello World",
    has_attachments=False,
    name="Foobar",
    type_="EXPENSE",
    updated_date_utc="/Date(1573755038314)/",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.accounts.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    account_id="00000000-0000-0000-0000-000000000000",
    code="123456",
    description="Hello World",
    has_attachments=False,
    name="Foobar",
    type_="EXPENSE",
    updated_date_utc="/Date(1573755038314)/",
)
```

#### Response

##### Type

[Accounts](/xero_accounting_py/types/models/accounts.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments

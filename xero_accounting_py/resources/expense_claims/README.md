# expense_claims

## Module Functions

### Retrieves expense claims <a name="list"></a>

**API Endpoint**: `GET /ExpenseClaims`

#### Parameters

| Parameter        | Required | Description                | Example                   |
| ---------------- | :------: | -------------------------- | ------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"`   |
| `order`          |    ✗     | Order by an any element    | `"Status ASC"`            |
| `where`          |    ✗     | Filter by an any element   | `"Status==\"SUBMITTED\""` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.expense_claims.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Status ASC",
    where='Status=="SUBMITTED"',
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.expense_claims.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    order="Status ASC",
    where='Status=="SUBMITTED"',
)
```

#### Response

##### Type

[ExpenseClaims](/xero_accounting_py/types/models/expense_claims.py)

##### Example

```python
{}
```

### Retrieves a specific expense claim using a unique expense claim Id <a name="get"></a>

**API Endpoint**: `GET /ExpenseClaims/{ExpenseClaimID}`

#### Parameters

| Parameter          | Required | Description                          | Example                                  |
| ------------------ | :------: | ------------------------------------ | ---------------------------------------- |
| `expense_claim_id` |    ✓     | Unique identifier for a ExpenseClaim | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.expense_claims.get(
    expense_claim_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.expense_claims.get(
    expense_claim_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[ExpenseClaims](/xero_accounting_py/types/models/expense_claims.py)

##### Example

```python
{}
```

### Updates a specific expense claims <a name="update"></a>

**API Endpoint**: `POST /ExpenseClaims/{ExpenseClaimID}`

#### Parameters

| Parameter          | Required | Description                          | Example                                  |
| ------------------ | :------: | ------------------------------------ | ---------------------------------------- |
| `expense_claim_id` |    ✓     | Unique identifier for a ExpenseClaim | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant           | `"YOUR_XERO_TENANT_ID"`                  |
| `expense_claims`   |    ✗     |                                      | `[]`                                     |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.expense_claims.update(
    expense_claim_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    expense_claims=[
        {
            "status": "SUBMITTED",
            "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.expense_claims.update(
    expense_claim_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    expense_claims=[
        {
            "status": "SUBMITTED",
            "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
        }
    ],
)
```

#### Response

##### Type

[ExpenseClaims](/xero_accounting_py/types/models/expense_claims.py)

##### Example

```python
{}
```

### Creates expense claims <a name="create"></a>

**API Endpoint**: `PUT /ExpenseClaims`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `expense_claims` |    ✗     |                            | `[]`                    |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.expense_claims.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    expense_claims=[
        {
            "status": "SUBMITTED",
            "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
        }
    ],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.expense_claims.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    expense_claims=[
        {
            "status": "SUBMITTED",
            "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
        }
    ],
)
```

#### Response

##### Type

[ExpenseClaims](/xero_accounting_py/types/models/expense_claims.py)

##### Example

```python
{}
```

## Submodules

- [history](history/README.md) - history

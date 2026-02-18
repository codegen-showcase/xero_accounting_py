# budgets

## Module Functions

### Retrieve a list of budgets <a name="list"></a>

**API Endpoint**: `GET /Budgets`

#### Parameters

| Parameter        | Required | Description                                                              | Example                                              |
| ---------------- | :------: | ------------------------------------------------------------------------ | ---------------------------------------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                               | `"YOUR_XERO_TENANT_ID"`                              |
| `date_from`      |    ✗     | Filter by end date                                                       | `"2019-10-31"`                                       |
| `date_to`        |    ✗     | Filter by start date                                                     | `"2019-10-31"`                                       |
| `i_ds`           |    ✗     | Filter by BudgetID. Allows you to retrieve a specific individual budget. | `"&quot;00000000-0000-0000-0000-000000000000&quot;"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.budgets.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date_from="2019-10-31",
    date_to="2019-10-31",
    i_ds="&quot;00000000-0000-0000-0000-000000000000&quot;",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.budgets.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date_from="2019-10-31",
    date_to="2019-10-31",
    i_ds="&quot;00000000-0000-0000-0000-000000000000&quot;",
)
```

#### Response

##### Type

[Budgets](/xero_accounting_py/types/models/budgets.py)

##### Example

```python
{}
```

### Retrieves a specific budget, which includes budget lines <a name="get"></a>

**API Endpoint**: `GET /Budgets/{BudgetID}`

#### Parameters

| Parameter        | Required | Description                   | Example                                  |
| ---------------- | :------: | ----------------------------- | ---------------------------------------- |
| `budget_id`      |    ✓     | Unique identifier for Budgets | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant    | `"YOUR_XERO_TENANT_ID"`                  |
| `date_from`      |    ✗     | Filter by end date            | `"2019-10-31"`                           |
| `date_to`        |    ✗     | Filter by start date          | `"2019-10-31"`                           |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.budgets.get(
    budget_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date_from="2019-10-31",
    date_to="2019-10-31",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.budgets.get(
    budget_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date_from="2019-10-31",
    date_to="2019-10-31",
)
```

#### Response

##### Type

[Budgets](/xero_accounting_py/types/models/budgets.py)

##### Example

```python
{}
```

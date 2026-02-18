# repeating_invoices

## Module Functions

### Retrieves repeating invoices <a name="list"></a>

**API Endpoint**: `GET /RepeatingInvoices`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |
| `order`          |    ✗     | Order by an any element    | `"Total ASC"`           |
| `where`          |    ✗     | Filter by an any element   | `"Status==\"DRAFT\""`   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.repeating_invoices.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Total ASC", where='Status=="DRAFT"'
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.repeating_invoices.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID", order="Total ASC", where='Status=="DRAFT"'
)
```

#### Response

##### Type

[RepeatingInvoices](/xero_accounting_py/types/models/repeating_invoices.py)

##### Example

```python
{}
```

### Retrieves a specific repeating invoice by using a unique repeating invoice Id <a name="get"></a>

**API Endpoint**: `GET /RepeatingInvoices/{RepeatingInvoiceID}`

#### Parameters

| Parameter              | Required | Description                               | Example                                  |
| ---------------------- | :------: | ----------------------------------------- | ---------------------------------------- |
| `repeating_invoice_id` |    ✓     | Unique identifier for a Repeating Invoice | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`       |    ✓     | Xero identifier for Tenant                | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.repeating_invoices.get(
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.repeating_invoices.get(
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[RepeatingInvoices](/xero_accounting_py/types/models/repeating_invoices.py)

##### Example

```python
{}
```

### Creates or deletes one or more repeating invoice templates <a name="update_or_create"></a>

**API Endpoint**: `POST /RepeatingInvoices`

#### Parameters

| Parameter            | Required | Description                                                                                   | Example                 |
| -------------------- | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`     |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `repeating_invoices` |    ✗     |                                                                                               | `[]`                    |
| `summarize_errors`   |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.repeating_invoices.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    repeating_invoices=[
        {
            "approved_for_sending": False,
            "currency_code": "NZD",
            "include_pdf": False,
            "line_amount_types": "Exclusive",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Guitars Fender Strat",
                    "line_amount": 5000.0,
                    "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                    "quantity": 1.0,
                    "tax_amount": 750.0,
                    "tax_type": "OUTPUT2",
                    "tracking": [
                        {
                            "name": "Region",
                            "option": "North",
                            "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                            "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "unit_amount": 5000.0,
                }
            ],
            "mark_as_sent": False,
            "reference": "[Week]",
            "schedule": {
                "due_date": 10,
                "due_date_type": "OFFOLLOWINGMONTH",
                "period": 1,
                "start_date": "/Date(1555286400000+0000)/",
                "unit": "MONTHLY",
            },
            "send_copy": False,
            "status": "AUTHORISED",
            "type_": "ACCREC",
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
res = await client.repeating_invoices.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    repeating_invoices=[
        {
            "approved_for_sending": False,
            "currency_code": "NZD",
            "include_pdf": False,
            "line_amount_types": "Exclusive",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Guitars Fender Strat",
                    "line_amount": 5000.0,
                    "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                    "quantity": 1.0,
                    "tax_amount": 750.0,
                    "tax_type": "OUTPUT2",
                    "tracking": [
                        {
                            "name": "Region",
                            "option": "North",
                            "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                            "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "unit_amount": 5000.0,
                }
            ],
            "mark_as_sent": False,
            "reference": "[Week]",
            "schedule": {
                "due_date": 10,
                "due_date_type": "OFFOLLOWINGMONTH",
                "period": 1,
                "start_date": "/Date(1555286400000+0000)/",
                "unit": "MONTHLY",
            },
            "send_copy": False,
            "status": "AUTHORISED",
            "type_": "ACCREC",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[RepeatingInvoices](/xero_accounting_py/types/models/repeating_invoices.py)

##### Example

```python
{}
```

### Deletes a specific repeating invoice template <a name="update"></a>

**API Endpoint**: `POST /RepeatingInvoices/{RepeatingInvoiceID}`

#### Parameters

| Parameter              | Required | Description                               | Example                                  |
| ---------------------- | :------: | ----------------------------------------- | ---------------------------------------- |
| `repeating_invoice_id` |    ✓     | Unique identifier for a Repeating Invoice | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`       |    ✓     | Xero identifier for Tenant                | `"YOUR_XERO_TENANT_ID"`                  |
| `repeating_invoices`   |    ✗     |                                           | `[]`                                     |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.repeating_invoices.update(
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.repeating_invoices.update(
    repeating_invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[RepeatingInvoices](/xero_accounting_py/types/models/repeating_invoices.py)

##### Example

```python
{}
```

### Creates one or more repeating invoice templates <a name="create"></a>

**API Endpoint**: `PUT /RepeatingInvoices`

#### Parameters

| Parameter            | Required | Description                                                                                   | Example                 |
| -------------------- | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`     |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `repeating_invoices` |    ✗     |                                                                                               | `[]`                    |
| `summarize_errors`   |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.repeating_invoices.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    repeating_invoices=[
        {
            "approved_for_sending": False,
            "currency_code": "NZD",
            "include_pdf": False,
            "line_amount_types": "Exclusive",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Guitars Fender Strat",
                    "line_amount": 5000.0,
                    "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                    "quantity": 1.0,
                    "tax_amount": 750.0,
                    "tax_type": "OUTPUT2",
                    "tracking": [
                        {
                            "name": "Region",
                            "option": "North",
                            "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                            "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "unit_amount": 5000.0,
                }
            ],
            "mark_as_sent": False,
            "reference": "[Week]",
            "schedule": {
                "due_date": 10,
                "due_date_type": "OFFOLLOWINGMONTH",
                "period": 1,
                "start_date": "/Date(1555286400000+0000)/",
                "unit": "MONTHLY",
            },
            "send_copy": False,
            "status": "AUTHORISED",
            "type_": "ACCREC",
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
res = await client.repeating_invoices.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    repeating_invoices=[
        {
            "approved_for_sending": False,
            "currency_code": "NZD",
            "include_pdf": False,
            "line_amount_types": "Exclusive",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Guitars Fender Strat",
                    "line_amount": 5000.0,
                    "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                    "quantity": 1.0,
                    "tax_amount": 750.0,
                    "tax_type": "OUTPUT2",
                    "tracking": [
                        {
                            "name": "Region",
                            "option": "North",
                            "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                            "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "unit_amount": 5000.0,
                }
            ],
            "mark_as_sent": False,
            "reference": "[Week]",
            "schedule": {
                "due_date": 10,
                "due_date_type": "OFFOLLOWINGMONTH",
                "period": 1,
                "start_date": "/Date(1555286400000+0000)/",
                "unit": "MONTHLY",
            },
            "send_copy": False,
            "status": "AUTHORISED",
            "type_": "ACCREC",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[RepeatingInvoices](/xero_accounting_py/types/models/repeating_invoices.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [history](history/README.md) - history

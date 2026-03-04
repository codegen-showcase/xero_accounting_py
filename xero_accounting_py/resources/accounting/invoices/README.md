# accounting.invoices

## Module Functions

### Retrieves sales invoices or purchase bills <a name="list"></a>

**API Endpoint**: `GET /Invoices`

#### Parameters

| Parameter           | Required | Description                                                                                                                                                                                                                                            | Example                                    |
| ------------------- | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| `xero_tenant_id`    |    ✓     | Xero identifier for Tenant                                                                                                                                                                                                                             | `"YOUR_XERO_TENANT_ID"`                    |
| `contact_i_ds`      |    ✗     | Filter by a comma-separated list of ContactIDs.                                                                                                                                                                                                        | `["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"]` |
| `created_by_my_app` |    ✗     | When set to true you'll only retrieve Invoices created by your app                                                                                                                                                                                     | `False`                                    |
| `i_ds`              |    ✗     | Filter by a comma-separated list of InvoicesIDs.                                                                                                                                                                                                       | `["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"]` |
| `include_archived`  |    ✗     | e.g. includeArchived=true - Invoices with a status of ARCHIVED will be included in the response                                                                                                                                                        | `True`                                     |
| `invoice_numbers`   |    ✗     | Filter by a comma-separated list of InvoiceNumbers.                                                                                                                                                                                                    | `["string"]`                               |
| `order`             |    ✗     | Order by an any element                                                                                                                                                                                                                                | `"InvoiceNumber ASC"`                      |
| `page`              |    ✗     | e.g. page=1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice                                                                                                                                          | `1`                                        |
| `page_size`         |    ✗     | Number of records to retrieve per page                                                                                                                                                                                                                 | `100`                                      |
| `search_term`       |    ✗     | Search parameter that performs a case-insensitive text search across the fields e.g. InvoiceNumber, Reference.                                                                                                                                         | `"SearchTerm=REF12"`                       |
| `statuses`          |    ✗     | Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter.                                                                              | `["string"]`                               |
| `summary_only`      |    ✗     | Use summaryOnly=true in GET Contacts and Invoices endpoint to retrieve a smaller version of the response object. This returns only lightweight fields, excluding computation-heavy fields from the response, making the API calls quick and efficient. | `True`                                     |
| `unitdp`            |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts                                                                                                                                                       | `4`                                        |
| `where`             |    ✗     | Filter by an any element                                                                                                                                                                                                                               | `"Status==\"DRAFT\""`                      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounting.invoices.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    created_by_my_app=False,
    include_archived=True,
    order="InvoiceNumber ASC",
    page=1,
    page_size=100,
    search_term="SearchTerm=REF12",
    summary_only=True,
    unitdp=4,
    where='Status=="DRAFT"',
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.accounting.invoices.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    created_by_my_app=False,
    include_archived=True,
    order="InvoiceNumber ASC",
    page=1,
    page_size=100,
    search_term="SearchTerm=REF12",
    summary_only=True,
    unitdp=4,
    where='Status=="DRAFT"',
)
```

#### Response

##### Type

[Invoices](/xero_accounting_py/types/models/invoices.py)

##### Example

```python
{}
```

### Retrieves a specific sales invoice or purchase bill using a unique invoice Id <a name="get"></a>

**API Endpoint**: `GET /Invoices/{InvoiceID}`

#### Parameters

| Parameter        | Required | Description                                                                                      | Example                                  |
| ---------------- | :------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `invoice_id`     |    ✓     | Unique identifier for an Invoice                                                                 | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                       | `"YOUR_XERO_TENANT_ID"`                  |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | `4`                                      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounting.invoices.get(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.accounting.invoices.get(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    unitdp=4,
)
```

#### Response

##### Type

[Invoices](/xero_accounting_py/types/models/invoices.py)

##### Example

```python
{}
```

### Updates or creates one or more sales invoices or purchase bills <a name="update_or_create"></a>

**API Endpoint**: `POST /Invoices`

#### Parameters

| Parameter          | Required | Description                                                                                                                            | Example                                                          |
| ------------------ | :------: | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                                                             | `"YOUR_XERO_TENANT_ID"`                                          |
| `invoices`         |    ✗     |                                                                                                                                        | `[]`                                                             |
| `pagination`       |    ✗     |                                                                                                                                        | `{"item_count": 2, "page": 1, "page_count": 1, "page_size": 10}` |
| `└─ item_count`    |    ✗     | Number of items returned                                                                                                               | `2`                                                              |
| `└─ page`          |    ✗     | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.                             | `1`                                                              |
| `└─ page_count`    |    ✗     | Number of pages available                                                                                                              | `1`                                                              |
| `└─ page_size`     |    ✗     | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | `10`                                                             |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors                                          | `True`                                                           |
| `unitdp`           |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts                                       | `4`                                                              |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                                                                        | `[{}]`                                                           |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounting.invoices.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    invoices=[
        {
            "date": "2019-03-11",
            "due_date": "2018-12-10",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Acme Tires",
                    "line_amount": 40.0,
                    "quantity": 2.0,
                    "tax_type": "NONE",
                    "unit_amount": 20.0,
                }
            ],
            "reference": "Website Design",
            "status": "AUTHORISED",
            "type_": "ACCREC",
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
res = await client.accounting.invoices.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    invoices=[
        {
            "date": "2019-03-11",
            "due_date": "2018-12-10",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Acme Tires",
                    "line_amount": 40.0,
                    "quantity": 2.0,
                    "tax_type": "NONE",
                    "unit_amount": 20.0,
                }
            ],
            "reference": "Website Design",
            "status": "AUTHORISED",
            "type_": "ACCREC",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Response

##### Type

[Invoices](/xero_accounting_py/types/models/invoices.py)

##### Example

```python
{}
```

### Updates a specific sales invoices or purchase bills <a name="update"></a>

**API Endpoint**: `POST /Invoices/{InvoiceID}`

#### Parameters

| Parameter        | Required | Description                                                                                                                            | Example                                                          |
| ---------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `invoice_id`     |    ✓     | Unique identifier for an Invoice                                                                                                       | `"00000000-0000-0000-0000-000000000000"`                         |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                                             | `"YOUR_XERO_TENANT_ID"`                                          |
| `invoices`       |    ✗     |                                                                                                                                        | `[]`                                                             |
| `pagination`     |    ✗     |                                                                                                                                        | `{"item_count": 2, "page": 1, "page_count": 1, "page_size": 10}` |
| `└─ item_count`  |    ✗     | Number of items returned                                                                                                               | `2`                                                              |
| `└─ page`        |    ✗     | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.                             | `1`                                                              |
| `└─ page_count`  |    ✗     | Number of pages available                                                                                                              | `1`                                                              |
| `└─ page_size`   |    ✗     | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | `10`                                                             |
| `unitdp`         |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts                                       | `4`                                                              |
| `warnings`       |    ✗     | Displays array of warning messages from the API                                                                                        | `[{}]`                                                           |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounting.invoices.update(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    invoices=[
        {
            "invoice_id": "00000000-0000-0000-0000-000000000000",
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
            "reference": "May the force be with you",
            "type_": "ACCPAY",
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
res = await client.accounting.invoices.update(
    invoice_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    invoices=[
        {
            "invoice_id": "00000000-0000-0000-0000-000000000000",
            "line_items": [
                {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "line_item_id": "00000000-0000-0000-0000-000000000000",
                    "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
            "reference": "May the force be with you",
            "type_": "ACCPAY",
        }
    ],
    unitdp=4,
)
```

#### Response

##### Type

[Invoices](/xero_accounting_py/types/models/invoices.py)

##### Example

```python
{}
```

### Creates one or more sales invoices or purchase bills <a name="create"></a>

**API Endpoint**: `PUT /Invoices`

#### Parameters

| Parameter          | Required | Description                                                                                                                            | Example                                                          |
| ------------------ | :------: | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                                                             | `"YOUR_XERO_TENANT_ID"`                                          |
| `invoices`         |    ✗     |                                                                                                                                        | `[]`                                                             |
| `pagination`       |    ✗     |                                                                                                                                        | `{"item_count": 2, "page": 1, "page_count": 1, "page_size": 10}` |
| `└─ item_count`    |    ✗     | Number of items returned                                                                                                               | `2`                                                              |
| `└─ page`          |    ✗     | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.                             | `1`                                                              |
| `└─ page_count`    |    ✗     | Number of pages available                                                                                                              | `1`                                                              |
| `└─ page_size`     |    ✗     | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | `10`                                                             |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors                                          | `True`                                                           |
| `unitdp`           |    ✗     | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts                                       | `4`                                                              |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                                                                        | `[{}]`                                                           |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.accounting.invoices.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    invoices=[
        {
            "date": "2019-03-11",
            "due_date": "2018-12-10",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Acme Tires",
                    "line_amount": 40.0,
                    "quantity": 2.0,
                    "tax_type": "NONE",
                    "unit_amount": 20.0,
                }
            ],
            "reference": "Website Design",
            "status": "AUTHORISED",
            "type_": "ACCREC",
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
res = await client.accounting.invoices.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    invoices=[
        {
            "date": "2019-03-11",
            "due_date": "2018-12-10",
            "line_items": [
                {
                    "account_code": "200",
                    "description": "Acme Tires",
                    "line_amount": 40.0,
                    "quantity": 2.0,
                    "tax_type": "NONE",
                    "unit_amount": 20.0,
                }
            ],
            "reference": "Website Design",
            "status": "AUTHORISED",
            "type_": "ACCREC",
        }
    ],
    summarize_errors=True,
    unitdp=4,
)
```

#### Response

##### Type

[Invoices](/xero_accounting_py/types/models/invoices.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [email](email/README.md) - email
- [history](history/README.md) - history
- [online_invoice](online_invoice/README.md) - online_invoice
- [pdf](pdf/README.md) - pdf

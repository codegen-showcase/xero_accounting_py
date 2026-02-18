# contacts

## Module Functions

### Retrieves all contacts in a Xero organisation <a name="list"></a>

**API Endpoint**: `GET /Contacts`

#### Parameters

| Parameter          | Required | Description                                                                                                                                                                                                                                            | Example                                    |
| ------------------ | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                                                                                                                                                                             | `"YOUR_XERO_TENANT_ID"`                    |
| `i_ds`             |    ✗     | Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call.                                                                                                                                    | `["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"]` |
| `include_archived` |    ✗     | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response                                                                                                                                                        | `True`                                     |
| `order`            |    ✗     | Order by an any element                                                                                                                                                                                                                                | `"Name ASC"`                               |
| `page`             |    ✗     | e.g. page=1 - Up to 100 contacts will be returned in a single API call.                                                                                                                                                                                | `1`                                        |
| `page_size`        |    ✗     | Number of records to retrieve per page                                                                                                                                                                                                                 | `100`                                      |
| `search_term`      |    ✗     | Search parameter that performs a case-insensitive text search across the Name, FirstName, LastName, ContactNumber and EmailAddress fields.                                                                                                             | `"Joe Bloggs"`                             |
| `summary_only`     |    ✗     | Use summaryOnly=true in GET Contacts and Invoices endpoint to retrieve a smaller version of the response object. This returns only lightweight fields, excluding computation-heavy fields from the response, making the API calls quick and efficient. | `True`                                     |
| `where`            |    ✗     | Filter by an any element                                                                                                                                                                                                                               | `"ContactStatus==&quot;ACTIVE&quot;"`      |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contacts.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    include_archived=True,
    order="Name ASC",
    page=1,
    page_size=100,
    search_term="Joe Bloggs",
    summary_only=True,
    where="ContactStatus==&quot;ACTIVE&quot;",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.contacts.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    include_archived=True,
    order="Name ASC",
    page=1,
    page_size=100,
    search_term="Joe Bloggs",
    summary_only=True,
    where="ContactStatus==&quot;ACTIVE&quot;",
)
```

#### Response

##### Type

[Contacts](/xero_accounting_py/types/models/contacts.py)

##### Example

```python
{}
```

### Retrieves a specific contacts in a Xero organisation using a unique contact Id <a name="get"></a>

**API Endpoint**: `GET /Contacts/{ContactID}`

#### Parameters

| Parameter        | Required | Description                     | Example                                  |
| ---------------- | :------: | ------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant      | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contacts.get(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.contacts.get(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[Contacts](/xero_accounting_py/types/models/contacts.py)

##### Example

```python
{}
```

### Updates or creates one or more contacts in a Xero organisation <a name="update_or_create"></a>

**API Endpoint**: `POST /Contacts`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                 |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `contacts`         |    ✗     |                                                                                               | `[]`                    |
| `pagination`       |    ✗     |                                                                                               | `{}`                    |
| `└─ item_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page`          |    ✗     |                                                                                               | `123`                   |
| `└─ page_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page_size`     |    ✗     |                                                                                               | `123`                   |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                               | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contacts.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[
        {
            "email_address": "hulk@avengers.com",
            "name": "Bruce Banner",
            "payment_terms": {
                "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
            },
            "phones": [
                {
                    "phone_area_code": "415",
                    "phone_number": "555-1212",
                    "phone_type": "MOBILE",
                }
            ],
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
res = await client.contacts.update_or_create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[
        {
            "email_address": "hulk@avengers.com",
            "name": "Bruce Banner",
            "payment_terms": {
                "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
            },
            "phones": [
                {
                    "phone_area_code": "415",
                    "phone_number": "555-1212",
                    "phone_type": "MOBILE",
                }
            ],
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[Contacts](/xero_accounting_py/types/models/contacts.py)

##### Example

```python
{}
```

### Updates a specific contact in a Xero organisation <a name="update"></a>

**API Endpoint**: `POST /Contacts/{ContactID}`

#### Parameters

| Parameter        | Required | Description                                     | Example                                  |
| ---------------- | :------: | ----------------------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact                 | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                      | `"YOUR_XERO_TENANT_ID"`                  |
| `contacts`       |    ✗     |                                                 | `[]`                                     |
| `pagination`     |    ✗     |                                                 | `{}`                                     |
| `└─ item_count`  |    ✗     |                                                 | `123`                                    |
| `└─ page`        |    ✗     |                                                 | `123`                                    |
| `└─ page_count`  |    ✗     |                                                 | `123`                                    |
| `└─ page_size`   |    ✗     |                                                 | `123`                                    |
| `warnings`       |    ✗     | Displays array of warning messages from the API | `[{}]`                                   |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contacts.update(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[{"contact_id": "00000000-0000-0000-0000-000000000000", "name": "Thanos"}],
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.contacts.update(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[{"contact_id": "00000000-0000-0000-0000-000000000000", "name": "Thanos"}],
)
```

#### Response

##### Type

[Contacts](/xero_accounting_py/types/models/contacts.py)

##### Example

```python
{}
```

### Creates multiple contacts (bulk) in a Xero organisation <a name="create"></a>

**API Endpoint**: `PUT /Contacts`

#### Parameters

| Parameter          | Required | Description                                                                                   | Example                 |
| ------------------ | :------: | --------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `contacts`         |    ✗     |                                                                                               | `[]`                    |
| `pagination`       |    ✗     |                                                                                               | `{}`                    |
| `└─ item_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page`          |    ✗     |                                                                                               | `123`                   |
| `└─ page_count`    |    ✗     |                                                                                               | `123`                   |
| `└─ page_size`     |    ✗     |                                                                                               | `123`                   |
| `summarize_errors` |    ✗     | If false return 200 OK and mix of successfully created objects and any with validation errors | `True`                  |
| `warnings`         |    ✗     | Displays array of warning messages from the API                                               | `[{}]`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.contacts.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[
        {
            "addresses": [
                {
                    "address_type": "STREET",
                    "city": "",
                    "country": "",
                    "postal_code": "",
                    "region": "",
                },
                {
                    "address_type": "POBOX",
                    "city": "",
                    "country": "",
                    "postal_code": "",
                    "region": "",
                },
            ],
            "bank_account_details": "",
            "contact_id": "3ff6d40c-af9a-40a3-89ce-3c1556a25591",
            "contact_persons": [{}],
            "contact_status": "ACTIVE",
            "email_address": "sid32476@blah.com",
            "is_customer": False,
            "is_supplier": False,
            "name": "Foo9987",
            "payment_terms": {
                "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
            },
            "phones": [
                {
                    "phone_area_code": "",
                    "phone_country_code": "",
                    "phone_number": "",
                    "phone_type": "DEFAULT",
                },
                {
                    "phone_area_code": "",
                    "phone_country_code": "",
                    "phone_number": "",
                    "phone_type": "DDI",
                },
                {
                    "phone_area_code": "",
                    "phone_country_code": "",
                    "phone_number": "",
                    "phone_type": "FAX",
                },
                {
                    "phone_area_code": "415",
                    "phone_country_code": "",
                    "phone_number": "555-1212",
                    "phone_type": "MOBILE",
                },
            ],
            "purchases_tracking_categories": [{}],
            "sales_tracking_categories": [{}],
            "updated_date_utc": "/Date(1551399321043+0000)/",
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
res = await client.contacts.create(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    contacts=[
        {
            "addresses": [
                {
                    "address_type": "STREET",
                    "city": "",
                    "country": "",
                    "postal_code": "",
                    "region": "",
                },
                {
                    "address_type": "POBOX",
                    "city": "",
                    "country": "",
                    "postal_code": "",
                    "region": "",
                },
            ],
            "bank_account_details": "",
            "contact_id": "3ff6d40c-af9a-40a3-89ce-3c1556a25591",
            "contact_persons": [{}],
            "contact_status": "ACTIVE",
            "email_address": "sid32476@blah.com",
            "is_customer": False,
            "is_supplier": False,
            "name": "Foo9987",
            "payment_terms": {
                "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
            },
            "phones": [
                {
                    "phone_area_code": "",
                    "phone_country_code": "",
                    "phone_number": "",
                    "phone_type": "DEFAULT",
                },
                {
                    "phone_area_code": "",
                    "phone_country_code": "",
                    "phone_number": "",
                    "phone_type": "DDI",
                },
                {
                    "phone_area_code": "",
                    "phone_country_code": "",
                    "phone_number": "",
                    "phone_type": "FAX",
                },
                {
                    "phone_area_code": "415",
                    "phone_country_code": "",
                    "phone_number": "555-1212",
                    "phone_type": "MOBILE",
                },
            ],
            "purchases_tracking_categories": [{}],
            "sales_tracking_categories": [{}],
            "updated_date_utc": "/Date(1551399321043+0000)/",
        }
    ],
    summarize_errors=True,
)
```

#### Response

##### Type

[Contacts](/xero_accounting_py/types/models/contacts.py)

##### Example

```python
{}
```

## Submodules

- [attachments](attachments/README.md) - attachments
- [cis_settings](cis_settings/README.md) - cis_settings
- [history](history/README.md) - history

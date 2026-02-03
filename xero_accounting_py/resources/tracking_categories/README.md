# tracking_categories

## Module Functions

### Deletes a specific tracking category <a name="delete"></a>

**API Endpoint**: `DELETE /TrackingCategories/{TrackingCategoryID}`

#### Parameters

| Parameter              | Required | Description                              | Example                                  |
| ---------------------- | :------: | ---------------------------------------- | ---------------------------------------- |
| `tracking_category_id` |    ✓     | Unique identifier for a TrackingCategory | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`       |    ✓     | Xero identifier for Tenant               | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.tracking_categories.delete(
    tracking_category_id="00000000-0000-0000-0000-000000000000",
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
res = await client.tracking_categories.delete(
    tracking_category_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[TrackingCategories](/xero_accounting_py/types/models/tracking_categories.py)

##### Example

```python
{}
```

### Retrieves tracking categories and options <a name="list"></a>

**API Endpoint**: `GET /TrackingCategories`

#### Parameters

| Parameter          | Required | Description                                                                                                   | Example                 |
| ------------------ | :------: | ------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                                                    | `"YOUR_XERO_TENANT_ID"` |
| `include_archived` |    ✗     | e.g. includeArchived=true - Categories and options with a status of ARCHIVED will be included in the response | `True`                  |
| `order`            |    ✗     | Order by an any element                                                                                       | `"Name ASC"`            |
| `where`            |    ✗     | Filter by an any element                                                                                      | `"Status==\"ACTIVE\""`  |

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
res = client.tracking_categories.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    include_archived=True,
    order="Name ASC",
    where='Status=="ACTIVE"',
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
res = await client.tracking_categories.list(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    include_archived=True,
    order="Name ASC",
    where='Status=="ACTIVE"',
)
```

#### Response

##### Type

[TrackingCategories](/xero_accounting_py/types/models/tracking_categories.py)

##### Example

```python
{}
```

### Retrieves specific tracking categories and options using a unique tracking category Id <a name="get"></a>

**API Endpoint**: `GET /TrackingCategories/{TrackingCategoryID}`

#### Parameters

| Parameter              | Required | Description                              | Example                                  |
| ---------------------- | :------: | ---------------------------------------- | ---------------------------------------- |
| `tracking_category_id` |    ✓     | Unique identifier for a TrackingCategory | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`       |    ✓     | Xero identifier for Tenant               | `"YOUR_XERO_TENANT_ID"`                  |

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
res = client.tracking_categories.get(
    tracking_category_id="00000000-0000-0000-0000-000000000000",
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
res = await client.tracking_categories.get(
    tracking_category_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[TrackingCategories](/xero_accounting_py/types/models/tracking_categories.py)

##### Example

```python
{}
```

### Updates a specific tracking category <a name="update"></a>

**API Endpoint**: `POST /TrackingCategories/{TrackingCategoryID}`

#### Parameters

| Parameter                   | Required | Description                                                                           | Example                                  |
| --------------------------- | :------: | ------------------------------------------------------------------------------------- | ---------------------------------------- |
| `tracking_category_id_path` |    ✓     | Unique identifier for a TrackingCategory                                              | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`            |    ✓     | Xero identifier for Tenant                                                            | `"YOUR_XERO_TENANT_ID"`                  |
| `name`                      |    ✗     | The name of the tracking category e.g. Department, Region (max length = 100)          | `"string"`                               |
| `option`                    |    ✗     | The option name of the tracking option e.g. East, West (max length = 100)             | `"string"`                               |
| `options`                   |    ✗     | See Tracking Options                                                                  | `[{}]`                                   |
| `status`                    |    ✗     | The status of a tracking category                                                     | `"ACTIVE"`                               |
| `tracking_category_id`      |    ✗     | The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `tracking_option_id`        |    ✗     | The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f   | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

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
res = client.tracking_categories.update(
    tracking_category_id_path="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    name="Avengers",
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
res = await client.tracking_categories.update(
    tracking_category_id_path="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    name="Avengers",
)
```

#### Response

##### Type

[TrackingCategories](/xero_accounting_py/types/models/tracking_categories.py)

##### Example

```python
{}
```

### Create tracking categories <a name="create"></a>

**API Endpoint**: `PUT /TrackingCategories`

#### Parameters

| Parameter              | Required | Description                                                                           | Example                                  |
| ---------------------- | :------: | ------------------------------------------------------------------------------------- | ---------------------------------------- |
| `xero_tenant_id`       |    ✓     | Xero identifier for Tenant                                                            | `"YOUR_XERO_TENANT_ID"`                  |
| `name`                 |    ✗     | The name of the tracking category e.g. Department, Region (max length = 100)          | `"string"`                               |
| `option`               |    ✗     | The option name of the tracking option e.g. East, West (max length = 100)             | `"string"`                               |
| `options`              |    ✗     | See Tracking Options                                                                  | `[{}]`                                   |
| `status`               |    ✗     | The status of a tracking category                                                     | `"ACTIVE"`                               |
| `tracking_category_id` |    ✗     | The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `tracking_option_id`   |    ✗     | The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f   | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

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
res = client.tracking_categories.create(xero_tenant_id="YOUR_XERO_TENANT_ID")
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
res = await client.tracking_categories.create(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Response

##### Type

[TrackingCategories](/xero_accounting_py/types/models/tracking_categories.py)

##### Example

```python
{}
```

## Submodules

- [options](options/README.md) - options

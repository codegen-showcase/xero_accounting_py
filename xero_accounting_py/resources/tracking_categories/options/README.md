# tracking_categories.options

## Module Functions

### Deletes a specific option for a specific tracking category <a name="delete"></a>

**API Endpoint**: `DELETE /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID}`

#### Parameters

| Parameter              | Required | Description                              | Example                                  |
| ---------------------- | :------: | ---------------------------------------- | ---------------------------------------- |
| `tracking_category_id` |    ✓     | Unique identifier for a TrackingCategory | `"00000000-0000-0000-0000-000000000000"` |
| `tracking_option_id`   |    ✓     | Unique identifier for a Tracking Option  | `"00000000-0000-0000-0000-000000000000"` |
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
res = client.tracking_categories.options.delete(
    tracking_category_id="00000000-0000-0000-0000-000000000000",
    tracking_option_id="00000000-0000-0000-0000-000000000000",
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
res = await client.tracking_categories.options.delete(
    tracking_category_id="00000000-0000-0000-0000-000000000000",
    tracking_option_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[TrackingOptions](/xero_accounting_py/types/models/tracking_options.py)

##### Example

```python
{}
```

### Updates a specific option for a specific tracking category <a name="update"></a>

**API Endpoint**: `POST /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID}`

#### Parameters

| Parameter                   | Required | Description                                                                         | Example                                  |
| --------------------------- | :------: | ----------------------------------------------------------------------------------- | ---------------------------------------- |
| `tracking_category_id_path` |    ✓     | Unique identifier for a TrackingCategory                                            | `"00000000-0000-0000-0000-000000000000"` |
| `tracking_option_id_path`   |    ✓     | Unique identifier for a Tracking Option                                             | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`            |    ✓     | Xero identifier for Tenant                                                          | `"YOUR_XERO_TENANT_ID"`                  |
| `name`                      |    ✗     | The name of the tracking option e.g. Marketing, East (max length = 100)             | `"string"`                               |
| `status`                    |    ✗     | The status of a tracking option                                                     | `"ACTIVE"`                               |
| `tracking_category_id`      |    ✗     | Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9             | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `tracking_option_id`        |    ✗     | The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

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
res = client.tracking_categories.options.update(
    tracking_category_id_path="00000000-0000-0000-0000-000000000000",
    tracking_option_id_path="00000000-0000-0000-0000-000000000000",
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
res = await client.tracking_categories.options.update(
    tracking_category_id_path="00000000-0000-0000-0000-000000000000",
    tracking_option_id_path="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[TrackingOptions](/xero_accounting_py/types/models/tracking_options.py)

##### Example

```python
{}
```

### Creates options for a specific tracking category <a name="create"></a>

**API Endpoint**: `PUT /TrackingCategories/{TrackingCategoryID}/Options`

#### Parameters

| Parameter                   | Required | Description                                                                         | Example                                  |
| --------------------------- | :------: | ----------------------------------------------------------------------------------- | ---------------------------------------- |
| `tracking_category_id_path` |    ✓     | Unique identifier for a TrackingCategory                                            | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id`            |    ✓     | Xero identifier for Tenant                                                          | `"YOUR_XERO_TENANT_ID"`                  |
| `name`                      |    ✗     | The name of the tracking option e.g. Marketing, East (max length = 100)             | `"string"`                               |
| `status`                    |    ✗     | The status of a tracking option                                                     | `"ACTIVE"`                               |
| `tracking_category_id`      |    ✗     | Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9             | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `tracking_option_id`        |    ✗     | The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

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
res = client.tracking_categories.options.create(
    tracking_category_id_path="00000000-0000-0000-0000-000000000000",
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
res = await client.tracking_categories.options.create(
    tracking_category_id_path="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[TrackingOptions](/xero_accounting_py/types/models/tracking_options.py)

##### Example

```python
{}
```

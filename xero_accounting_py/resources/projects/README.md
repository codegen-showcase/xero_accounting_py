# projects

## Module Functions

### Retrieves all projects <a name="list"></a>

Allows you to retrieve, create and update projects.

**API Endpoint**: `GET /Projects`

#### Parameters

| Parameter        | Required | Description                                                                                                                            | Example                                    |
| ---------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                                             | `"string"`                                 |
| `contact_id`     |    ✗     | Filter for projects for a specific contact                                                                                             | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"`   |
| `page`           |    ✗     | set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.                             | `1`                                        |
| `page_size`      |    ✗     | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | `100`                                      |
| `project_ids`    |    ✗     | Search for all projects that match a comma separated list of projectIds                                                                | `["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"]` |
| `states`         |    ✗     | Filter for projects in a particular state (INPROGRESS or CLOSED)                                                                       | `"string"`                                 |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.list(xero_tenant_id="string", page=1, page_size=100)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.list(xero_tenant_id="string", page=1, page_size=100)
```

#### Response

##### Type

[Projects](/xero_accounting_py/types/models/projects.py)

##### Example

```python
{}
```

### Retrieves a single project <a name="get"></a>

Allows you to retrieve a specific project using the projectId

**API Endpoint**: `GET /Projects/{projectId}`

#### Parameters

| Parameter        | Required | Description                                                                      | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                       | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.get(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", xero_tenant_id="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.get(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", xero_tenant_id="string"
)
```

#### Response

##### Type

[Project](/xero_accounting_py/types/models/project.py)

##### Example

```python
{"contact_id": "01234567-89ab-cdef-0123-456789abcdef", "currency_code": "AUD", "deadline_utc": "2019-12-10T12:59:59Z", "minutes_logged": 0, "minutes_to_be_invoiced": 0, "name": "New Kitchen", "project_id": "254553fa-2be8-4991-bd5e-70a97ea12ef8", "status": "INPROGRESS"}
```

### creates a project for the specified contact <a name="patch"></a>

Allows you to update a specific projects.

**API Endpoint**: `PATCH /Projects/{projectId}`

#### Parameters

| Parameter        | Required | Description                                                                      | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `status`         |    ✓     |                                                                                  | `"INPROGRESS"`                           |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                       | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.patch(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    status="INPROGRESS",
    xero_tenant_id="string",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.patch(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    status="INPROGRESS",
    xero_tenant_id="string",
)
```

### Create one or more new projects <a name="create"></a>

**API Endpoint**: `POST /Projects`

#### Parameters

| Parameter         | Required | Description                                                 | Example                                  |
| ----------------- | :------: | ----------------------------------------------------------- | ---------------------------------------- |
| `name`            |    ✓     | Name of the project.                                        | `"New Kitchen"`                          |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant                                  | `"string"`                               |
| `contact_id`      |    ✗     | Identifier of the contact this project was created for.     | `"01234567-89ab-cdef-0123-456789abcdef"` |
| `deadline_utc`    |    ✗     | Deadline for the project. UTC Date Time in ISO-8601 format. | `"2019-12-10T12:59:59Z"`                 |
| `estimate_amount` |    ✗     |                                                             | `1.0`                                    |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.create(
    name="New Kitchen",
    xero_tenant_id="string",
    contact_id="00000000-0000-0000-000-000000000000",
    deadline_utc="2019-12-10T12:59:59Z",
    estimate_amount=99.99,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.create(
    name="New Kitchen",
    xero_tenant_id="string",
    contact_id="00000000-0000-0000-000-000000000000",
    deadline_utc="2019-12-10T12:59:59Z",
    estimate_amount=99.99,
)
```

#### Response

##### Type

[Project](/xero_accounting_py/types/models/project.py)

##### Example

```python
{"contact_id": "01234567-89ab-cdef-0123-456789abcdef", "currency_code": "AUD", "deadline_utc": "2019-12-10T12:59:59Z", "minutes_logged": 0, "minutes_to_be_invoiced": 0, "name": "New Kitchen", "project_id": "254553fa-2be8-4991-bd5e-70a97ea12ef8", "status": "INPROGRESS"}
```

### Updates a specific project <a name="update"></a>

Allows you to update a specific projects.

**API Endpoint**: `PUT /Projects/{projectId}`

#### Parameters

| Parameter         | Required | Description                                                                      | Example                                  |
| ----------------- | :------: | -------------------------------------------------------------------------------- | ---------------------------------------- |
| `name`            |    ✓     | Name of the project.                                                             | `"New Kitchen"`                          |
| `project_id`      |    ✓     | You can specify an individual project by appending the projectId to the endpoint | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant                                                       | `"string"`                               |
| `contact_id`      |    ✗     | Identifier of the contact this project was created for.                          | `"01234567-89ab-cdef-0123-456789abcdef"` |
| `deadline_utc`    |    ✗     | Deadline for the project. UTC Date Time in ISO-8601 format.                      | `"2019-12-10T12:59:59Z"`                 |
| `estimate_amount` |    ✗     |                                                                                  | `1.0`                                    |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.update(
    name="New Kitchen",
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    contact_id="01234567-89ab-cdef-0123-456789abcdef",
    deadline_utc="2017-04-23T18:25:43.511Z",
    estimate_amount=99.99,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.update(
    name="New Kitchen",
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    contact_id="01234567-89ab-cdef-0123-456789abcdef",
    deadline_utc="2017-04-23T18:25:43.511Z",
    estimate_amount=99.99,
)
```

## Submodules

- [projects_users](projects_users/README.md) - projects_users
- [tasks](tasks/README.md) - tasks
- [time](time/README.md) - time

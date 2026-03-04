# projects.projects1.tasks

## Module Functions

### Allows you to delete a task <a name="delete"></a>

Allows you to delete a specific task

**API Endpoint**: `DELETE /Projects/{projectId}/Tasks/{taskId}`

#### Parameters

| Parameter        | Required | Description                                                                      | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `task_id`        |    ✓     | You can specify an individual task by appending the id to the endpoint           | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                       | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.projects1.tasks.delete(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.projects1.tasks.delete(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

### Retrieves all project tasks <a name="list"></a>

Allows you to retrieve a specific project

**API Endpoint**: `GET /Projects/{projectId}/Tasks`

#### Parameters

| Parameter        | Required | Description                                                                                                                            | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint                                                       | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                                             | `"string"`                               |
| `charge_type`    |    ✗     |                                                                                                                                        | `"FIXED"`                                |
| `page`           |    ✗     | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.                             | `1`                                      |
| `page_size`      |    ✗     | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | `10`                                     |
| `task_ids`       |    ✗     | Search for all tasks that match a comma separated list of taskIds, i.e. GET https://.../tasks?taskIds={taskID},{taskID}                | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.projects1.tasks.list(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    page=1,
    page_size=10,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.projects1.tasks.list(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    page=1,
    page_size=10,
)
```

#### Response

##### Type

[Tasks](/xero_accounting_py/types/models/tasks.py)

##### Example

```python
{}
```

### Retrieves a single project task <a name="get"></a>

Allows you to retrieve a specific project

**API Endpoint**: `GET /Projects/{projectId}/Tasks/{taskId}`

#### Parameters

| Parameter        | Required | Description                                                                                                     | Example                                  |
| ---------------- | :------: | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint                                | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `task_id`        |    ✓     | You can specify an individual task by appending the taskId to the endpoint, i.e. GET https://.../tasks/{taskID} | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                                      | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.projects1.tasks.get(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.projects1.tasks.get(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

#### Response

##### Type

[Task](/xero_accounting_py/types/models/task.py)

##### Example

```python
{"project_id": "00000000-0000-0000-000-000000000000", "task_id": "00000000-0000-0000-000-000000000000"}
```

### Allows you to create a task <a name="create"></a>

Allows you to create a specific task

**API Endpoint**: `POST /Projects/{projectId}/Tasks`

#### Parameters

| Parameter          | Required | Description                                    | Example                                  |
| ------------------ | :------: | ---------------------------------------------- | ---------------------------------------- |
| `charge_type`      |    ✓     |                                                | `"FIXED"`                                |
| `name`             |    ✓     | Name of the task. Max length 100 characters.   | `"string"`                               |
| `project_id`       |    ✓     | You can create a task on a specified projectId | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `rate`             |    ✓     |                                                | `{"currency": "AUD", "value": 1.0}`      |
| `└─ currency`      |    ✗     |                                                | `"AUD"`                                  |
| `└─ value`         |    ✗     |                                                | `1.0`                                    |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                     | `"string"`                               |
| `estimate_minutes` |    ✗     | An estimated time to perform the task          | `123`                                    |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.projects1.tasks.create(
    charge_type="TIME",
    name="Demolition",
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    rate={"currency": "AUD", "value": 20.0},
    xero_tenant_id="string",
    estimate_minutes=12000,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.projects1.tasks.create(
    charge_type="TIME",
    name="Demolition",
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    rate={"currency": "AUD", "value": 20.0},
    xero_tenant_id="string",
    estimate_minutes=12000,
)
```

#### Response

##### Type

[Task](/xero_accounting_py/types/models/task.py)

##### Example

```python
{"project_id": "00000000-0000-0000-000-000000000000", "task_id": "00000000-0000-0000-000-000000000000"}
```

### Allows you to update a task <a name="update"></a>

Allows you to update a specific task

**API Endpoint**: `PUT /Projects/{projectId}/Tasks/{taskId}`

#### Parameters

| Parameter          | Required | Description                                                                      | Example                                  |
| ------------------ | :------: | -------------------------------------------------------------------------------- | ---------------------------------------- |
| `charge_type`      |    ✓     |                                                                                  | `"FIXED"`                                |
| `name`             |    ✓     | Name of the task. Max length 100 characters.                                     | `"string"`                               |
| `project_id`       |    ✓     | You can specify an individual project by appending the projectId to the endpoint | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `rate`             |    ✓     |                                                                                  | `{"currency": "AUD", "value": 1.0}`      |
| `└─ currency`      |    ✗     |                                                                                  | `"AUD"`                                  |
| `└─ value`         |    ✗     |                                                                                  | `1.0`                                    |
| `task_id`          |    ✓     | You can specify an individual task by appending the id to the endpoint           | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id`   |    ✓     | Xero identifier for Tenant                                                       | `"string"`                               |
| `estimate_minutes` |    ✗     | An estimated time to perform the task                                            | `123`                                    |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.projects1.tasks.update(
    charge_type="TIME",
    name="Demolition",
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    rate={"currency": "AUD", "value": 20.0},
    task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    estimate_minutes=12000,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.projects1.tasks.update(
    charge_type="TIME",
    name="Demolition",
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    rate={"currency": "AUD", "value": 20.0},
    task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    estimate_minutes=12000,
)
```

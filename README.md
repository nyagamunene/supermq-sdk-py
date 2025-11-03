## SuperMQ Python SDK

[![Testing](https://github.com/absmach/supermq-sdk-py/actions/workflows/python-testing.yml/badge.svg?branch=main)](https://github.com/absmach/supermq-sdk-py/actions/workflows/python-testing.yml)
[![Check SDK documentation](https://github.com/absmach/supermq-sdk-py/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/absmach/supermq-sdk-py/actions/workflows/docs.yml)

This is the SuperMQ Python SDK, a Python client library for [SuperMQ](https://github.com/absmach/supermq) - Event-driven Infrastructure for Modern Cloud, and [Magistrala](https://github.com/absmach/magistrala) - a scalable IoT platform. 

The SDK provides Python bindings for interacting with HTTP APIs for managing users, domains, IoT devices (clients), channels, groups, messaging, rules, alarms, and more. It includes auto-generated Swagger clients for both SuperMQ event-driven services and Magistrala IoT services.

## Features

- **User Management**: Create, update, and manage users with authentication
- **Domain Management**: Multi-tenancy support with domain creation and management
- **Client Management**: IoT device/client provisioning and lifecycle management
- **Channel Management**: Communication channel setup and configuration
- **Group Management**: Hierarchical organization of clients and channels
- **Connections**: Establish publish/subscribe relationships between clients and channels
- **Messaging**: Send and receive messages via HTTP adapter (SuperMQ)
- **Rules Engine**: Create and manage data processing rules (Magistrala)
- **Reports**: Generate PDF reports from IoT sensor data (Magistrala)
- **Alarms**: Monitor and manage alarm conditions (Magistrala)
- **Role-Based Access Control**: Fine-grained permissions for domains, clients, and groups

## Requirements

- Python 3.9 or higher
- SuperMQ (Event-driven Infrastructure) and/or Magistrala (IoT platform) running locally or accessible via network

## Installation

### From Source

1. Clone the repository:
```sh
git clone https://github.com/absmach/supermq-sdk-py.git
cd supermq-sdk-py
```

2. Install in a virtual environment:
```sh
python -m venv magistralaVenv
source magistralaVenv/bin/activate  # On Windows: magistralaVenv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

**Note:** You may see warnings about missing `swagger_client` modules when importing the SDK. These warnings are expected and harmless - the SDK will set unavailable services to `None`. The warnings occur because individual service clients share the same package name and cannot all be installed simultaneously.

## Quick Start

The SDK provides two ways to interact with the services:

### Option 1: Simplified SDK Interface (Recommended for Beginners)

```python
from supermq import SDK

# Initialize SDK with default URL
sdk = SDK(default_url="http://localhost")

# Create a user
try:
    response = sdk.users.create_user(
        body={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "credentials": {
                "username": "johndoe",
                "secret": "password123"
            },
            "tags": ["demo"],
            "status": "enabled"
        }
    )
    print(f"User created with ID: {response.id}")
    
    # Login and get token
    token_response = sdk.users.issue_token(
        body={
            "identity": "johndoe",
            "secret": "password123"
        }
    )
    
    # Set token for all services
    sdk.set_token(token_response.access_token)
    
    # Now you can use any service with authentication
    # Create a domain
    domain_response = sdk.domains.domains_post(
        body={"name": "my-domain", "route": "my-route"}
    )
    print(f"Domain created with ID: {domain_response.id}")
    
except Exception as e:
    print(f"Error: {e}")
```

### Option 2: Direct Swagger Client Access (Advanced Users)

For more control, you can directly load and configure individual API clients:

```python
import sys
import os

# Add the SDK to your path
sdk_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, sdk_root)

def load_api(package_path, api_name):
    """Dynamically load API client, config, and API class"""
    package = __import__(f"{package_path}.swagger_client.api.{api_name}_api", 
                        fromlist=[''])
    api_client = getattr(__import__(f"{package_path}.swagger_client", 
                        fromlist=['']), 'ApiClient')
    config = getattr(__import__(f"{package_path}.swagger_client", 
                    fromlist=['']), 'Configuration')
    api_class = getattr(package, f"{api_name.title().replace('_', '')}Api")
    return api_client, config, api_class

# Initialize Users API
default_url = "http://localhost"
UsersApiClient, UsersConfig, UsersApi = load_api('supermq/users', 'users')
users_config = UsersConfig()
users_config.host = default_url + ":9002"
users_api = UsersApi(UsersApiClient(users_config))

# Create a user
try:
    response = users_api.create_user(
        body={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "credentials": {
                "username": "johndoe",
                "secret": "password123"
            },
            "tags": ["demo"],
            "status": "enabled"
        }
    )
    print(f"User created with ID: {response.id}")
except Exception as e:
    print(f"Error: {e}")
```

## Examples

A comprehensive example demonstrating all SDK features is available in the `examples/` directory.

### Prerequisites

Before running the examples, ensure Magistrala is running. In the Magistrala project root folder:

```bash
make run args="-d"
```

This starts all required services in detached mode.

### Running the Examples

```sh
cd examples
pip install -r requirements.txt
python examples.py
```

### What the Example Demonstrates

The `examples.py` file shows a complete end-to-end workflow:

1. **User authentication and token management**
2. **Domain creation and management** (active and disabled domains)
3. **Client (device) management** - Creates 10 clients (8 enabled, 2 disabled)
4. **Channel management** - Creates 10 channels (8 enabled, 2 disabled)
5. **Group hierarchy** - Builds a 10-level cascading group structure
6. **Group assignments** - Assigns clients and channels to groups
7. **Connections** - Establishes client-channel connections (publish/subscribe)
8. **Rules creation** - Different output types (channels, save_senml, alarms, save_remote_pg)
9. **Messaging operations** - Sends 50 SenML temperature readings via HTTP
10. **Report generation** - Generates PDF reports from sensor data
11. **Alarm management** - Lists, acknowledges, assigns, and resolves alarms
12. **Update operations** - Updates users, clients, channels, and groups
13. **Domain roles** - Creates roles with different permission levels
14. **User invitations** - Sends invitations for role assignments
15. **Client and group roles** - Fine-grained access control

### Expected Output

The script provides detailed progress for each operation:
- ✓ for successful operations
- ⚠ for warnings or skipped operations
- Error messages for failed operations
- A comprehensive summary at the end

**Note**: The script creates resources but does not delete them. Random credentials are generated for each run.

## Project Structure

```
supermq-sdk-py/
├── supermq/              # SuperMQ event-driven infrastructure services
│   ├── auth/             # Authentication service (with swagger_client/docs/)
│   ├── channels/         # Channels and connections (with swagger_client/docs/)
│   ├── clients/          # IoT clients/devices (with swagger_client/docs/)
│   ├── domains/          # Multi-tenancy domains (with swagger_client/docs/)
│   ├── groups/           # Hierarchical groups (with swagger_client/docs/)
│   ├── http/             # HTTP messaging adapter (with swagger_client/docs/)
│   ├── journal/          # Event journal (with swagger_client/docs/)
│   └── users/            # User management (with swagger_client/docs/)
├── magistrala/           # Magistrala IoT platform services
│   ├── alarms/           # Alarm management (with swagger_client/docs/)
│   ├── bootstrap/        # Device bootstrapping (with swagger_client/docs/)
│   ├── notifiers/        # Notification service (with swagger_client/docs/)
│   ├── readers/          # Message reading (with swagger_client/docs/)
│   ├── reports/          # Report generation (with swagger_client/docs/)
│   └── rules/            # Rules engine (with swagger_client/docs/)
├── examples/             # Usage examples
│   ├── examples.py       # Comprehensive example
│   └── requirements.txt  # Example dependencies
└── setup.py              # Package setup

Note: Each service directory contains auto-generated Swagger client code
with comprehensive API documentation in the swagger_client/docs/ subdirectory.
```

## API Services and Ports

The SDK connects to the following services:

### SuperMQ Event-driven Infrastructure Services

| Service    | Port | Description                          | API Documentation |
|------------|------|--------------------------------------|-------------------|
| Users      | 9002 | User management and authentication   | [UsersApi](supermq/users/docs/UsersApi.md) |
| Domains    | 9003 | Multi-tenancy domain management      | [DomainsApi](supermq/domains/docs/DomainsApi.md) |
| Groups     | 9004 | Hierarchical group organization      | [GroupsApi](supermq/groups/docs/GroupsApi.md) |
| Channels   | 9005 | Communication channel management     | [ChannelsApi](supermq/channels/docs/ChannelsApi.md) |
| Clients    | 9006 | IoT device/client management         | [ClientsApi](supermq/clients/docs/ClientsApi.md) |
| HTTP       | 8008 | HTTP messaging adapter               | [MessagesApi](supermq/http/docs/MessagesApi.md) |

### Magistrala IoT Platform Services

| Service    | Port | Description                          | API Documentation |
|------------|------|--------------------------------------|-------------------|
| Rules      | 9008 | Rules engine for data processing     | [RulesApi](magistrala/rules/docs/RulesApi.md) |
| Readers    | 9011 | Message reading and querying         | [ReadersApi](magistrala/readers/docs/ReadersApi.md) |
| Bootstrap  | 9013 | Device provisioning and bootstrap    | [ConfigsApi](magistrala/bootstrap/docs/ConfigsApi.md) |
| Reports    | 9017 | PDF report generation                | [ReportsApi](magistrala/reports/docs/ReportsApi.md) |
| Alarms     | 8050 | Alarm monitoring and management      | [AlarmsApi](magistrala/alarms/docs/AlarmsApi.md) |

## Documentation

### API Reference (Auto-Generated Swagger Documentation)

Each service includes comprehensive auto-generated API documentation:

#### SuperMQ Services
- **Users API**: [Documentation](supermq/users/docs/) - User management, authentication, profiles
- **Domains API**: [Documentation](supermq/domains/docs/) - Domain management, roles, invitations
- **Clients API**: [Documentation](supermq/clients/docs/) - IoT client/device management
- **Channels API**: [Documentation](supermq/channels/docs/) - Channel management, connections
- **Groups API**: [Documentation](supermq/groups/docs/) - Group hierarchy and organization
- **HTTP API**: [Documentation](supermq/http/docs/) - HTTP messaging adapter
- **Auth API**: [Documentation](supermq/auth/docs/) - Authentication and authorization
- **Journal API**: [Documentation](supermq/journal/docs/) - Event journaling

#### Magistrala Services
- **Alarms API**: [Documentation](magistrala/alarms/docs/) - Alarm monitoring and management
- **Bootstrap API**: [Documentation](magistrala/bootstrap/docs/) - Device bootstrapping
- **Readers API**: [Documentation](magistrala/readers/docs/) - Message reading and querying
- **Reports API**: [Documentation](magistrala/reports/docs/) - Report generation
- **Rules API**: [Documentation](magistrala/rules/docs/) - Rules engine
- **Notifiers API**: [Documentation](magistrala/notifiers/docs/) - Notification service

## Contributing

Thank you for your interest in SuperMQ and the desire to contribute!

1. Take a look at our [open issues](https://github.com/absmach/supermq-sdk-py/issues). The [good-first-issue](https://github.com/absmach/supermq-sdk-py/labels/good-first-issue) label is specifically for issues that are great for getting started.
2. Check out the [contribution guide](CONTRIBUTING.md) to learn more about our style and conventions.
3. Make your changes compatible with our workflow.

## Community

- [SuperMQ Documentation](https://docs.supermq.abstractmachines.fr/)
- [Magistrala Documentation](https://docs.magistrala.abstractmachines.fr/)
- [GitHub Discussions](https://github.com/absmach/supermq/discussions)
- [Discord](https://discord.gg/supermq)

## Professional Support

Professional support for SuperMQ and Magistrala is available through [Abstract Machines](https://abstractmachines.fr).

For enterprise deployments, custom integrations, or professional services, please contact the team directly.

## License

[Apache-2.0](LICENSE)

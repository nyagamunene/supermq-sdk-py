# Examples File

## Summary

The examples directory contains a comprehensive workflow demonstration using Swagger Codegen generated SDKs for both **SuperMQ** and **Magistrala** services.

## File: `examples.py`

This file demonstrates a complete end-to-end workflow showing how SuperMQ and Magistrala services work together.

### SuperMQ Services (Core Platform)
- **Users API** - User account management, authentication, authorization
- **Clients API** - Client (device) management (renamed from "Things")
- **Channels API** - Communication channels and connections
- **Groups API** - Group management and membership
- **Domains API** - Domain management and multi-tenancy

### Magistrala Services (Advanced Features)
- **Bootstrap API** - Secure device provisioning and configuration
- **Notifiers API** - Event notifications and subscriptions
- **Readers API** - Historical message data retrieval
- **Reports API** - Automated report generation
- **Rules API** - Event-driven automation rules

### Workflow Steps

The examples follow a logical workflow:

1. **User Management** - Create user account and obtain authentication token
2. **Domain Setup** - Create a domain for multi-tenancy
3. **Client Management** - Create IoT devices (clients)
4. **Channel Management** - Create communication channels and connect clients
5. **Group Management** - Organize clients into groups
6. **Bootstrap Configuration** - Set up device provisioning (Magistrala)
7. **Notification Setup** - Subscribe to channel events (Magistrala)
8. **Message Reading** - Access historical data (Magistrala)
9. **Report Configuration** - Schedule automated reports (Magistrala)
10. **Automation Rules** - Create event-driven rules (Magistrala)

### Key Features

- **Complete workflow** from user creation to automation rules
- **Dependency handling** - Shows how Magistrala depends on SuperMQ entities
- **Error handling** with try-except blocks
- **Informative output** with step-by-step progress
- **Real-world scenario** - Temperature sensor monitoring system
- **Production-ready** - Includes all necessary configurations

## Usage

### Prerequisites

Before running the examples, ensure you have:

1. **SuperMQ and Magistrala services running** with all required microservices
2. **Installed the generated SDKs** (see Installation section below)
3. **Network connectivity** to the service endpoints

### Installation

Install all required service SDKs:

```bash
# SuperMQ services
cd supermq/users && pip install -e . && cd ../..
cd supermq/clients && pip install -e . && cd ../..
cd supermq/channels && pip install -e . && cd ../..
cd supermq/groups && pip install -e . && cd ../..
cd supermq/domains && pip install -e . && cd ../..

# Magistrala services
cd magistrala/bootstrap && pip install -e . && cd ../..
cd magistrala/notifiers && pip install -e . && cd ../..
cd magistrala/readers && pip install -e . && cd ../..
cd magistrala/reports && pip install -e . && cd ../..
cd magistrala/rules && pip install -e . && cd ../..
```

### Running Examples

```bash
# Navigate to examples directory
cd examples

# Run the complete workflow
python examples.py
```

### Expected Output

The script will:
- Print progress for each step
- Show ✓ for successful operations
- Show ✗ for failed operations with error messages
- Display a summary at the end with all created resource IDs

## Configuration

### Service URLs

The examples use default localhost URLs. To use different hosts or ports, modify the configuration section:

```python
default_url = "http://localhost"  # Change to your server URL

# SuperMQ service ports (default)
users_config.host = default_url + ":9002"
clients_config.host = default_url + ":9000"
# ... etc

# Magistrala service ports (default)
bootstrap_config.host = default_url + ":9013"
notifiers_config.host = default_url + ":9014"
# ... etc
```

### User Credentials

Modify the email and password at the beginning of the script:

```python
email = "user@example.com"  # Change to your email
password = "securepassword123"  # Change to your password
```

## Understanding the Workflow

### Why Magistrala Depends on SuperMQ

Magistrala services are built on top of SuperMQ's core infrastructure:

- **Bootstrap** needs `client_id` to provision devices
- **Notifiers** subscribe to `channel_id` events
- **Readers** read messages from `channel_id`
- **Reports** analyze data from `channel_id`
- **Rules** monitor activity on `channel_id`

All Magistrala operations require:
1. A valid **authentication token** (from SuperMQ Users API)
2. A **domain_id** (from SuperMQ Domains API)
3. Entity IDs like **client_id** and **channel_id**

### Complete IoT Platform Flow

```
SuperMQ (Core)          Magistrala (Advanced)
├── Users               
│   └── token ──────────┬──> Bootstrap (uses token)
├── Domains             │
│   └── domain_id ──────┼──> Reports (uses domain_id)
├── Clients             │   └── Rules (uses domain_id)
│   └── client_id ──────┼──> Bootstrap (maps device)
└── Channels            │
    └── channel_id ─────┴──> Notifiers (subscribes)
                           └──> Readers (queries)
                           └──> Reports (analyzes)
                           └──> Rules (monitors)
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'supermq.users.swagger_client'
   ```
   **Solution**: Install the SDK: `cd supermq/users && pip install -e .`

2. **Connection Refused**
   ```
   Error: Connection refused to localhost:9002
   ```
   **Solution**: Ensure SuperMQ services are running. Check with `docker ps` or service status.

3. **Authentication Errors**
   ```
   Error 401: Unauthorized
   ```
   **Solution**: Token may be invalid or expired. Re-run user login to get a fresh token.

4. **Resource Already Exists**
   ```
   Error 409: Conflict
   ```
   **Solution**: Resource with same email/name exists. Change the identifier or delete existing resource.

5. **Method Not Found**
   ```
   AttributeError: 'UsersApi' object has no attribute 'create_user_0'
   ```
   **Solution**: Method names depend on OpenAPI spec. Check `supermq/users/docs/UsersApi.md` for correct method names.

## Important Notes

1. **Error Handling**: All operations use try-except blocks. Errors are expected if services aren't running or resources already exist.

2. **Method Names**: Exact method names depend on OpenAPI specifications. Check generated docs in each service's `docs/` folder.

3. **Resource Cleanup**: The script creates resources but doesn't delete them. You may want to add cleanup steps or manually delete resources.

4. **Generated Code**: The SDKs are auto-generated. For custom behavior, consider creating wrapper classes.

5. **Dependencies**: Each SDK has its own requirements.txt. Common dependencies include urllib3, python-dateutil, and certifi.

## Documentation References

For detailed API documentation, see:
- **SuperMQ Services**: `supermq/<service>/docs/`
- **Magistrala Services**: `magistrala/<service>/docs/`
- **OpenAPI Specs**: Original YAML files in SuperMQ and Magistrala repositories

## Support

For issues with:
- **Generated SDK code**: Check OpenAPI specification and regenerate if needed
- **API behavior**: Refer to service documentation
- **Example code**: These examples are templates; adjust based on your OpenAPI spec

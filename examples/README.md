# SuperMQ SDK Examples

This directory contains a comprehensive example demonstrating the SuperMQ and Magistrala Python SDK usage.

## Prerequisites

Before running the examples, you need to have Magistrala running. In the Magistrala project root folder, run:

```bash
make run args="-d"
```

This will start all required services in detached mode.

## Setup

1. **Create a Python virtual environment** (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
# or
venv\Scripts\activate  # On Windows
```

2. **Navigate to the examples directory**:

```bash
cd examples
```

3. **Install required dependencies**:

```bash
# Install all dependencies
pip install -r requirements.txt
```

## Running the Examples

```bash
python examples.py
```

The script will demonstrate:
- User authentication and token management
- Domain creation and management
- Client (device) creation and configuration
- Channel creation and client connections
- Group hierarchy management
- Rules creation with different output types
- Messaging operations with SenML format
- Report generation from sensor data
- Alarm management and acknowledgment
- Update operations for various entities
- Domain roles and invitations
- Client and group role management

## What the Example Does

The `examples.py` file shows a complete end-to-end workflow:

1. Creates a user and obtains authentication token
2. Creates domains (active and disabled)
3. Creates 10 clients (8 enabled, 2 disabled)
4. Creates 10 channels (8 enabled, 2 disabled)
5. Connects clients to channels with publish/subscribe permissions
6. Creates a cascading group hierarchy (10 groups)
7. Creates rules for message processing (channels, save_senml, alarms, save_remote_pg)
8. Sends 50 temperature sensor readings via HTTP
9. Generates PDF reports from sensor data
10. Lists and manages alarms triggered by threshold rules
11. Demonstrates update operations for users, clients, channels, and groups
12. Creates domain roles with different permission levels
13. Sends invitations to users for role assignments
14. Creates and manages client and group roles

## Expected Output

The script will print progress for each operation with:
- ✓ for successful operations
- ⚠ for warnings or skipped operations
- Error messages for failed operations
- A comprehensive summary at the end

## Notes

- All operations include proper error handling
- The script creates resources but does not delete them
- Random credentials are generated for each run
- Service availability is checked before operations

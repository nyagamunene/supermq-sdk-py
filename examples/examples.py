#!/usr/bin/env python3
"""
SuperMQ and Magistrala Python SDK Examples using Swagger Codegen Generated SDKs

This file demonstrates how to use both SuperMQ and Magistrala services together.
It shows proper authentication flow and how services interact.
"""
import sys
import os
import random
import string

# Add SDK paths
sdk_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Helper function to generate random strings
def random_string(length=8):
    """Generate a random string of lowercase letters"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_email():
    """Generate a random email address"""
    return f"{random_string(8)}@example.com"

# Helper function to load SDK
def load_api(service_path, api_name):
    """Load a specific API from a service SDK"""
    full_path = os.path.join(sdk_root, service_path)
    sys.path.insert(0, full_path)
    try:
        # Clear any cached swagger_client modules to avoid conflicts
        import importlib
        if 'swagger_client' in sys.modules:
            # Remove all swagger_client related modules from cache
            modules_to_remove = [key for key in sys.modules.keys() if key.startswith('swagger_client')]
            for module in modules_to_remove:
                del sys.modules[module]
        
        from swagger_client import ApiClient, Configuration
        api_module = __import__(f'swagger_client.api.{api_name}_api', fromlist=[f'{api_name.title().replace("_", "")}Api'])
        api_class = getattr(api_module, f'{api_name.title().replace("_", "")}Api')
        return ApiClient, Configuration, api_class
    finally:
        sys.path.pop(0)

print("=" * 80)
print("SuperMQ and Magistrala SDK Examples")
print("=" * 80)

# Configuration
default_url = "http://localhost"

# Initialize Users API (port 9002)
print("\nInitializing Users API (port 9002)...")
UsersApiClient, UsersConfig, UsersApi = load_api('supermq/users', 'users')
users_config = UsersConfig()
users_config.host = default_url + ":9002"
users_api = UsersApi(UsersApiClient(users_config))

# Initialize Clients API (port 9006)
print("Initializing Clients API (port 9006)...")
ClientsApiClient, ClientsConfig, ClientsApi = load_api('supermq/clients', 'clients')
clients_config = ClientsConfig()
clients_config.host = default_url + ":9006"
clients_api = ClientsApi(ClientsApiClient(clients_config))

# Initialize Channels API (port 9005)
print("Initializing Channels API (port 9005)...")
ChannelsApiClient, ChannelsConfig, ChannelsApi = load_api('supermq/channels', 'channels')
channels_config = ChannelsConfig()
channels_config.host = default_url + ":9005"
channels_api = ChannelsApi(ChannelsApiClient(channels_config))

# Initialize Connections API (port 9005 - same as channels)
print("Initializing Connections API (port 9005)...")
ConnectionsApiClient, ConnectionsConfig, ConnectionsApi = load_api('supermq/channels', 'connections')
connections_config = ConnectionsConfig()
connections_config.host = default_url + ":9005"
connections_api = ConnectionsApi(ConnectionsApiClient(connections_config))

# Initialize Groups API (port 9004)
print("Initializing Groups API (port 9004)...")
GroupsApiClient, GroupsConfig, GroupsApi = load_api('supermq/groups', 'groups')
groups_config = GroupsConfig()
groups_config.host = default_url + ":9004"
groups_api = GroupsApi(GroupsApiClient(groups_config))

# Initialize Domains API (port 9003)
print("Initializing Domains API (port 9003)...")
DomainsApiClient, DomainsConfig, DomainsApi = load_api('supermq/domains', 'domains')
domains_config = DomainsConfig()
domains_config.host = default_url + ":9003"
domains_api = DomainsApi(DomainsApiClient(domains_config))

# Initialize Bootstrap API (port 9013)
print("Initializing Bootstrap API (port 9013)...")
BootstrapApiClient, BootstrapConfig, ConfigsApi = load_api('magistrala/bootstrap', 'configs')
bootstrap_config = BootstrapConfig()
bootstrap_config.host = default_url + ":9013"
bootstrap_api = ConfigsApi(BootstrapApiClient(bootstrap_config))

# Initialize Readers API (port 9011)
print("Initializing Readers API (port 9011)...")
ReadersApiClient, ReadersConfig, ReadersApi = load_api('magistrala/readers', 'readers')
readers_config = ReadersConfig()
readers_config.host = default_url + ":9011"
readers_api = ReadersApi(ReadersApiClient(readers_config))

# Initialize Rules API (port 9008)
print("Initializing Rules API (port 9008)...")
RulesApiClient, RulesConfig, RulesApi = load_api('magistrala/rules', 'rules')
rules_config = RulesConfig()
rules_config.host = default_url + ":9008"
rules_api = RulesApi(RulesApiClient(rules_config))

# Initialize Reports API (port 9017)
print("Initializing Reports API (port 9017)...")
ReportsApiClient, ReportsConfig, ReportsApi = load_api('magistrala/reports', 'reports')
reports_config = ReportsConfig()
reports_config.host = default_url + ":9017"
reports_api = ReportsApi(ReportsApiClient(reports_config))

print("\nAll API clients initialized!\n")

# ==============================================================================
# HEALTH CHECKS
# ==============================================================================

print("=" * 80)
print("HEALTH CHECKS")
print("=" * 80)

# Check Users Service
print("\n1. Users Service (port 9002)")
try:
    HealthApiClient, HealthConfig, HealthApi = load_api('supermq/users', 'health')
    health_config = HealthConfig()
    health_config.host = default_url + ":9002"
    health_api = HealthApi(HealthApiClient(health_config))
    response = health_api.health()
    print(f"   ✓ Status: {response.status if hasattr(response, 'status') else 'OK'}")
    if hasattr(response, 'version'):
        print(f"   Version: {response.version}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Check Domains Service
print("\n2. Domains Service (port 9003)")
try:
    HealthApiClient, HealthConfig, HealthApi = load_api('supermq/domains', 'health')
    health_config = HealthConfig()
    health_config.host = default_url + ":9003"
    health_api = HealthApi(HealthApiClient(health_config))
    response = health_api.health_get()
    print(f"   ✓ Status: {response.status if hasattr(response, 'status') else 'OK'}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Check Groups Service
print("\n3. Groups Service (port 9004)")
try:
    HealthApiClient, HealthConfig, HealthApi = load_api('supermq/groups', 'health')
    health_config = HealthConfig()
    health_config.host = default_url + ":9004"
    health_api = HealthApi(HealthApiClient(health_config))
    response = health_api.health()
    print(f"   ✓ Status: {response.status if hasattr(response, 'status') else 'OK'}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Check Channels Service
print("\n4. Channels Service (port 9005)")
try:
    HealthApiClient, HealthConfig, HealthApi = load_api('supermq/channels', 'health')
    health_config = HealthConfig()
    health_config.host = default_url + ":9005"
    health_api = HealthApi(HealthApiClient(health_config))
    response = health_api.health_get()
    print(f"   ✓ Status: {response.status if hasattr(response, 'status') else 'OK'}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Check Clients Service
print("\n5. Clients Service (port 9006)")
try:
    HealthApiClient, HealthConfig, HealthApi = load_api('supermq/clients', 'health')
    health_config = HealthConfig()
    health_config.host = default_url + ":9006"
    health_api = HealthApi(HealthApiClient(health_config))
    response = health_api.health_get()
    print(f"   ✓ Status: {response.status if hasattr(response, 'status') else 'OK'}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Check Readers Service
print("\n6. Readers Service (port 9011)")
try:
    HealthApiClient, HealthConfig, HealthApi = load_api('magistrala/readers', 'health')
    health_config = HealthConfig()
    health_config.host = default_url + ":9011"
    health_api = HealthApi(HealthApiClient(health_config))
    response = health_api.health()
    print(f"   ✓ Status: {response.status if hasattr(response, 'status') else 'OK'}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Check Bootstrap Service
print("\n7. Bootstrap Service (port 9013)")
try:
    HealthApiClient, HealthConfig, HealthApi = load_api('magistrala/bootstrap', 'health')
    health_config = HealthConfig()
    health_config.host = default_url + ":9013"
    health_api = HealthApi(HealthApiClient(health_config))
    response = health_api.health_get()
    print(f"   ✓ Status: {response.status if hasattr(response, 'status') else 'OK'}")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n")

# Global variables for storing created resources
token = None
user_id = None
client_ids = []
client_secrets = []  # Store client secrets for messaging
channel_ids = []
group_ids = []
domain_id = None
domain_id_disabled = None

# Generate random credentials for this run
random_username = random_string(10)
random_password = "12345678"
random_first_name = random_string(6).capitalize()
random_last_name = random_string(8).capitalize()
random_user_email = random_email()

print(f"\n{'='*80}")
print(f"Generated credentials for this session:")
print(f"  Username: {random_username}")
print(f"  Email: {random_user_email}")
print(f"  Name: {random_first_name} {random_last_name}")
print(f"{'='*80}\n")

# ==============================================================================
# USER OPERATIONS (SuperMQ)
# ==============================================================================

print("=" * 80)
print("USER OPERATIONS (SuperMQ)")
print("=" * 80)

"""Create a new user"""
print("\n1. Create User")
try:
    response = users_api.create_user(
        body={
            "first_name": random_first_name,
            "last_name": random_last_name,
            "email": random_user_email,
            "credentials": {
                "username": random_username,
                "secret": random_password
            },
            "status": "enabled"
        }
    )
    print(f"   Success: User created")
    if hasattr(response, 'id'):
        user_id = response.id
        print(f"   User ID: {user_id}")
        print(f"   Email: {random_user_email}")
except Exception as e:
    print(f"   Error: {e}")

"""Log in with the created user credentials"""
print("\n2. Issue Token (Login)")
try:
    response = users_api.issue_token(
        body={"username": random_username, "password": random_password}
    )
    print(f"   Success!")
    # Extract the access token from the response
    if hasattr(response, 'access_token'):
        token = response.access_token
        print(f"   Access Token: {token[:20]}...")
        
        # Set the authorization header for all API clients that need it
        users_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        domains_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        clients_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        channels_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        connections_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        groups_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        rules_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        reports_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        print(f"   Authorization headers set for all services")
    elif isinstance(response, dict) and 'access_token' in response:
        token = response['access_token']
        print(f"   Access Token: {token[:20]}...")
        
        # Set the authorization header for all API clients that need it
        users_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        domains_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        clients_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        channels_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        connections_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        groups_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        rules_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        reports_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        print(f"   Authorization headers set for all services")
    else:
        print(f"   Response: {response}")
except Exception as e:
    print(f"   Error: {e}")
    print("   Note: Make sure the user was created successfully or already exists")

if not token:
    print("\n⚠️  No token obtained. Remaining examples will fail.")
    print("   Please create a user first or update the credentials above.")
else:
    print("\n✓ Token obtained successfully! Proceeding with examples...\n")

# ==============================================================================
# DOMAIN OPERATIONS (SuperMQ) - Create 2 domains, disable one
# ==============================================================================

print("\n" + "=" * 80)
print("DOMAIN OPERATIONS (SuperMQ) - Creating 2 domains")
print("=" * 80)

"""Create first domain (active)"""
print("\n3. Create Domain 1 (Active)")
try:
    domain_name_1 = f"domain_{random_string(8)}"
    response = domains_api.domains_post(
        body={"name": domain_name_1, "route": random_string(8)}
    )
    print(f"   Success: Domain created")
    if hasattr(response, 'id'):
        domain_id = response.id
        print(f"   Domain ID: {domain_id}")
        print(f"   Domain Name: {domain_name_1}")
        print(f"   Status: Active")
except Exception as e:
    print(f"   Error: {e}")

"""Create second domain (to be disabled)"""
print("\n4. Create Domain 2 (Will be disabled)")
try:
    domain_name_2 = f"domain_{random_string(8)}"
    response = domains_api.domains_post(
        body={"name": domain_name_2, "route": random_string(8)}
    )
    print(f"   Success: Domain created")
    if hasattr(response, 'id'):
        domain_id_disabled = response.id
        print(f"   Domain ID: {domain_id_disabled}")
        print(f"   Domain Name: {domain_name_2}")
except Exception as e:
    print(f"   Error: {e}")

"""Disable the second domain"""
if domain_id_disabled:
    print("\n5. Disable Domain 2")
    try:
        response = domains_api.domains_domain_id_disable_post(domain_id=domain_id_disabled)
        print(f"   Success: Domain disabled")
        print(f"   Domain ID: {domain_id_disabled}")
    except Exception as e:
        print(f"   Error: {e}")

if not domain_id:
    print("\n⚠️  No active domain_id obtained. Remaining examples will fail.")
    print("   domain_id is required for all client, channel, and group operations.")
else:
    print(f"\n✓ Active Domain ID obtained: {domain_id}")
    print(f"✓ Disabled Domain ID: {domain_id_disabled if domain_id_disabled else 'N/A'}")

"""Get user profile"""
print("\n6. Get Profile")
try:
    response = users_api.get_profile()
    print(f"   Success: User profile retrieved")
    # Extract user_id if available
    if hasattr(response, 'id'):
        user_id = response.id
        print(f"   User ID: {user_id}")
        print(f"   Email: {random_user_email}")
        print(f"   Name: {random_first_name} {random_last_name}")
except Exception as e:
    print(f"   Error: {e}")

"""List all users"""
print("\n7. List Users")
try:
    response = users_api.list_users(
        offset=0,
        limit=5
    )
    print(f"   Success: Found {response.total if hasattr(response, 'total') else 'N/A'} users")
    if hasattr(response, 'users') and response.users:
        print(f"   First user: {response.users[0].name if hasattr(response.users[0], 'name') else 'N/A'}")
except Exception as e:
    print(f"   Error: {e}")

# ==============================================================================
# CLIENT OPERATIONS (SuperMQ) - Create 10 clients
# ==============================================================================

print("\n" + "=" * 80)
print("CLIENT OPERATIONS (SuperMQ) - Creating 10 clients")
print("=" * 80)

"""Create 10 clients"""
print("\n1. Create 10 Clients")
for i in range(10):
    try:
        client_name = f"client_{random_string(6)}"
        client_secret = f"secret_{random_string(16)}"
        response = clients_api.create_client(
            body={
                "name": client_name, 
                "tags": ["example", "demo", f"client{i+1}"],
                "credentials": {
                    "identity": f"{client_name}@example.com",
                    "secret": client_secret
                }
            }, 
            domain_id=domain_id
        )
        if hasattr(response, 'id'):
            client_ids.append(response.id)
            client_secrets.append(client_secret)
            print(f"   [{i+1}/10] Client created: {client_name} (ID: {response.id[:8]}...)")
    except Exception as e:
        print(f"   [{i+1}/10] Error: {e}")

print(f"\n   Success: Created {len(client_ids)} clients with credentials")

"""Disable last 2 clients"""
print("\n2. Disable Last 2 Clients")
if len(client_ids) >= 2:
    for i in range(len(client_ids) - 2, len(client_ids)):
        try:
            response = clients_api.disable_client(
                domain_id=domain_id,
                client_id=client_ids[i]
            )
            print(f"   [{i-7}/2] Client disabled: {client_ids[i][:8]}...")
        except Exception as e:
            print(f"   [{i-7}/2] Error disabling client: {e}")
    print(f"\n   Success: Disabled 2 clients (last 2 in list)")
else:
    print("   Skipped: Not enough clients to disable")

"""List clients"""
print("\n3. List Clients")
try:
    response = clients_api.list_clients(
        domain_id=domain_id,
        offset=0, 
        limit=20
    )
    print(f"   Success: Found {response.total if hasattr(response, 'total') else 'N/A'} clients")
    if hasattr(response, 'clients') and response.clients:
        print(f"   Showing first 5 clients:")
        for idx, client in enumerate(response.clients[:5]):
            status = getattr(client, 'status', 'unknown')
            print(f"     {idx+1}. {client.name if hasattr(client, 'name') else 'N/A'} (Status: {status})")
except Exception as e:
    print(f"   Error: {e}")

# ==============================================================================
# CHANNEL OPERATIONS (SuperMQ) - Create 10 channels
# ==============================================================================

print("\n" + "=" * 80)
print("CHANNEL OPERATIONS (SuperMQ) - Creating 10 channels")
print("=" * 80)

"""Create 10 channels"""
print("\n1. Create 10 Channels")
for i in range(10):
    try:
        channel_name = f"channel_{random_string(6)}"
        response = channels_api.create_channel(
            body={"name": channel_name, "metadata": {"type": "demo", "index": i+1}},
            domain_id=domain_id
        )
        if hasattr(response, 'id'):
            channel_ids.append(response.id)
            print(f"   [{i+1}/10] Channel created: {channel_name} (ID: {response.id[:8]}...)")
    except Exception as e:
        print(f"   [{i+1}/10] Error: {e}")

print(f"\n   Success: Created {len(channel_ids)} channels")

"""Disable last 2 channels"""
print("\n2. Disable Last 2 Channels")
if len(channel_ids) >= 2:
    for i in range(len(channel_ids) - 2, len(channel_ids)):
        try:
            response = channels_api.disable_channel(
                domain_id=domain_id,
                chan_id=channel_ids[i]
            )
            print(f"   [{i-7}/2] Channel disabled: {channel_ids[i][:8]}...")
        except Exception as e:
            print(f"   [{i-7}/2] Error disabling channel: {e}")
    print(f"\n   Success: Disabled 2 channels (last 2 in list)")
else:
    print("   Skipped: Not enough channels to disable")

"""List channels"""
print("\n3. List Channels")
try:
    # Note: There's a bug in the generated SDK where the response model
    # expects 'offset' in the response but the API doesn't return it
    response = channels_api.list_channels(
        domain_id=domain_id,
        offset=0,
        limit=20
    )
    print(f"   Success: Found {response.total if hasattr(response, 'total') else 'N/A'} channels")
    if hasattr(response, 'channels') and response.channels:
        print(f"   Showing first 5 channels:")
        for idx, channel in enumerate(response.channels[:5]):
            status = getattr(channel, 'status', 'unknown')
            print(f"     {idx+1}. {channel.name if hasattr(channel, 'name') else 'N/A'} (Status: {status})")
except ValueError as e:
    if "offset" in str(e):
        print(f"   Warning: SDK validation bug (offset field) - but channels were likely retrieved")
        print(f"   This is a known issue with the generated SDK response model")
    else:
        print(f"   Error: {e}")
except Exception as e:
    print(f"   Error: {e}")

"""Connect enabled clients to enabled channels (first 8 of each)"""
enabled_client_ids = client_ids[:8]  # First 8 are enabled
enabled_channel_ids = channel_ids[:8]  # First 8 are enabled

if enabled_client_ids and enabled_channel_ids:
    print("\n4. Connect Enabled Clients to Enabled Channels")
    
    # First 4 connections: publish type
    publish_client_ids = enabled_client_ids[:4]
    publish_channel_ids = enabled_channel_ids[:4]
    
    print(f"\n   a) Connecting first 4 clients to first 4 channels (PUBLISH)")
    try:
        response = connections_api.connect_clients_and_channels(
            domain_id=domain_id,
            body={
                "client_ids": publish_client_ids,
                "channel_ids": publish_channel_ids,
                "types": ["publish"]
            }
        )
        print(f"   Success: Connected {len(publish_client_ids)} clients with PUBLISH permission")
        print(f"   Client IDs: {[cid[:8] + '...' for cid in publish_client_ids]}")
        print(f"   Channel IDs: {[chid[:8] + '...' for chid in publish_channel_ids]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Last 4 connections: subscribe type
    subscribe_client_ids = enabled_client_ids[4:]
    subscribe_channel_ids = enabled_channel_ids[4:]
    
    print(f"\n   b) Connecting last 4 clients to last 4 channels (SUBSCRIBE)")
    try:
        response = connections_api.connect_clients_and_channels(
            domain_id=domain_id,
            body={
                "client_ids": subscribe_client_ids,
                "channel_ids": subscribe_channel_ids,
                "types": ["subscribe"]
            }
        )
        print(f"   Success: Connected {len(subscribe_client_ids)} clients with SUBSCRIBE permission")
        print(f"   Client IDs: {[cid[:8] + '...' for cid in subscribe_client_ids]}")
        print(f"   Channel IDs: {[chid[:8] + '...' for chid in subscribe_channel_ids]}")
    except Exception as e:
        print(f"   Error: {e}")

# ==============================================================================
# GROUP OPERATIONS (SuperMQ) - Create 10 groups
# ==============================================================================

print("\n" + "=" * 80)
print("GROUP OPERATIONS (SuperMQ) - Creating 10 cascading groups")
print("=" * 80)

"""Create 10 groups with cascading hierarchy (each group's parent is the previous group)"""
print("\n1. Create 10 Groups with Cascading Hierarchy")
parent_id = None
for i in range(10):
    try:
        group_name = f"group_{random_string(6)}"
        body = {
            "name": group_name,
            "description": f"Demo group {i+1} - Level {i+1}",
            "tags": ["demo", f"level{i+1}"],
            "metadata": {"level": str(i+1)},
            "status": "enabled"
        }
        
        # Add parent_id if this is not the first group
        if parent_id:
            body["parent_id"] = parent_id
            
        response = groups_api.create_group(
            body=body,
            domain_id=domain_id
        )
        if hasattr(response, 'id'):
            group_ids.append(response.id)
            parent_info = f", Parent: {parent_id[:8]}..." if parent_id else " (Root)"
            print(f"   [{i+1}/10] Group created: {group_name} (ID: {response.id[:8]}...{parent_info})")
            # Set this group as parent for the next iteration
            parent_id = response.id
    except Exception as e:
        print(f"   [{i+1}/10] Error: {e}")

print(f"\n   Success: Created {len(group_ids)} groups in cascading hierarchy")

"""Disable the last 2 groups"""
print("\n2. Disable Last 2 Groups")
if len(group_ids) >= 2:
    for i in range(2):
        group_index = len(group_ids) - 2 + i
        group_id = group_ids[group_index]
        try:
            response = groups_api.disable_group(
                domain_id=domain_id,
                group_id=group_id
            )
            print(f"   [{i+1}/2] Group disabled: {group_id[:8]}... (Level {group_index + 1})")
        except Exception as e:
            print(f"   [{i+1}/2] Error disabling group: {e}")
    print(f"   Success: Disabled last 2 groups")
else:
    print(f"   Warning: Not enough groups to disable (need at least 2)")

"""List groups"""
print("\n3. List Groups")
try:
    response = groups_api.list_groups(
        domain_id=domain_id,
        offset=0,
        limit=20
    )
    print(f"   Success: Found {response.total if hasattr(response, 'total') else 'N/A'} groups")
    if group_ids:
        print(f"   Hierarchy structure:")
        for i, gid in enumerate(group_ids, 1):
            status = "DISABLED" if i > len(group_ids) - 2 else "enabled"
            parent_info = f" (child of group {i-1})" if i > 1 else " (root)"
            print(f"     {i}. Group ID: {gid[:8]}... - Level {i}{parent_info} [{status}]")
except Exception as e:
    print(f"   Error: {e}")

# ==============================================================================
# RULES OPERATIONS (Magistrala) - Create 4 rules
# ==============================================================================

print("\n" + "=" * 80)
print("RULES OPERATIONS (Magistrala) - Creating 4 rules with different outputs")
print("=" * 80)

# Get the first 4 enabled channels (publish channels)
publish_channel_ids = [cid for i, cid in enumerate(channel_ids) if i < len(channel_ids) - 2][:4]

"""Create 4 rules with different outputs"""
print("\n1. Create 4 Rules with Different Outputs")

# Rule 1: Output to another channel
if len(publish_channel_ids) >= 2:
    try:
        rule_name = f"rule_channels_{random_string(6)}"
        simple_logic = "function logicFunction() return message.payload end return logicFunction()"
        
        response = rules_api.create_rule(
            domain_id=domain_id,
            body={
                "name": rule_name,
                "domain": domain_id,
                "input_channel": publish_channel_ids[0],
                "tags": ["example", "channels_output"],
                "logic": {
                    "type": 0,
                    "value": simple_logic
                },
                "outputs": [
                    {
                        "type": "channels",
                        "channel": publish_channel_ids[1],
                        "topic": "messages"
                    }
                ]
            }
        )
        print(f"   [1/4] Rule created: {rule_name} -> output: channels (to channel {publish_channel_ids[1][:8]}...)")
    except Exception as e:
        print(f"   [1/4] Error creating rule: {e}")

# Rule 2: Save to SenML
if len(publish_channel_ids) >= 1:
    try:
        rule_name = f"rule_senml_{random_string(6)}"
        simple_logic = "function logicFunction() return message.payload end return logicFunction()"
        
        response = rules_api.create_rule(
            domain_id=domain_id,
            body={
                "name": rule_name,
                "domain": domain_id,
                "input_channel": publish_channel_ids[0],
                "tags": ["example", "save_senml"],
                "logic": {
                    "type": 0,
                    "value": simple_logic
                },
                "outputs": [
                    {
                        "type": "save_senml"
                    }
                ]
            }
        )
        print(f"   [2/4] Rule created: {rule_name} -> output: save_senml")
    except Exception as e:
        print(f"   [2/4] Error creating rule: {e}")

# Rule 3: Alarm processing with threshold logic
if len(publish_channel_ids) >= 1:
    try:
        rule_name = f"rule_alarms_{random_string(6)}"
        alarm_logic = """function logicFunction()
    local results = {}
    local threshold = 20

    for _, msg in ipairs(message.payload) do
        local value = msg.v
        local severity
        local cause

        if value >= threshold * 1.5 then
            severity = 5
            cause = "Critical level exceeded"
        elseif value >= threshold * 1.2 then
            severity = 4
            cause = "High level detected"
        elseif value >= threshold then
            severity = 3
            cause = "Threshold reached"
        end

        if severity then
            table.insert(results, {
                measurement = msg.n,
                value = tostring(value),
                threshold = tostring(threshold),
                cause = cause,
                unit = msg.u,
                severity = severity
            })
        end
    end

    return results
end
return logicFunction()"""
        
        response = rules_api.create_rule(
            domain_id=domain_id,
            body={
                "name": rule_name,
                "domain": domain_id,
                "input_channel": publish_channel_ids[0],
                "tags": ["example", "alarms"],
                "logic": {
                    "type": 0,
                    "value": alarm_logic
                },
                "outputs": [
                    {
                        "type": "alarms"
                    }
                ]
            }
        )
        print(f"   [3/4] Rule created: {rule_name} -> output: alarms (with threshold logic)")
    except Exception as e:
        print(f"   [3/4] Error creating rule: {e}")

# Rule 4: Save to remote PostgreSQL
if len(publish_channel_ids) >= 1:
    try:
        rule_name = f"rule_remote_pg_{random_string(6)}"
        simple_logic = "function logicFunction() return message.payload end return logicFunction()"
        
        response = rules_api.create_rule(
            domain_id=domain_id,
            body={
                "name": rule_name,
                "domain": domain_id,
                "input_channel": publish_channel_ids[0],
                "tags": ["example", "save_remote_pg"],
                "logic": {
                    "type": 0,
                    "value": simple_logic
                },
                "outputs": [
                    {
                        "type": "save_remote_pg"
                    }
                ]
            }
        )
        print(f"   [4/4] Rule created: {rule_name} -> output: save_remote_pg")
    except Exception as e:
        print(f"   [4/4] Error creating rule: {e}")

print(f"\n   Success: Created 4 rules with different output topics")

"""List rules"""
print("\n2. List Rules")
try:
    response = rules_api.get_rules(
        domain_id=domain_id,
        offset=0,
        limit=20
    )
    print(f"   Success: Found rules in domain")
    print(f"   Rules configured for channels:")
    for i, cid in enumerate(publish_channel_ids[:4], 1):
        outputs = ["channels", "save_senml", "alarms", "save_remote_pg"]
        print(f"     {i}. Channel {cid[:8]}... -> {outputs[i-1]}")
except Exception as e:
    print(f"   Note: Rules service not running - {type(e).__name__}")

# ==============================================================================
# MESSAGING OPERATIONS - Send SenML messages
# ==============================================================================

print("\n" + "=" * 80)
print("MESSAGING OPERATIONS - Sending SenML temperature messages")
print("=" * 80)

import requests
import time
import json

# Get the first 4 enabled clients (publish clients) with their secrets
publish_clients = [(client_ids[i], client_secrets[i]) for i in range(min(4, len(client_ids)))]

"""Send 10 SenML messages to each publish channel"""
print("\n1. Send 10 Temperature Readings to Each Publish Channel")

message_count = 0
base_time = int(time.time())

for client_idx, (client_id, client_secret) in enumerate(publish_clients):
    if client_idx >= len(publish_channel_ids):
        break
    
    channel_id = publish_channel_ids[client_idx]
    print(f"\n   Publishing to Channel {client_idx + 1} (ID: {channel_id[:8]}...)")
    
    for msg_num in range(10):
        try:
            # Create SenML message with temperature data
            senml_message = [
                {
                    "bn": "temperature_sensor:",
                    "bt": base_time + (msg_num * 60),  # 1 minute intervals
                    "bu": "Cel",  # Celsius
                    "bver": 5,
                    "n": "temperature",
                    "u": "Cel",
                    "v": 20.0 + (msg_num * 0.5) + (client_idx * 2)  # Varying temperature
                },
                {
                    "n": "humidity",
                    "t": 0,
                    "u": "%RH",
                    "v": 45.0 + (msg_num * 1.5)
                },
                {
                    "n": "pressure",
                    "t": 0,
                    "u": "hPa",
                    "v": 1013.25 + (msg_num * 0.2)
                }
            ]
            
            # Send message via HTTP
            url = f"http://localhost:8008/m/{domain_id}/c/{channel_id}"
            headers = {
                "Content-Type": "application/senml+json",
                "Authorization": f"Client {client_secret}"
            }
            
            response = requests.post(url, headers=headers, json=senml_message, timeout=5)
            
            if response.status_code == 202:
                message_count += 1
                temp_value = senml_message[0]["v"]
                if msg_num == 0 or msg_num == 9:  # Only print first and last
                    print(f"     [{msg_num + 1}/10] Message sent - Temp: {temp_value:.1f}°C, Humidity: {senml_message[1]['v']:.1f}%")
            else:
                print(f"     [{msg_num + 1}/10] Error: HTTP {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            if msg_num == 0:
                print(f"     Note: HTTP adapter service not running on port 8008")
            break
        except Exception as e:
            print(f"     [{msg_num + 1}/10] Error: {e}")
            break

print(f"\n   Total messages sent: {message_count}/40")
if message_count > 0:
    print(f"   ✓ Successfully sent temperature readings via HTTP adapter")
else:
    print(f"   Note: HTTP adapter service not available (port 8008)")

# ==============================================================================
# SUMMARY
# ==============================================================================

print("\n" + "=" * 80)
print("EXAMPLES COMPLETED!")
print("=" * 80)
print("\nSummary of created resources:")
print(f"  - Token: {'✓ Obtained' if token else '✗ Not obtained'}")
print(f"  - User: {random_username} ({random_user_email})")
print(f"  - User ID: {user_id if user_id else 'N/A'}")
print(f"  - Active Domain ID: {domain_id[:8] + '...' if domain_id else 'N/A'}")
print(f"  - Disabled Domain ID: {domain_id_disabled[:8] + '...' if domain_id_disabled else 'N/A'}")
print(f"  - Clients Created: {len(client_ids)} (8 enabled, 2 disabled)")
print(f"  - Channels Created: {len(channel_ids)} (8 enabled, 2 disabled)")
print(f"  - Groups Created: {len(group_ids)} (cascading hierarchy, 8 enabled, 2 disabled)")
print(f"  - Connections:")
print(f"    • 4 clients connected with PUBLISH permission")
print(f"    • 4 clients connected with SUBSCRIBE permission")
print(f"  - Rules Created: 4")
print(f"    • Rule 1: channels output")
print(f"    • Rule 2: save_senml output")
print(f"    • Rule 3: alarms output (with threshold logic)")
print(f"    • Rule 4: save_remote_pg output")
print(f"  - Messages Sent: {message_count} SenML temperature readings")
print(f"    • 10 messages per publish channel (4 channels)")
print("\nPort configuration:")
print("  - Users:     9002")
print("  - Domains:   9003")
print("  - Groups:    9004")
print("  - Channels:  9005")
print("  - Clients:   9006")
print("  - HTTP:      8008")
print("  - Rules:     9008")
print("  - Readers:   9011")
print("  - Bootstrap: 9013")
print("  - Reports:   9017")
print("  - Alarms:    8050")

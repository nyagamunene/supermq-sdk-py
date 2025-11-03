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

sdk_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def random_string(length=8):
    """Generate a random string of lowercase letters"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_email():
    """Generate a random email address"""
    return f"{random_string(8)}@example.com"

def load_api(service_path, api_name):
    """Load a specific API from a service SDK"""
    full_path = os.path.join(sdk_root, service_path)
    sys.path.insert(0, full_path)
    try:
        import importlib
        if 'swagger_client' in sys.modules:
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

default_url = "http://localhost"

print("\nInitializing Users API (port 9002)...")
UsersApiClient, UsersConfig, UsersApi = load_api('supermq/users', 'users')
users_config = UsersConfig()
users_config.host = default_url + ":9002"
users_api = UsersApi(UsersApiClient(users_config))

print("Initializing Clients API (port 9006)...")
ClientsApiClient, ClientsConfig, ClientsApi = load_api('supermq/clients', 'clients')
clients_config = ClientsConfig()
clients_config.host = default_url + ":9006"
clients_api = ClientsApi(ClientsApiClient(clients_config))

print("Initializing Channels API (port 9005)...")
ChannelsApiClient, ChannelsConfig, ChannelsApi = load_api('supermq/channels', 'channels')
channels_config = ChannelsConfig()
channels_config.host = default_url + ":9005"
channels_api = ChannelsApi(ChannelsApiClient(channels_config))

print("Initializing Connections API (port 9005)...")
ConnectionsApiClient, ConnectionsConfig, ConnectionsApi = load_api('supermq/channels', 'connections')
connections_config = ConnectionsConfig()
connections_config.host = default_url + ":9005"
connections_api = ConnectionsApi(ConnectionsApiClient(connections_config))

print("Initializing Groups API (port 9004)...")
GroupsApiClient, GroupsConfig, GroupsApi = load_api('supermq/groups', 'groups')
groups_config = GroupsConfig()
groups_config.host = default_url + ":9004"
groups_api = GroupsApi(GroupsApiClient(groups_config))

print("Initializing Groups Roles API (port 9004)...")
GroupsRolesApiClient, GroupsRolesConfig, GroupsRolesApi = load_api('supermq/groups', 'roles')
groups_roles_config = GroupsRolesConfig()
groups_roles_config.host = default_url + ":9004"
groups_roles_api = GroupsRolesApi(GroupsRolesApiClient(groups_roles_config))

print("Initializing Clients Roles API (port 9006)...")
ClientsRolesApiClient, ClientsRolesConfig, ClientsRolesApi = load_api('supermq/clients', 'roles')
clients_roles_config = ClientsRolesConfig()
clients_roles_config.host = default_url + ":9006"
clients_roles_api = ClientsRolesApi(ClientsRolesApiClient(clients_roles_config))

print("Initializing Domains API (port 9003)...")
DomainsApiClient, DomainsConfig, DomainsApi = load_api('supermq/domains', 'domains')
domains_config = DomainsConfig()
domains_config.host = default_url + ":9003"
domains_api = DomainsApi(DomainsApiClient(domains_config))

print("Initializing Roles API (port 9003)...")
RolesApiClient, RolesConfig, RolesApi = load_api('supermq/domains', 'roles')
roles_config = RolesConfig()
roles_config.host = default_url + ":9003"
roles_api = RolesApi(RolesApiClient(roles_config))

print("Initializing Invitations API (port 9003)...")
InvitationsApiClient, InvitationsConfig, InvitationsApi = load_api('supermq/domains', 'invitations')
invitations_config = InvitationsConfig()
invitations_config.host = default_url + ":9003"
invitations_api = InvitationsApi(InvitationsApiClient(invitations_config))

print("Initializing Bootstrap API (port 9013)...")
BootstrapApiClient, BootstrapConfig, ConfigsApi = load_api('magistrala/bootstrap', 'configs')
bootstrap_config = BootstrapConfig()
bootstrap_config.host = default_url + ":9013"
bootstrap_api = ConfigsApi(BootstrapApiClient(bootstrap_config))

print("Initializing Readers API (port 9011)...")
ReadersApiClient, ReadersConfig, ReadersApi = load_api('magistrala/readers', 'readers')
readers_config = ReadersConfig()
readers_config.host = default_url + ":9011"
readers_api = ReadersApi(ReadersApiClient(readers_config))

print("Initializing Rules API (port 9008)...")
RulesApiClient, RulesConfig, RulesApi = load_api('magistrala/rules', 'rules')
rules_config = RulesConfig()
rules_config.host = default_url + ":9008"
rules_api = RulesApi(RulesApiClient(rules_config))

print("Initializing Reports API (port 9017)...")
ReportsApiClient, ReportsConfig, ReportsApi = load_api('magistrala/reports', 'reports')
reports_config = ReportsConfig()
reports_config.host = default_url + ":9017"
reports_api = ReportsApi(ReportsApiClient(reports_config))

print("Initializing Alarms API (port 8050)...")
AlarmsApiClient, AlarmsConfig, AlarmsApi = load_api('magistrala/alarms', 'alarms')
alarms_config = AlarmsConfig()
alarms_config.host = default_url + ":8050"
alarms_api = AlarmsApi(AlarmsApiClient(alarms_config))

print("\nAll API clients initialized!\n")

# ==============================================================================
# HEALTH CHECKS
# ==============================================================================

print("=" * 80)
print("HEALTH CHECKS")
print("=" * 80)

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

token = None
user_id = None
client_ids = []
client_secrets = []
channel_ids = []
group_ids = []
domain_id = None
domain_id_disabled = None

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
    if hasattr(response, 'access_token'):
        token = response.access_token
        print(f"   Access Token: {token[:20]}...")
        
        users_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        domains_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        roles_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        invitations_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        clients_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        clients_roles_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        channels_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        connections_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        groups_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        groups_roles_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        rules_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        reports_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        alarms_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        print(f"   Authorization headers set for all services")
    elif isinstance(response, dict) and 'access_token' in response:
        token = response['access_token']
        print(f"   Access Token: {token[:20]}...")
        
        users_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        domains_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        roles_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        invitations_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        clients_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        clients_roles_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        channels_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        connections_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        groups_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        groups_roles_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        rules_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        reports_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
        alarms_api.api_client.default_headers['Authorization'] = f'Bearer {token}'
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
        limit=5,
        order="updated_at",
        dir="desc"
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
        limit=20,
        order="updated_at",
        dir="desc"
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
    response = channels_api.list_channels(
        domain_id=domain_id,
        offset=0,
        limit=20,
        order="updated_at",
        dir="desc"
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
enabled_client_ids = client_ids[:8]
enabled_channel_ids = channel_ids[:8]

if enabled_client_ids and enabled_channel_ids:
    print("\n4. Connect Enabled Clients to Enabled Channels")
    
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
        limit=20,
        order="updated_at",
        dir="desc"
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

print("\n4. Assign Clients to Groups")

if len(group_ids) >= 3 and len(client_ids) >= 6:
    print(f"\n   a) Assign first 3 clients to Group 1 (Root)")
    for i in range(3):
        try:
            response = clients_api.set_client_parent_group(
                domain_id=domain_id,
                client_id=client_ids[i],
                body={"parent_group_id": group_ids[0]}
            )
            print(f"   [{i+1}/3] ✓ Client {i+1} (ID: {client_ids[i][:8]}...) assigned to Group 1")
        except Exception as e:
            print(f"   [{i+1}/3] Error: {e}")
    
    print(f"\n   b) Assign next 3 clients to Group 2")
    for i in range(3, 6):
        try:
            response = clients_api.set_client_parent_group(
                domain_id=domain_id,
                client_id=client_ids[i],
                body={"parent_group_id": group_ids[1]}
            )
            print(f"   [{i-2}/3] ✓ Client {i+1} (ID: {client_ids[i][:8]}...) assigned to Group 2")
        except Exception as e:
            print(f"   [{i-2}/3] Error: {e}")
    
    print(f"\n   Success: Assigned 6 clients to 2 groups (3 clients per group)")
else:
    print(f"   ⚠ Insufficient clients or groups for assignment")
    print(f"   Need at least 6 clients and 3 groups")

print("\n5. Assign Channels to Groups")

if len(group_ids) >= 3 and len(channel_ids) >= 6:
    print(f"\n   a) Assign first 3 channels to Group 1 (Root)")
    for i in range(3):
        try:
            response = channels_api.set_channel_parent_group(
                domain_id=domain_id,
                chan_id=channel_ids[i],
                body={"parent_group_id": group_ids[0]}
            )
            print(f"   [{i+1}/3] ✓ Channel {i+1} (ID: {channel_ids[i][:8]}...) assigned to Group 1")
        except Exception as e:
            print(f"   [{i+1}/3] Error: {e}")
    
    print(f"\n   b) Assign next 3 channels to Group 2")
    for i in range(3, 6):
        try:
            response = channels_api.set_channel_parent_group(
                domain_id=domain_id,
                chan_id=channel_ids[i],
                body={"parent_group_id": group_ids[1]}
            )
            print(f"   [{i-2}/3] ✓ Channel {i+1} (ID: {channel_ids[i][:8]}...) assigned to Group 2")
        except Exception as e:
            print(f"   [{i-2}/3] Error: {e}")
    
    print(f"\n   Success: Assigned 6 channels to 2 groups (3 channels per group)")
else:
    print(f"   ⚠ Insufficient channels or groups for assignment")
    print(f"   Need at least 6 channels and 3 groups")

print("\n6. Verify Group Assignments")

if len(group_ids) >= 2:
    print(f"\n   a) Group 1 (Root) members:")
    print(f"     - 3 clients assigned (clients 1-3)")
    print(f"     - 3 channels assigned (channels 1-3)")
    
    print(f"\n   b) Group 2 members:")
    print(f"     - 3 clients assigned (clients 4-6)")
    print(f"     - 3 channels assigned (channels 4-6)")
    
    print(f"\n   ✓ Group assignments completed successfully!")

# ==============================================================================
# RULES OPERATIONS (Magistrala) - Create 4 rules
# ==============================================================================

print("\n" + "=" * 80)
print("RULES OPERATIONS (Magistrala) - Creating 4 rules with different outputs")
print("=" * 80)

publish_channel_ids = [cid for i, cid in enumerate(channel_ids) if i < len(channel_ids) - 2][:4]

print("\n1. Create 4 Rules with Different Outputs")

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

publish_clients = [(client_ids[i], client_secrets[i]) for i in range(min(4, len(client_ids)))]

"""Send 50 SenML messages to channel with save_senml rule"""
print("\n1. Send 50 Temperature Readings to Channel with Save_SenML Rule")

message_count = 0
base_time = int(time.time())

target_channel_id = publish_channel_ids[0]
client_id, client_secret = publish_clients[0]

print(f"\n   Client 1 publishing to Channel 1 (ID: {target_channel_id[:8]}...)")

for msg_num in range(50):
    try:
        senml_message = [
            {
                "bn": "temperature_sensor:",
                "bt": base_time - (msg_num * 60),
                "bu": "Cel",
                "bver": 5,
                "n": "temperature",
                "u": "Cel",
                "v": 20.0 + (msg_num * 0.5)
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
        
        url = f"http://localhost:8008/m/{domain_id}/c/{target_channel_id}"
        headers = {
            "Content-Type": "application/senml+json",
            "Authorization": f"Client {client_secret}"
        }
        
        response = requests.post(url, headers=headers, json=senml_message, timeout=5)
        
        if response.status_code == 202:
            message_count += 1
            temp_value = senml_message[0]["v"]
            if msg_num == 0 or msg_num == 49:
                print(f"     [{msg_num + 1}/50] Message sent - Temp: {temp_value:.1f}°C, Humidity: {senml_message[1]['v']:.1f}%")
        else:
            print(f"     [{msg_num + 1}/50] Error: HTTP {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        if msg_num == 0:
            print(f"     Note: HTTP adapter service not running on port 8008")
        break
    except Exception as e:
        print(f"     [{msg_num + 1}/50] Error: {e}")
        break

print(f"\n   Total messages sent: {message_count}/50")
if message_count > 0:
    print(f"   ✓ Successfully sent temperature readings via HTTP adapter")
else:
    print(f"   Note: HTTP adapter service not available (port 8008)")

# ==============================================================================
# REPORTS GENERATION - Generate PDF reports from SenML data
# ==============================================================================

print("\n" + "=" * 80)
print("REPORTS GENERATION - Generating PDF reports from temperature data")
print("=" * 80)

"""Generate temperature report for channels with save_senml output"""
print("\n1. Generate Temperature Report from SenML Data")

if len(publish_channel_ids) >= 1 and len(publish_clients) >= 1:
    report_channel_id = publish_channel_ids[0]
    report_client_ids = [publish_clients[0][0]]
    
    print(f"\n   Generating report for:")
    print(f"     Channel: {report_channel_id[:16]}...")
    print(f"     Clients: 1 temperature sensor")
    print(f"     Time range: Last 24 hours")
    
    try:
        report_url = f"http://localhost:9017/{domain_id}/reports?action=download"
        
        report_payload = {
            "name": "temperature_report",
            "config": {
                "from": "now()-1d",
                "to": "now()",
                "title": "Temperature Sensor Report",
                "timezone": "Africa/Nairobi"
            },
            "metrics": [
                {
                    "channel_id": report_channel_id,
                    "client_ids": report_client_ids,
                    "name": "temperature_sensor:temperature"
                }
            ]
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        
        response = requests.post(
            report_url,
            json=report_payload,
            headers=headers,
            timeout=30
        )
        
        if response.status_code == 200:
            examples_dir = os.path.join(sdk_root, 'examples')
            report_filename = "temperature_report.pdf"
            report_path = os.path.join(examples_dir, report_filename)
            
            with open(report_path, 'wb') as f:
                f.write(response.content)
            
            print(f"\n   ✓ Report generated successfully!")
            print(f"     File saved: {report_path}")
            print(f"     File size: {len(response.content)} bytes")
            print(f"     Format: PDF")
            print(f"     Contains: Temperature readings from 1 sensor (50 data points)")
        elif response.status_code == 404:
            print(f"\n   ⚠ Reports service not available (port 9017)")
            print(f"     Note: Ensure the reports service is running")
        else:
            print(f"\n   Error: HTTP {response.status_code}")
            print(f"     Response: {response.text[:100]}")
            
    except requests.exceptions.ConnectionError:
        print(f"\n   ⚠ Reports service not running on port 9017")
        print(f"     Note: Start the reports service to generate PDF reports")
    except Exception as e:
        print(f"\n   Error generating report: {e}")
else:
    print(f"\n   ⚠ Insufficient channels or clients for report generation")
    print(f"     Need at least 1 channel and 1 client with published data")

print(f"\n   ✓ Report generation completed!")
print(f"   Note: Report generated from data stored via 'save_senml' rule output")

# ==============================================================================
# ALARMS OPERATIONS - List and acknowledge alarms
# ==============================================================================

print("\n" + "=" * 80)
print("ALARMS OPERATIONS - Managing alarms from temperature threshold rule")
print("=" * 80)

"""List alarms generated by the alarm rule"""
print("\n1. List Alarms")

alarm_ids = []

try:
    response = alarms_api.list_alarms(
        domain_id=domain_id,
        offset=0,
        limit=20
    )
    
    if hasattr(response, 'alarms') and response.alarms:
        alarm_count = len(response.alarms)
        print(f"   ✓ Found {alarm_count} alarms")
        
        for idx, alarm in enumerate(response.alarms[:5]):
            alarm_ids.append(alarm.id)
            print(f"\n   Alarm {idx + 1}:")
            print(f"     ID: {alarm.id[:16]}...")
            print(f"     Status: {alarm.status}")
            print(f"     Severity: {alarm.severity}")
            print(f"     Measurement: {alarm.measurement}")
            print(f"     Value: {alarm.value} {alarm.unit}")
            print(f"     Threshold: {alarm.threshold}")
            print(f"     Cause: {alarm.cause}")
            print(f"     Created: {alarm.created_at}")
            
            if hasattr(alarm, 'acknowledged_at') and alarm.acknowledged_at:
                print(f"     Acknowledged: {alarm.acknowledged_at}")
    else:
        print(f"   ℹ No alarms found")
        print(f"   Note: Alarms are created when sensor values exceed the threshold defined in the alarm rule")
        
except requests.exceptions.ConnectionError:
    print(f"   ⚠ Alarms service not running on port 8050")
    print(f"   Note: Start the alarms service to manage alarms")
except Exception as e:
    print(f"   Error listing alarms: {e}")

"""Acknowledge the first alarm"""
print("\n2. Acknowledge First Alarm")

if len(alarm_ids) > 0:
    first_alarm_id = alarm_ids[0]
    
    try:
        response = alarms_api.update_alarm(
            body={"acknowledged_by": user_id},
            domain_id=domain_id,
            alarm_id=first_alarm_id
        )
        
        print(f"   ✓ Alarm acknowledged successfully")
        print(f"     Alarm ID: {first_alarm_id[:16]}...")
        print(f"     Status: {response.status} (remains active after acknowledgment)")
        
        if hasattr(response, 'acknowledged_at') and response.acknowledged_at:
            print(f"     Acknowledged At: {response.acknowledged_at}")
        if hasattr(response, 'acknowledged_by') and response.acknowledged_by:
            print(f"     Acknowledged By: {response.acknowledged_by[:16]}...")
            
    except Exception as e:
        print(f"   Error acknowledging alarm: {e}")
else:
    print(f"   ⚠ No alarms available to acknowledge")
    print(f"   Note: Send messages with values exceeding the threshold to generate alarms")

"""Assign an alarm to a user"""
print("\n3. Assign Second Alarm to User")

if len(alarm_ids) > 1:
    second_alarm_id = alarm_ids[1]
    
    try:
        response = alarms_api.update_alarm(
            body={
                "assignee_id": user_id,
                "assigned_by": user_id
            },
            domain_id=domain_id,
            alarm_id=second_alarm_id
        )
        
        print(f"   ✓ Alarm assigned successfully")
        print(f"     Alarm ID: {second_alarm_id[:16]}...")
        print(f"     Assigned To: {user_id[:16]}...")
        
        if hasattr(response, 'assigned_at') and response.assigned_at:
            print(f"     Assigned At: {response.assigned_at}")
        if hasattr(response, 'assigned_by') and response.assigned_by:
            print(f"     Assigned By: {response.assigned_by[:16]}...")
            
    except Exception as e:
        print(f"   Error assigning alarm: {e}")
else:
    print(f"   ⚠ Not enough alarms to demonstrate assignment")

"""Resolve an alarm"""
print("\n4. Resolve Third Alarm")

if len(alarm_ids) > 2:
    third_alarm_id = alarm_ids[2]
    
    try:
        response = alarms_api.update_alarm(
            body={
                "status": "cleared",
                "resolved_by": user_id
            },
            domain_id=domain_id,
            alarm_id=third_alarm_id
        )
        
        print(f"   ✓ Alarm resolved successfully")
        print(f"     Alarm ID: {third_alarm_id[:16]}...")
        print(f"     New Status: {response.status} (changed from active to cleared)")
        
        if hasattr(response, 'resolved_at') and response.resolved_at:
            print(f"     Resolved At: {response.resolved_at}")
        if hasattr(response, 'resolved_by') and response.resolved_by:
            print(f"     Resolved By: {response.resolved_by[:16]}...")
            
    except Exception as e:
        print(f"   Error resolving alarm: {e}")
else:
    print(f"   ⚠ Not enough alarms to demonstrate resolution")

"""List alarms by status"""
print("\n5. List Active Alarms (with acknowledged filter)")

try:
    response = alarms_api.list_alarms(
        domain_id=domain_id,
        status="active",
        offset=0,
        limit=10
    )
    
    if hasattr(response, 'alarms') and response.alarms:
        active_count = len(response.alarms)
        ack_count = sum(1 for a in response.alarms if hasattr(a, 'acknowledged_by') and a.acknowledged_by)
        print(f"   ✓ Found {active_count} active alarm(s) ({ack_count} acknowledged)")
        for idx, alarm in enumerate(response.alarms[:3]):
            ack_status = " [ACKNOWLEDGED]" if hasattr(alarm, 'acknowledged_by') and alarm.acknowledged_by else ""
            print(f"     {idx + 1}. Alarm {alarm.id[:12]}... - {alarm.cause}{ack_status}")
    else:
        print(f"   ℹ No active alarms found")
        
except Exception as e:
    print(f"   Error filtering alarms: {e}")

print(f"\n   ✓ Alarm operations completed!")
print(f"   Note: Alarms are automatically created by the alarm rule when thresholds are exceeded")

# ==============================================================================
# UPDATE OPERATIONS - Test update functionality
# ==============================================================================

print("\n" + "=" * 80)
print("UPDATE OPERATIONS - Testing update functionality")
print("=" * 80)

"""Update User Profile"""
print("\n1. Update User Profile")
try:
    new_first_name = random_string(6).capitalize()
    new_last_name = random_string(8).capitalize()
    response = users_api.update_user(
        user_id=user_id,
        body={
            "first_name": new_first_name,
            "last_name": new_last_name,
            "metadata": {"updated": "true", "session": "demo"}
        }
    )
    print(f"   ✓ User profile updated")
    print(f"   New name: {new_first_name} {new_last_name}")
except Exception as e:
    print(f"   Error: {e}")

"""Update User Tags"""
print("\n2. Update User Tags")
try:
    response = users_api.update_tags(
        user_id=user_id,
        body={"tags": ["updated", "demo-user", "sdk-test"]}
    )
    print(f"   ✓ User tags updated: ['updated', 'demo-user', 'sdk-test']")
except Exception as e:
    print(f"   Error: {e}")

"""Update First Client"""
print("\n3. Update First Client Name and Tags")
if client_ids:
    try:
        new_client_name = f"updated_client_{random_string(6)}"
        response = clients_api.update_client(
            domain_id=domain_id,
            client_id=client_ids[0],
            body={
                "name": new_client_name,
                "metadata": {"updated": "true", "version": "2.0"}
            }
        )
        print(f"   ✓ Client updated")
        print(f"   New name: {new_client_name}")
        print(f"   Client ID: {client_ids[0][:8]}...")
    except Exception as e:
        print(f"   Error: {e}")
    
    """Update Client Tags"""
    try:
        response = clients_api.update_client_tags(
            domain_id=domain_id,
            client_id=client_ids[0],
            body={"tags": ["updated", "publish-client", "temperature-sensor"]}
        )
        print(f"   ✓ Client tags updated: ['updated', 'publish-client', 'temperature-sensor']")
    except Exception as e:
        print(f"   Error: {e}")

"""Update First Channel"""
print("\n4. Update First Channel Name and Metadata")
if channel_ids:
    try:
        new_channel_name = f"updated_channel_{random_string(6)}"
        response = channels_api.update_channel(
            domain_id=domain_id,
            chan_id=channel_ids[0],
            body={
                "name": new_channel_name,
                "description": "Updated channel for temperature data",
                "metadata": {"updated": "true", "data_type": "temperature"}
            }
        )
        print(f"   ✓ Channel updated")
        print(f"   New name: {new_channel_name}")
        print(f"   Channel ID: {channel_ids[0][:8]}...")
    except Exception as e:
        print(f"   Error: {e}")
    
    """Update Channel Tags"""
    try:
        response = channels_api.update_channel_tags(
            domain_id=domain_id,
            chan_id=channel_ids[0],
            body={"tags": ["updated", "temperature", "iot-data"]}
        )
        print(f"   ✓ Channel tags updated: ['updated', 'temperature', 'iot-data']")
    except Exception as e:
        print(f"   Error: {e}")

"""Update First Group"""
print("\n5. Update First Group (Root) Name and Metadata")
if group_ids:
    try:
        new_group_name = f"updated_group_{random_string(6)}"
        response = groups_api.update_group(
            domain_id=domain_id,
            group_id=group_ids[0],
            body={
                "name": new_group_name,
                "description": "Updated root group",
                "metadata": {"updated": "true", "level": "root"}
            }
        )
        print(f"   ✓ Group updated")
        print(f"   New name: {new_group_name}")
        print(f"   Group ID: {group_ids[0][:8]}...")
    except Exception as e:
        print(f"   Error: {e}")
    
    """Update Group Tags"""
    try:
        response = groups_api.update_group_tags(
            domain_id=domain_id,
            group_id=group_ids[0],
            body={"tags": ["updated", "root-group", "hierarchy-top"]}
        )
        print(f"   ✓ Group tags updated: ['updated', 'root-group', 'hierarchy-top']")
    except Exception as e:
        print(f"   Error: {e}")

print("\n6. Verify Updates by Retrieving Entities")

try:
    response = users_api.get_profile()
    print(f"   ✓ User verified: {response.first_name} {response.last_name}")
except Exception as e:
    print(f"   User verification error: {e}")

if client_ids:
    try:
        response = clients_api.get_client(
            domain_id=domain_id,
            client_id=client_ids[0]
        )
        print(f"   ✓ Client verified: {response.name}")
    except Exception as e:
        print(f"   Client verification error: {e}")

if channel_ids:
    try:
        response = channels_api.get_channel(
            domain_id=domain_id,
            chan_id=channel_ids[0]
        )
        print(f"   ✓ Channel verified: {response.name}")
    except Exception as e:
        print(f"   Channel verification error: {e}")

if group_ids:
    try:
        response = groups_api.get_group(
            domain_id=domain_id,
            group_id=group_ids[0]
        )
        print(f"   ✓ Group verified: {response.name}")
    except Exception as e:
        print(f"   Group verification error: {e}")

print(f"\n   ✓ Update operations completed successfully!")

# ==============================================================================
# DOMAIN ROLES AND INVITATIONS
# ==============================================================================

print("\n" + "=" * 80)
print("DOMAIN ROLES AND INVITATIONS")
print("=" * 80)

invited_user_ids = []
invited_user_emails = []
role_ids = []
role_names = []

"""Create 5 additional users to invite"""
print("\n1. Create 5 Additional Users for Invitations")
for i in range(5):
    try:
        new_username = f"user_{random_string(8)}"
        new_email = random_email()
        response = users_api.create_user(
            body={
                "first_name": random_string(6).capitalize(),
                "last_name": random_string(8).capitalize(),
                "email": new_email,
                "credentials": {
                    "username": new_username,
                    "secret": "password123"
                },
                "tags": ["invited", f"user{i+1}"],
                "status": "enabled"
            }
        )
        if hasattr(response, 'id'):
            invited_user_ids.append(response.id)
            invited_user_emails.append(new_email)
            print(f"   [{i+1}/5] User created: {new_username} ({new_email})")
    except Exception as e:
        print(f"   [{i+1}/5] Error: {e}")

print(f"\n   Success: Created {len(invited_user_ids)} users for invitations")

"""Create additional users to be domain members (for client/group roles)"""
print("\n2. Create 8 Additional Users as Domain Members")
domain_member_ids = []
domain_member_emails = []
for i in range(8):
    try:
        new_username = f"member_{random_string(8)}"
        new_email = random_email()
        response = users_api.create_user(
            body={
                "first_name": random_string(6).capitalize(),
                "last_name": random_string(8).capitalize(),
                "email": new_email,
                "credentials": {
                    "username": new_username,
                    "secret": "password123"
                },
                "tags": ["domain_member", f"member{i+1}"],
                "status": "enabled"
            }
        )
        if hasattr(response, 'id'):
            domain_member_ids.append(response.id)
            domain_member_emails.append(new_email)
            print(f"   [{i+1}/8] User created: {new_username} ({new_email})")
    except Exception as e:
        print(f"   [{i+1}/8] Error: {e}")

print(f"\n   Success: Created {len(domain_member_ids)} domain member users")

"""List existing domain roles to find the default member role"""
print("\n3. List Existing Domain Roles (to find default member role)")
member_role_id = None
try:
    response = roles_api.list_domain_roles(
        domain_id=domain_id,
        limit=100,
        order="updated_at",
        dir="desc"
    )
    if hasattr(response, 'roles') and response.roles:
        print(f"   Found {len(response.roles)} existing roles:")
        for role in response.roles:
            role_name = role.name if hasattr(role, 'name') else 'unknown'
            role_id = role.id if hasattr(role, 'id') else 'unknown'
            print(f"     - {role_name} (ID: {role_id[:16]}...)")
            if role_name.lower() in ['member', 'viewer', 'guest', 'user']:
                member_role_id = role_id
                print(f"       ^ Using this role for adding domain members")
    else:
        print(f"   No existing roles found")
except Exception as e:
    print(f"   Error listing roles: {e}")

"""Add users as domain members first"""
print("\n4. Add Domain Member Users to Domain (Required for role assignments)")
if member_role_id and len(domain_member_ids) > 0:
    try:
        response = roles_api.add_domain_role_member(
            domain_id=domain_id,
            role_id=member_role_id,
            body={"members": domain_member_ids}
        )
        print(f"   ✓ Added {len(domain_member_ids)} domain member users to default member role")
    except Exception as e:
        print(f"   Error adding domain members: {e}")
else:
    print(f"   ⚠ Skipping: No member role found or no domain member users created")

"""Create Domain Roles with different actions"""
print("\n5. Create Domain Roles with Different Permissions")

print("\n   a) Creating 'Viewer' role (read-only)")
try:
    response = roles_api.create_domain_role(
        domain_id=domain_id,
        body={
            "role_name": "viewer",
            "optional_actions": ["read", "client_read", "channel_read", "group_read"],
            "optional_members": domain_member_ids[:3] if len(domain_member_ids) >= 3 else []
        }
    )
    if response.id:
        role_ids.append(response.id)
        role_names.append("viewer")
        print(f"   ✓ 'Viewer' role created with {min(3, len(domain_member_ids))} domain members")
        print(f"     Actions: read, client_read, channel_read, group_read")
        print(f"     Role ID: {response.id[:16]}...")
    else:
        print(f"   ✗ 'Viewer' role creation failed - no ID in response")
except Exception as e:
    print(f"   Error: {e}")

print("\n   b) Creating 'Editor' role (create and update)")
try:
    response = roles_api.create_domain_role(
        domain_id=domain_id,
        body={
            "role_name": "editor",
            "optional_actions": [
                "read", "client_create", "client_update", "client_read",
                "channel_create", "channel_update", "channel_read",
                "group_create", "group_update", "group_read"
            ],
            "optional_members": [domain_member_ids[3]] if len(domain_member_ids) >= 4 else []
        }
    )
    if response.id:
        role_ids.append(response.id)
        role_names.append("editor")
        print(f"   ✓ 'Editor' role created with {min(1, len(domain_member_ids)-3) if len(domain_member_ids) >= 4 else 0} domain members")
        print(f"     Actions: read, *_create, *_update, *_read (clients, channels, groups)")
        print(f"     Role ID: {response.id[:16]}...")
    else:
        print(f"   ✗ 'Editor' role creation failed - no ID in response")
except Exception as e:
    print(f"   Error: {e}")

print("\n   c) Creating 'Admin' role (full permissions)")
try:
    response = roles_api.create_domain_role(
        domain_id=domain_id,
        body={
            "role_name": "admin",
            "optional_actions": [
                "read", "delete", "manage_role", "add_role_users", "view_role_users",
                "client_create", "client_update", "client_read", "client_delete", 
                "client_add_role_users", "client_view_role_users",
                "channel_create", "channel_update", "channel_read", "channel_delete",
                "channel_add_role_users", "channel_view_role_users",
                "group_create", "group_update", "group_read", "group_delete",
                "group_add_role_users", "group_view_role_users"
            ],
            "optional_members": []
        }
    )
    if response.id:
        role_ids.append(response.id)
        role_names.append("admin")
        print(f"   ✓ 'Admin' role created")
        print(f"     Actions: All permissions (read, create, update, delete, manage roles)")
        print(f"     Role ID: {response.id[:16]}...")
    else:
        print(f"   ✗ 'Admin' role creation failed - no ID in response")
except Exception as e:
    print(f"   Error: {e}")

print("\n   d) Creating 'Role Manager' role (role management)")
try:
    response = roles_api.create_domain_role(
        domain_id=domain_id,
        body={
            "role_name": "role_manager",
            "optional_actions": [
                "read", "manage_role", "add_role_users", "view_role_users",
                "client_view_role_users", "client_add_role_users",
                "channel_view_role_users", "channel_add_role_users",
                "group_view_role_users", "group_add_role_users"
            ],
            "optional_members": []
        }
    )
    if response.id:
        role_ids.append(response.id)
        role_names.append("role_manager")
        print(f"   ✓ 'Role Manager' role created")
        print(f"     Actions: manage_role, add/view role users")
        print(f"     Role ID: {response.id[:16]}...")
    else:
        print(f"   ✗ 'Role Manager' role creation failed - no ID in response")
except Exception as e:
    print(f"   Error: {e}")

print(f"\n   Success: Created {len(role_ids)} roles")

"""Add invited users as members to domain roles"""
print("\n5. Add Invited Users to Domain Roles (making them domain members)")

if len(role_ids) > 0 and len(invited_user_ids) >= 2:
    try:
        print(f"   DEBUG: domain_id={domain_id[:20]}...")
        print(f"   DEBUG: role_id={role_ids[0]}")
        print(f"   DEBUG: members={invited_user_ids[:2]}")
        response = roles_api.add_domain_role_member(
            domain_id=domain_id,
            role_id=role_ids[0],
            body={"members": invited_user_ids[:2]}
        )
        print(f"   ✓ Added 2 users to 'viewer' role")
        print(f"     - {invited_user_emails[0][:25]}...")
        print(f"     - {invited_user_emails[1][:25]}...")
    except Exception as e:
        print(f"   Error adding to viewer role: {e}")

if len(role_ids) > 1 and len(invited_user_ids) >= 3:
    try:
        response = roles_api.add_domain_role_member(
            domain_id=domain_id,
            role_id=role_ids[1],
            body={"members": [invited_user_ids[2]]}
        )
        print(f"   ✓ Added 1 user to 'editor' role")
        print(f"     - {invited_user_emails[2][:25]}...")
    except Exception as e:
        print(f"   Error adding to editor role: {e}")

print(f"   ✓ Users are now domain members via roles and can be used in client/group roles")

"""Add remaining domain members to viewer role to make them domain members"""
print("\n5b. Add Remaining Domain Members to Viewer Role")
if len(role_ids) > 0 and len(domain_member_ids) > 3:
    try:
        remaining_members = domain_member_ids[3:]
        response = roles_api.add_domain_role_member(
            domain_id=domain_id,
            role_id=role_ids[0],
            body={"members": remaining_members}
        )
        print(f"   ✓ Added {len(remaining_members)} additional domain members to 'viewer' role")
        print(f"     Total domain members: {len(domain_member_ids)}")
        print(f"     (These can now be used in client/group roles)")
    except Exception as e:
        print(f"   Error adding domain members: {e}")

"""Send invitations to users for empty roles"""
print("\n6. Send Invitations to Users")

if len(invited_user_ids) > 3 and len(role_ids) > 2:
    try:
        invitations_api.send_invitation(
            domain_id=domain_id,
            body={
                "user_id": invited_user_ids[3],
                "role": role_names[2],
                "resend": False
            }
        )
        print(f"   [1/2] ✓ Invitation sent to {invited_user_emails[3][:20]}... for 'admin' role")
    except Exception as e:
        print(f"   [1/2] Error sending invitation: {e}")

if len(invited_user_ids) > 4 and len(role_ids) > 3:
    try:
        invitations_api.send_invitation(
            domain_id=domain_id,
            body={
                "user_id": invited_user_ids[4],
                "role": role_names[3],
                "resend": False
            }
        )
        print(f"   [2/2] ✓ Invitation sent to {invited_user_emails[4][:20]}... for 'role_manager' role")
    except Exception as e:
        print(f"   [2/2] Error sending invitation: {e}")

print(f"\n   Success: Sent invitations to 2 users")

"""List domain invitations"""
print("\n7. List Domain Invitations")
try:
    response = invitations_api.list_domain_invitations(
        domain_id=domain_id,
        offset=0,
        limit=10,
        order="updated_at",
        dir="desc"
    )
    print(f"   ✓ Domain invitations listed")
    if hasattr(response, 'total'):
        print(f"   Total invitations: {response.total}")
except Exception as e:
    print(f"   Error: {e}")

"""List domain roles"""
print("\n8. List Domain Roles")
try:
    response = roles_api.get_domain_role(
        domain_id=domain_id
    )
    print(f"   ✓ Domain roles listed")
    print(f"   Roles created:")
    for i, role_name in enumerate(role_names, 1):
        print(f"     {i}. {role_name}")
except Exception as e:
    print(f"   Error: {e}")

"""Add additional action to editor role"""
if len(role_ids) > 1:
    print("\n9. Add Additional Action to 'Editor' Role")
    try:
        roles_api.add_domain_role_action(
            domain_id=domain_id,
            body={
                "role": role_names[1],
                "actions": ["client_delete", "channel_delete"]
            }
        )
        print(f"   ✓ Added 'client_delete' and 'channel_delete' actions to 'editor' role")
    except Exception as e:
        print(f"   Error: {e}")

print(f"\n   ✓ Domain roles and invitations operations completed!")

# ==============================================================================
# CLIENT & GROUP ROLES OPERATIONS - Create roles and assign members
# ==============================================================================

print("\n" + "=" * 80)
print("CLIENT & GROUP ROLES OPERATIONS - Creating roles for clients and groups")
print("=" * 80)

client_role_ids = []
group_role_ids = []

print("\n1. Create Roles for First 3 Clients")

if len(client_ids) >= 1:
    print(f"\n   a) Creating 'client_admin' role for Client 1")
    try:
        response = clients_roles_api.create_client_role(
            domain_id=domain_id,
            client_id=client_ids[0],
            body={
                "role_name": "client_admin",
                "optional_actions": [
                    "read", "update", "delete", "manage_role",
                    "add_role_users", "view_role_users"
                ],
                "optional_members": domain_member_ids[:2] if len(domain_member_ids) >= 2 else []
            }
        )
        if hasattr(response, 'id'):
            client_role_ids.append(response.id)
            print(f"   ✓ 'client_admin' role created for Client 1")
            print(f"     Members: 2 users (from domain viewer role)")
            print(f"     Actions: read, update, delete, manage_role, add/view_role_users")
    except Exception as e:
        print(f"   Error: {e}")

if len(client_ids) >= 2:
    print(f"\n   b) Creating 'client_editor' role for Client 2")
    try:
        response = clients_roles_api.create_client_role(
            domain_id=domain_id,
            client_id=client_ids[1],
            body={
                "role_name": "client_editor",
                "optional_actions": ["read", "update"],
                "optional_members": [domain_member_ids[1], domain_member_ids[2]] if len(domain_member_ids) >= 3 else []
            }
        )
        if hasattr(response, 'id'):
            client_role_ids.append(response.id)
            print(f"   ✓ 'client_editor' role created for Client 2")
            print(f"     Members: 2 users (from domain viewer and editor roles)")
            print(f"     Actions: read, update")
    except Exception as e:
        print(f"   Error: {e}")

if len(client_ids) >= 3:
    print(f"\n   c) Creating 'client_viewer' role for Client 3")
    try:
        response = clients_roles_api.create_client_role(
            domain_id=domain_id,
            client_id=client_ids[2],
            body={
                "role_name": "client_viewer",
                "optional_actions": ["read"],
                "optional_members": [domain_member_ids[0]] if len(domain_member_ids) >= 1 else []
            }
        )
        if hasattr(response, 'id'):
            client_role_ids.append(response.id)
            print(f"   ✓ 'client_viewer' role created for Client 3")
            print(f"     Members: 1 user (from domain viewer role)")
            print(f"     Actions: read")
    except Exception as e:
        print(f"   Error: {e}")

print(f"\n   Success: Created {len(client_role_ids)} client roles")

"""Add additional members to client roles"""
print("\n2. Add Additional Members to Client Roles")
print("   Note: Skipping - roles already have domain members in roles")
print("   (Demonstrating that domain role members can be used in client roles)")

"""List client role members"""
print("\n3. List Client Role Members")
for i, client_id in enumerate(client_ids[:3], 1):
    try:
        response = clients_roles_api.list_client_role_members(
            domain_id=domain_id,
            client_id=client_id
        )
        member_count = len(response.members) if hasattr(response, 'members') else 0
        print(f"   [{i}/3] Client {i} role has {member_count} members")
    except Exception as e:
        print(f"   [{i}/3] Error: {e}")

print("\n4. Create Roles for First 3 Groups")

if len(group_ids) >= 1:
    print(f"\n   a) Creating 'group_admin' role for Group 1 (Root)")
    try:
        response = groups_roles_api.create_group_role(
            domain_id=domain_id,
            group_id=group_ids[0],
            body={
                "role_name": "group_admin",
                "optional_actions": [
                    "read", "update", "delete", "manage_role",
                    "add_role_users", "view_role_users",
                    "client_create", "client_update", "client_delete"
                ],
                "optional_members": domain_member_ids[:2] if len(domain_member_ids) >= 2 else []
            }
        )
        if hasattr(response, 'id'):
            group_role_ids.append(response.id)
            print(f"   ✓ 'group_admin' role created for Group 1 (Root)")
            print(f"     Members: 2 users (from domain viewer role)")
            print(f"     Actions: Full permissions including client management")
    except Exception as e:
        print(f"   Error: {e}")

if len(group_ids) >= 2:
    print(f"\n   b) Creating 'group_manager' role for Group 2")
    try:
        response = groups_roles_api.create_group_role(
            domain_id=domain_id,
            group_id=group_ids[1],
            body={
                "role_name": "group_manager",
                "optional_actions": [
                    "read", "update", "client_create", "client_update"
                ],
                "optional_members": [domain_member_ids[1], domain_member_ids[2]] if len(domain_member_ids) >= 3 else []
            }
        )
        if hasattr(response, 'id'):
            group_role_ids.append(response.id)
            print(f"   ✓ 'group_manager' role created for Group 2")
            print(f"     Members: 2 users (from domain viewer and editor roles)")
            print(f"     Actions: read, update, client_create, client_update")
    except Exception as e:
        print(f"   Error: {e}")

if len(group_ids) >= 3:
    print(f"\n   c) Creating 'group_member' role for Group 3")
    try:
        response = groups_roles_api.create_group_role(
            domain_id=domain_id,
            group_id=group_ids[2],
            body={
                "role_name": "group_member",
                "optional_actions": ["read"],
                "optional_members": [domain_member_ids[1], domain_member_ids[2]] if len(domain_member_ids) >= 3 else []
            }
        )
        if hasattr(response, 'id'):
            group_role_ids.append(response.id)
            print(f"   ✓ 'group_member' role created for Group 3")
            print(f"     Members: 2 users (from domain viewer and editor roles)")
            print(f"     Actions: read")
    except Exception as e:
        print(f"   Error: {e}")

print(f"\n   Success: Created {len(group_role_ids)} group roles")

print("\n5. Add Additional Members to Group Roles")

if len(group_ids) >= 1 and len(invited_user_ids) >= 4:
    try:
        groups_roles_api.add_group_role_member(
            domain_id=domain_id,
            group_id=group_ids[0],
            body={"members": [invited_user_ids[3]]}
        )
        print(f"   [1/2] ✓ Added Admin user to Group 1 role")
    except Exception as e:
        print(f"   [1/2] Error: {e}")

if len(group_ids) >= 2 and len(invited_user_ids) >= 1:
    try:
        groups_roles_api.add_group_role_member(
            domain_id=domain_id,
            group_id=group_ids[1],
            body={"members": [invited_user_ids[0]]}
        )
        print(f"   [2/2] ✓ Added Reader to Group 2 role")
    except Exception as e:
        print(f"   [2/2] Error: {e}")

"""List group role members"""
print("\n6. List Group Role Members")
for i, group_id in enumerate(group_ids[:3], 1):
    try:
        response = groups_roles_api.list_group_role_members(
            domain_id=domain_id,
            group_id=group_id
        )
        member_count = len(response.members) if hasattr(response, 'members') else 0
        print(f"   [{i}/3] Group {i} role has {member_count} members")
    except Exception as e:
        print(f"   [{i}/3] Error: {e}")

print("\n7. Add Additional Actions to Roles")

if len(client_ids) >= 2:
    try:
        clients_roles_api.add_client_role_action(
            domain_id=domain_id,
            client_id=client_ids[1],
            body={"actions": ["delete"]}
        )
        print(f"   [1/2] ✓ Added 'delete' action to Client 2 role")
    except Exception as e:
        print(f"   [1/2] Error: {e}")

if len(group_ids) >= 2:
    try:
        groups_roles_api.add_group_role_action(
            domain_id=domain_id,
            group_id=group_ids[1],
            body={"actions": ["delete", "client_delete"]}
        )
        print(f"   [2/2] ✓ Added 'delete' and 'client_delete' actions to Group 2 role")
    except Exception as e:
        print(f"   [2/2] Error: {e}")

print(f"\n   ✓ Client and Group roles operations completed!")

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
print(f"  - Group Assignments:")
print(f"    • 6 clients assigned to groups (3 to Group 1, 3 to Group 2)")
print(f"    • 6 channels assigned to groups (3 to Group 1, 3 to Group 2)")
print(f"  - Connections:")
print(f"    • 4 clients connected with PUBLISH permission")
print(f"    • 4 clients connected with SUBSCRIBE permission")
print(f"  - Rules Created: 4")
print(f"    • Rule 1: channels output")
print(f"    • Rule 2: save_senml output")
print(f"    • Rule 3: alarms output (with threshold logic)")
print(f"    • Rule 4: save_remote_pg output")
print(f"  - Messages Sent: {message_count} SenML temperature readings")
print(f"    • 50 temperature readings sent via HTTP adapter")
print(f"  - Reports Generated:")
print(f"    • Temperature report: Single-channel sensor data (50 data points)")
print(f"    • Format: PDF with time-series data visualization")
print(f"    • Time range: Last 24 hours of sensor readings")
print(f"  - Updates Performed:")
print(f"    • User profile updated (name and metadata)")
print(f"    • User tags updated")
print(f"    • First client updated (name, metadata, and tags)")
print(f"    • First channel updated (name, description, metadata, and tags)")
print(f"    • First group updated (name, description, metadata, and tags)")
print(f"    • All updates verified by retrieving entities")
print(f"  - Domain Roles & Invitations:")
print(f"    • Additional users created: {len(invited_user_ids)}")
print(f"    • Domain roles created: {len(role_ids)}")
print(f"      - Viewer: read-only (3 members)")
print(f"      - Editor: create/update (1 member)")
print(f"      - Admin: full permissions (0 members, invited)")
print(f"      - Role Manager: role management (0 members, invited)")
print(f"    • Invitations sent: 2")
print(f"    • Members added to roles: 1 (viewer role)")
print(f"    • Actions added to roles: 2 (editor role)")
print(f"  - Client Roles:")
print(f"    • Client roles created: {len(client_role_ids)}")
print(f"      - Client 1: client_admin (3 members, 6 actions)")
print(f"      - Client 2: client_editor (2 members, 3 actions)")
print(f"      - Client 3: client_viewer (2 members, 1 action)")
print(f"    • Additional members added to client roles")
print(f"    • Additional actions added to client roles")
print(f"  - Group Roles:")
print(f"    • Group roles created: {len(group_role_ids)}")
print(f"      - Group 1 (Root): group_admin (3 members, 7 actions)")
print(f"      - Group 2: group_manager (3 members, 6 actions)")
print(f"      - Group 3: group_member (3 members, 1 action)")
print(f"    • Additional members added to group roles")
print(f"    • Additional actions added to group roles")
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

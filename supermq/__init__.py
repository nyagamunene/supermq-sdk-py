"""
SuperMQ Python SDK

A Python client library for SuperMQ messaging platform and Magistrala IoT platform.
Provides simplified access to all services through a unified SDK interface.
"""

import sys
import os
import logging
import importlib.util


def load_api(package_path, api_name):
    """
    Dynamically load API client, config, and API class.
    Supports both installed packages and local repo structure.
    
    Args:
        package_path: Path to the package (e.g., 'supermq.users' or 'supermq/users')
        api_name: Name of the API (e.g., 'users')
    
    Returns:
        Tuple of (ApiClient, Configuration, ApiClass)
    """
    # Normalize path separators to dots for import
    package_path = package_path.replace('/', '.')
    
    try:
        # Try standard import first (for installed packages)
        package = __import__(f"{package_path}.swagger_client.api.{api_name}_api",
                            fromlist=[''])
        api_client = getattr(__import__(f"{package_path}.swagger_client",
                            fromlist=['']), 'ApiClient')
        config = getattr(__import__(f"{package_path}.swagger_client",
                        fromlist=['']), 'Configuration')
        api_class = getattr(package, f"{api_name.title().replace('_', '')}Api")
        return api_client, config, api_class
    except (ImportError, ModuleNotFoundError):
        # Fall back to loading from local repo structure
        # Get the repo root (parent of supermq/__init__.py)
        sdk_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        service_path = os.path.join(sdk_root, package_path.replace('.', os.sep))
        swagger_path = os.path.join(service_path, 'swagger_client')
        
        if not os.path.exists(swagger_path):
            raise ImportError(f"Could not find swagger_client at {swagger_path}")
        
        # Add the service directory to sys.path so swagger_client can be imported
        parent_path = os.path.dirname(swagger_path)
        if parent_path not in sys.path:
            sys.path.insert(0, parent_path)
        
        try:
            # Now import swagger_client (it will resolve from the parent_path)
            # Need to clear any cached imports first
            if 'swagger_client' in sys.modules:
                del sys.modules['swagger_client']
            # Also clear api submodules
            to_delete = [k for k in sys.modules.keys() if k.startswith('swagger_client.')]
            for k in to_delete:
                del sys.modules[k]
            
            import swagger_client
            api_module = __import__(f"swagger_client.api.{api_name}_api", fromlist=[''])
            
            api_class_name = f"{api_name.title().replace('_', '')}Api"
            api_class = getattr(api_module, api_class_name)
            
            return swagger_client.ApiClient, swagger_client.Configuration, api_class
        finally:
            # Remove from sys.path
            if parent_path in sys.path:
                sys.path.remove(parent_path)


class SDK:
    """
    Unified SDK interface for SuperMQ and Magistrala services.
    
    Usage:
        from supermq import SDK
        
        sdk = SDK(default_url="http://localhost")
        
        # Create a user
        response = sdk.users.create_user(body={...})
        
        # Create a client
        response = sdk.clients.create_client(domain_id="...", body={...})
        
        # Send a message
        # Use the HTTP adapter directly or via requests library
    """
    
    def __init__(self, default_url="http://localhost"):
        """
        Initialize the SDK with service URLs.
        
        Args:
            default_url: Base URL for services (default: "http://localhost")
        """
        self.default_url = default_url
        self._token = None
        
        # Initialize SuperMQ services
        self._init_users()
        self._init_domains()
        self._init_clients()
        self._init_channels()
        self._init_connections()
        self._init_groups()
        self._init_groups_roles()
        self._init_clients_roles()
        self._init_roles()
        self._init_invitations()
        self._init_http()
        
        # Initialize Magistrala services
        self._init_bootstrap()
        self._init_readers()
        self._init_rules()
        self._init_reports()
        self._init_alarms()
        
        # Initialize Health APIs for all services
        self._init_health_apis()
    
    def set_token(self, token):
        """
        Set authentication token for all services.
        
        Args:
            token: Bearer token obtained from login
        """
        self._token = token
        
        # Set authorization header for all initialized services
        services = [
            self.users, self.domains, self.clients, self.channels,
            self.connections, self.groups, self.groups_roles,
            self.clients_roles, self.roles, self.invitations,
            self.bootstrap, self.readers, self.rules, self.reports, self.alarms
        ]
        
        for service in services:
            if service and hasattr(service, 'api_client'):
                service.api_client.default_headers['Authorization'] = f'Bearer {token}'
    
    def _init_users(self):
        """Initialize Users API (port 9002)"""
        try:
            UsersApiClient, UsersConfig, UsersApi = load_api('supermq.users', 'users')
            config = UsersConfig()
            config.host = self.default_url + ":9002"
            self.users = UsersApi(UsersApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Users API: {e}")
            self.users = None
    
    def _init_domains(self):
        """Initialize Domains API (port 9003)"""
        try:
            DomainsApiClient, DomainsConfig, DomainsApi = load_api('supermq.domains', 'domains')
            config = DomainsConfig()
            config.host = self.default_url + ":9003"
            self.domains = DomainsApi(DomainsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Domains API: {e}")
            self.domains = None
    
    def _init_clients(self):
        """Initialize Clients API (port 9006)"""
        try:
            ClientsApiClient, ClientsConfig, ClientsApi = load_api('supermq.clients', 'clients')
            config = ClientsConfig()
            config.host = self.default_url + ":9006"
            self.clients = ClientsApi(ClientsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Clients API: {e}")
            self.clients = None
    
    def _init_channels(self):
        """Initialize Channels API (port 9005)"""
        try:
            ChannelsApiClient, ChannelsConfig, ChannelsApi = load_api('supermq.channels', 'channels')
            config = ChannelsConfig()
            config.host = self.default_url + ":9005"
            self.channels = ChannelsApi(ChannelsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Channels API: {e}")
            self.channels = None
    
    def _init_connections(self):
        """Initialize Connections API (port 9005)"""
        try:
            ConnectionsApiClient, ConnectionsConfig, ConnectionsApi = load_api('supermq.channels', 'connections')
            config = ConnectionsConfig()
            config.host = self.default_url + ":9005"
            self.connections = ConnectionsApi(ConnectionsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Connections API: {e}")
            self.connections = None
    
    def _init_groups(self):
        """Initialize Groups API (port 9004)"""
        try:
            GroupsApiClient, GroupsConfig, GroupsApi = load_api('supermq.groups', 'groups')
            config = GroupsConfig()
            config.host = self.default_url + ":9004"
            self.groups = GroupsApi(GroupsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Groups API: {e}")
            self.groups = None
    
    def _init_groups_roles(self):
        """Initialize Groups Roles API (port 9004)"""
        try:
            GroupsRolesApiClient, GroupsRolesConfig, GroupsRolesApi = load_api('supermq.groups', 'roles')
            config = GroupsRolesConfig()
            config.host = self.default_url + ":9004"
            self.groups_roles = GroupsRolesApi(GroupsRolesApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Groups Roles API: {e}")
            self.groups_roles = None
    
    def _init_clients_roles(self):
        """Initialize Clients Roles API (port 9006)"""
        try:
            ClientsRolesApiClient, ClientsRolesConfig, ClientsRolesApi = load_api('supermq.clients', 'roles')
            config = ClientsRolesConfig()
            config.host = self.default_url + ":9006"
            self.clients_roles = ClientsRolesApi(ClientsRolesApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Clients Roles API: {e}")
            self.clients_roles = None
    
    def _init_roles(self):
        """Initialize Roles API (port 9003)"""
        try:
            RolesApiClient, RolesConfig, RolesApi = load_api('supermq.domains', 'roles')
            config = RolesConfig()
            config.host = self.default_url + ":9003"
            self.roles = RolesApi(RolesApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Roles API: {e}")
            self.roles = None
    
    def _init_invitations(self):
        """Initialize Invitations API (port 9003)"""
        try:
            InvitationsApiClient, InvitationsConfig, InvitationsApi = load_api('supermq.domains', 'invitations')
            config = InvitationsConfig()
            config.host = self.default_url + ":9003"
            self.invitations = InvitationsApi(InvitationsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Invitations API: {e}")
            self.invitations = None
    
    def _init_http(self):
        """Initialize HTTP Messaging API (port 8008)"""
        try:
            HttpApiClient, HttpConfig, MessagesApi = load_api('supermq.http', 'messages')
            config = HttpConfig()
            config.host = self.default_url + ":8008"
            self.http = MessagesApi(HttpApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize HTTP API: {e}")
            self.http = None
    
    def _init_bootstrap(self):
        """Initialize Bootstrap API (port 9013)"""
        try:
            BootstrapApiClient, BootstrapConfig, ConfigsApi = load_api('magistrala.bootstrap', 'configs')
            config = BootstrapConfig()
            config.host = self.default_url + ":9013"
            self.bootstrap = ConfigsApi(BootstrapApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Bootstrap API: {e}")
            self.bootstrap = None
    
    def _init_readers(self):
        """Initialize Readers API (port 9011)"""
        try:
            ReadersApiClient, ReadersConfig, ReadersApi = load_api('magistrala.readers', 'readers')
            config = ReadersConfig()
            config.host = self.default_url + ":9011"
            self.readers = ReadersApi(ReadersApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Readers API: {e}")
            self.readers = None
    
    def _init_rules(self):
        """Initialize Rules API (port 9008)"""
        try:
            RulesApiClient, RulesConfig, RulesApi = load_api('magistrala.rules', 'rules')
            config = RulesConfig()
            config.host = self.default_url + ":9008"
            self.rules = RulesApi(RulesApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Rules API: {e}")
            self.rules = None
    
    def _init_reports(self):
        """Initialize Reports API (port 9017)"""
        try:
            ReportsApiClient, ReportsConfig, ReportsApi = load_api('magistrala.reports', 'reports')
            config = ReportsConfig()
            config.host = self.default_url + ":9017"
            self.reports = ReportsApi(ReportsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Reports API: {e}")
            self.reports = None
    
    def _init_alarms(self):
        """Initialize Alarms API (port 8050)"""
        try:
            AlarmsApiClient, AlarmsConfig, AlarmsApi = load_api('magistrala.alarms', 'alarms')
            config = AlarmsConfig()
            config.host = self.default_url + ":8050"
            self.alarms = AlarmsApi(AlarmsApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Alarms API: {e}")
            self.alarms = None
    
    def _init_health_apis(self):
        """Initialize Health APIs for all services"""
        # SuperMQ Health APIs
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('supermq.users', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9002"
            self.users_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Users Health API: {e}")
            self.users_health = None
        
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('supermq.domains', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9003"
            self.domains_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Domains Health API: {e}")
            self.domains_health = None
        
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('supermq.groups', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9004"
            self.groups_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Groups Health API: {e}")
            self.groups_health = None
        
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('supermq.channels', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9005"
            self.channels_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Channels Health API: {e}")
            self.channels_health = None
        
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('supermq.clients', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9006"
            self.clients_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Clients Health API: {e}")
            self.clients_health = None
        
        # Magistrala Health APIs
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('magistrala.readers', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9011"
            self.readers_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Readers Health API: {e}")
            self.readers_health = None
        
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('magistrala.bootstrap', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9013"
            self.bootstrap_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Bootstrap Health API: {e}")
            self.bootstrap_health = None


__all__ = ['SDK', 'load_api']

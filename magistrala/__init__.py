"""
Magistrala Python SDK

A Python client library for Magistrala IoT platform.
Provides simplified access to IoT-specific services through a unified SDK interface.
"""

import sys
import os
import logging


def load_api(package_path, api_name):
    """
    Dynamically load API client, config, and API class.
    Supports both installed packages and local repo structure.
    
    Args:
        package_path: Path to the package (e.g., 'magistrala.rules' or 'magistrala/rules')
        api_name: Name of the API (e.g., 'rules')
    
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
        # Get the repo root (parent of magistrala/__init__.py)
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
    Unified SDK interface for Magistrala IoT platform services.
    
    Usage:
        from magistrala import SDK
        
        sdk = SDK(default_url="http://localhost", token="your_bearer_token")
        
        # Create a rule
        response = sdk.rules.create_rule(domain_id="...", body={...})
        
        # Generate a report
        response = sdk.reports.generate_report(domain_id="...", body={...})
        
        # List alarms
        response = sdk.alarms.list_alarms(domain_id="...", offset=0, limit=10)
    """
    
    def __init__(self, default_url="http://localhost", token=None):
        """
        Initialize the Magistrala SDK with service URLs.
        
        Args:
            default_url: Base URL for services (default: "http://localhost")
            token: Optional bearer token for authentication
        """
        self.default_url = default_url
        self._token = token
        
        # Initialize Magistrala IoT services
        self._init_bootstrap()
        self._init_readers()
        self._init_rules()
        self._init_reports()
        self._init_alarms()
        self._init_notifiers()
        
        # Initialize health check APIs
        self._init_bootstrap_health()
        self._init_readers_health()
        
        # Set token if provided
        if token:
            self.set_token(token)
    
    def set_token(self, token):
        """
        Set authentication token for all services.
        
        Args:
            token: Bearer token obtained from SuperMQ authentication
        """
        self._token = token
        
        # Set authorization header for all initialized services
        services = [
            self.bootstrap, self.readers, self.rules, 
            self.reports, self.alarms, self.notifiers
        ]
        
        for service in services:
            if service and hasattr(service, 'api_client'):
                service.api_client.default_headers['Authorization'] = f'Bearer {token}'
    
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
    
    def _init_notifiers(self):
        """Initialize Notifiers API (port 9014)"""
        try:
            NotifiersApiClient, NotifiersConfig, NotifiersApi = load_api('magistrala.notifiers', 'notifiers')
            config = NotifiersConfig()
            config.host = self.default_url + ":9014"
            self.notifiers = NotifiersApi(NotifiersApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Notifiers API: {e}")
            self.notifiers = None
    
    def _init_bootstrap_health(self):
        """Initialize Bootstrap Health API (port 9013)"""
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('magistrala.bootstrap', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9013"
            self.bootstrap_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Bootstrap Health API: {e}")
            self.bootstrap_health = None
    
    def _init_readers_health(self):
        """Initialize Readers Health API (port 9011)"""
        try:
            HealthApiClient, HealthConfig, HealthApi = load_api('magistrala.readers', 'health')
            config = HealthConfig()
            config.host = self.default_url + ":9011"
            self.readers_health = HealthApi(HealthApiClient(config))
        except Exception as e:
            logging.getLogger(__name__).debug(f"Could not initialize Readers Health API: {e}")
            self.readers_health = None


__all__ = ['SDK', 'load_api']

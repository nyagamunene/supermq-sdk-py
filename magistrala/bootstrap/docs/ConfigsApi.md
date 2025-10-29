# swagger_client.ConfigsApi

All URIs are relative to *http://localhost:9013*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config**](ConfigsApi.md#create_config) | **POST** /{domainID}/clients/configs | Adds new config
[**get_bootstrap_config**](ConfigsApi.md#get_bootstrap_config) | **GET** /clients/bootstrap/{externalId} | Retrieves configuration.
[**get_config**](ConfigsApi.md#get_config) | **GET** /{domainID}/clients/configs/{configID} | Retrieves config info (with channels).
[**get_configs**](ConfigsApi.md#get_configs) | **GET** /{domainID}/clients/configs | Retrieves managed configs
[**get_secure_bootstrap_config**](ConfigsApi.md#get_secure_bootstrap_config) | **GET** /clients/bootstrap/secure/{externalId} | Retrieves configuration.
[**remove_config**](ConfigsApi.md#remove_config) | **DELETE** /{domainID}/clients/configs/{configID} | Removes a Config
[**update_config**](ConfigsApi.md#update_config) | **PUT** /{domainID}/clients/configs/{configID} | Updates config info
[**update_config_certs**](ConfigsApi.md#update_config_certs) | **PATCH** /{domainID}/clients/configs/certs/{configID} | Updates certs
[**update_config_connections**](ConfigsApi.md#update_config_connections) | **PUT** /{domainID}/clients/configs/connections/{configID} | Updates channels the client is connected to
[**update_config_state**](ConfigsApi.md#update_config_state) | **PUT** /{domainID}/clients/state/{configID} | Updates Config state.

# **create_config**
> create_config(body, domain_id)

Adds new config

Adds new config to the list of config owned by user identified using the provided access token. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing the new config.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Adds new config
    api_instance.create_config(body, domain_id)
except ApiException as e:
    print("Exception when calling ConfigsApi->create_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing the new config. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bootstrap_config**
> BootstrapConfig get_bootstrap_config(external_id)

Retrieves configuration.

Retrieves a configuration with given external ID and external key. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
external_id = 'external_id_example' # str | Unique Config identifier provided by external entity.

try:
    # Retrieves configuration.
    api_response = api_instance.get_bootstrap_config(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->get_bootstrap_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| Unique Config identifier provided by external entity. | 

### Return type

[**BootstrapConfig**](BootstrapConfig.md)

### Authorization

[bootstrapAuth](../README.md#bootstrapAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> Config get_config(domain_id, config_id)

Retrieves config info (with channels).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
config_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique Config identifier. It's the ID of the corresponding Client.

try:
    # Retrieves config info (with channels).
    api_response = api_instance.get_config(domain_id, config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **config_id** | [**str**](.md)| Unique Config identifier. It&#x27;s the ID of the corresponding Client. | 

### Return type

[**Config**](Config.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configs**
> ConfigList get_configs(domain_id, limit=limit, offset=offset, state=state, name=name)

Retrieves managed configs

Retrieves a list of managed configs. Due to performance concerns, data is retrieved in subsets. The API configs must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
state = swagger_client.State() # State | A state of items (optional)
name = 'name_example' # str | Name of the config. Search by name is partial-match and case-insensitive. (optional)

try:
    # Retrieves managed configs
    api_response = api_instance.get_configs(domain_id, limit=limit, offset=offset, state=state, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->get_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **state** | [**State**](.md)| A state of items | [optional] 
 **name** | **str**| Name of the config. Search by name is partial-match and case-insensitive. | [optional] 

### Return type

[**ConfigList**](ConfigList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secure_bootstrap_config**
> BootstrapConfig get_secure_bootstrap_config(external_id)

Retrieves configuration.

Retrieves a configuration with given external ID and encrypted external key. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
external_id = 'external_id_example' # str | Unique Config identifier provided by external entity.

try:
    # Retrieves configuration.
    api_response = api_instance.get_secure_bootstrap_config(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->get_secure_bootstrap_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| Unique Config identifier provided by external entity. | 

### Return type

[**BootstrapConfig**](BootstrapConfig.md)

### Authorization

[bootstrapEncAuth](../README.md#bootstrapEncAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_config**
> remove_config(domain_id, config_id)

Removes a Config

Removes a Config. In case of successful removal the service will ensure that the removed config is disconnected from all of the SuperMQ channels. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
config_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique Config identifier. It's the ID of the corresponding Client.

try:
    # Removes a Config
    api_instance.remove_config(domain_id, config_id)
except ApiException as e:
    print("Exception when calling ConfigsApi->remove_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **config_id** | [**str**](.md)| Unique Config identifier. It&#x27;s the ID of the corresponding Client. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config**
> update_config(domain_id, config_id, body=body)

Updates config info

Update is performed by replacing the current resource data with values provided in a request payload. Note that the owner, ID, external ID, external key, SuperMQ Client ID and key cannot be changed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
config_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique Config identifier. It's the ID of the corresponding Client.
body = NULL # object | JSON-formatted document describing the updated client. (optional)

try:
    # Updates config info
    api_instance.update_config(domain_id, config_id, body=body)
except ApiException as e:
    print("Exception when calling ConfigsApi->update_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **config_id** | [**str**](.md)| Unique Config identifier. It&#x27;s the ID of the corresponding Client. | 
 **body** | [**object**](object.md)| JSON-formatted document describing the updated client. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_certs**
> ConfigUpdateCerts update_config_certs(domain_id, config_id, body=body)

Updates certs

Update is performed by replacing the current certificate data with values provided in a request payload. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
config_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique Config identifier. It's the ID of the corresponding Client.
body = NULL # object | JSON-formatted document describing the updated client. (optional)

try:
    # Updates certs
    api_response = api_instance.update_config_certs(domain_id, config_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->update_config_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **config_id** | [**str**](.md)| Unique Config identifier. It&#x27;s the ID of the corresponding Client. | 
 **body** | [**object**](object.md)| JSON-formatted document describing the updated client. | [optional] 

### Return type

[**ConfigUpdateCerts**](ConfigUpdateCerts.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_connections**
> update_config_connections(domain_id, config_id, body=body)

Updates channels the client is connected to

Update connections performs update of the channel list corresponding Client is connected to. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
config_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique Config identifier. It's the ID of the corresponding Client.
body = NULL # object | Array if IDs the client is be connected to. (optional)

try:
    # Updates channels the client is connected to
    api_instance.update_config_connections(domain_id, config_id, body=body)
except ApiException as e:
    print("Exception when calling ConfigsApi->update_config_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **config_id** | [**str**](.md)| Unique Config identifier. It&#x27;s the ID of the corresponding Client. | 
 **body** | [**object**](object.md)| Array if IDs the client is be connected to. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_state**
> update_config_state(domain_id, config_id, body=body)

Updates Config state.

Updating state represents enabling/disabling Config, i.e. connecting and disconnecting corresponding SuperMQ Client to the list of Channels. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
config_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique Config identifier. It's the ID of the corresponding Client.
body = NULL # object | Update the state of the Config. (optional)

try:
    # Updates Config state.
    api_instance.update_config_state(domain_id, config_id, body=body)
except ApiException as e:
    print("Exception when calling ConfigsApi->update_config_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **config_id** | [**str**](.md)| Unique Config identifier. It&#x27;s the ID of the corresponding Client. | 
 **body** | [**object**](object.md)| Update the state of the Config. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


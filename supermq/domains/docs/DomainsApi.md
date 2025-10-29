# swagger_client.DomainsApi

All URIs are relative to *http://localhost:9003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_domain_id_disable_post**](DomainsApi.md#domains_domain_id_disable_post) | **POST** /domains/{domainID}/disable | Disable a domain
[**domains_domain_id_enable_post**](DomainsApi.md#domains_domain_id_enable_post) | **POST** /domains/{domainID}/enable | Enables a domain
[**domains_domain_id_freeze_post**](DomainsApi.md#domains_domain_id_freeze_post) | **POST** /domains/{domainID}/freeze | Freeze a domain
[**domains_domain_id_get**](DomainsApi.md#domains_domain_id_get) | **GET** /domains/{domainID} | Retrieves domain information
[**domains_domain_id_patch**](DomainsApi.md#domains_domain_id_patch) | **PATCH** /domains/{domainID} | Updates name, metadata and tags of the domain.
[**domains_get**](DomainsApi.md#domains_get) | **GET** /domains | Retrieves list of domains.
[**domains_post**](DomainsApi.md#domains_post) | **POST** /domains | Adds new domain

# **domains_domain_id_disable_post**
> domains_domain_id_disable_post(domain_id)

Disable a domain

Disable a specific domain that is identified by the domain ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Disable a domain
    api_instance.domains_domain_id_disable_post(domain_id)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_domain_id_disable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_domain_id_enable_post**
> domains_domain_id_enable_post(domain_id)

Enables a domain

Enables a specific domain that is identified by the domain ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Enables a domain
    api_instance.domains_domain_id_enable_post(domain_id)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_domain_id_enable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_domain_id_freeze_post**
> domains_domain_id_freeze_post(domain_id)

Freeze a domain

Freeze a specific domain that is identified by the domain ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Freeze a domain
    api_instance.domains_domain_id_freeze_post(domain_id)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_domain_id_freeze_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_domain_id_get**
> Domain domains_domain_id_get(domain_id)

Retrieves domain information

Retrieves a specific domain that is identified by the domain ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Retrieves domain information
    api_response = api_instance.domains_domain_id_get(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_domain_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_domain_id_patch**
> Domain domains_domain_id_patch(body, domain_id)

Updates name, metadata and tags of the domain.

Updates name, metadata and tags of the domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainUpdate() # DomainUpdate | JSON-formated document describing the name, tags, and metadata of the domain to be updated
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Updates name, metadata and tags of the domain.
    api_response = api_instance.domains_domain_id_patch(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_domain_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainUpdate**](DomainUpdate.md)| JSON-formated document describing the name, tags, and metadata of the domain to be updated | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_get**
> DomainsPage domains_get(limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, name=name, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total)

Retrieves list of domains.

Retrieves list of domains that the user have access. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
order = 'order_example' # str | Field by which to order the results (optional)
dir = 'dir_example' # str | Direction of ordering the results. (optional)
metadata = NULL # dict(str, object) | Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. (optional)
status = 'enabled' # str | Domain status. (optional) (default to enabled)
name = 'name_example' # str | Domain's name. (optional)
actions = 'actions_example' # str | Lists domains that the user has the given actions on. Multiple actions can be specified separated by comma. (optional)
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List domains that the user has the given role ID on. (optional)
role_name = 'role_name_example' # str | List domains that the user has the given role name on. (optional)
access_type = 'access_type_example' # str | Type of access the user has on the domain. (optional)
only_total = false # bool | If true, the response will contain only the total number of domains that match the query parameters. (optional) (default to false)

try:
    # Retrieves list of domains.
    api_response = api_instance.domains_get(limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, name=name, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **order** | **str**| Field by which to order the results | [optional] 
 **dir** | **str**| Direction of ordering the results. | [optional] 
 **metadata** | [**dict(str, object)**](object.md)| Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. | [optional] 
 **status** | **str**| Domain status. | [optional] [default to enabled]
 **name** | **str**| Domain&#x27;s name. | [optional] 
 **actions** | **str**| Lists domains that the user has the given actions on. Multiple actions can be specified separated by comma. | [optional] 
 **role_id** | [**str**](.md)| List domains that the user has the given role ID on. | [optional] 
 **role_name** | **str**| List domains that the user has the given role name on. | [optional] 
 **access_type** | **str**| Type of access the user has on the domain. | [optional] 
 **only_total** | **bool**| If true, the response will contain only the total number of domains that match the query parameters. | [optional] [default to false]

### Return type

[**DomainsPage**](DomainsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_post**
> Domain domains_post(body)

Adds new domain

Adds new domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainReqObj() # DomainReqObj | JSON-formatted document describing the new domain to be registered

try:
    # Adds new domain
    api_response = api_instance.domains_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainReqObj**](DomainReqObj.md)| JSON-formatted document describing the new domain to be registered | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


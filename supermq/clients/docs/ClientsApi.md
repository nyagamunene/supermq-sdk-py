# swagger_client.ClientsApi

All URIs are relative to *http://localhost:9006*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_clients**](ClientsApi.md#bulk_create_clients) | **POST** /{domainID}/clients/bulk | Bulk provisions new clients
[**create_client**](ClientsApi.md#create_client) | **POST** /{domainID}/clients | Adds new client
[**disable_client**](ClientsApi.md#disable_client) | **POST** /{domainID}/clients/{clientID}/disable | Disables a client
[**domain_id_clients_client_id_delete**](ClientsApi.md#domain_id_clients_client_id_delete) | **DELETE** /{domainID}/clients/{clientID} | Delete client for a client with the given id.
[**enable_client**](ClientsApi.md#enable_client) | **POST** /{domainID}/clients/{clientID}/enable | Enables a client
[**get_client**](ClientsApi.md#get_client) | **GET** /{domainID}/clients/{clientID} | Retrieves client info
[**list_clients**](ClientsApi.md#list_clients) | **GET** /{domainID}/clients | Retrieves clients
[**remove_client_parent_group**](ClientsApi.md#remove_client_parent_group) | **DELETE** /{domainID}/clients/{clientID}/parent | Removes a parent group from a client.
[**set_client_parent_group**](ClientsApi.md#set_client_parent_group) | **POST** /{domainID}/clients/{clientID}/parent | Sets a parent group for a client
[**update_client**](ClientsApi.md#update_client) | **PATCH** /{domainID}/clients/{clientID} | Updates name and metadata of the client.
[**update_client_secret**](ClientsApi.md#update_client_secret) | **PATCH** /{domainID}/clients/{clientID}/secret | Updates Secret of the identified client.
[**update_client_tags**](ClientsApi.md#update_client_tags) | **PATCH** /{domainID}/clients/{clientID}/tags | Updates tags the client.

# **bulk_create_clients**
> ClientsPage bulk_create_clients(body, domain_id)

Bulk provisions new clients

Adds a list of new clients to the list of clients owned by user identified using the provided access token. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ClientReqObj()] # list[ClientReqObj] | JSON-formatted document describing the new clients.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Bulk provisions new clients
    api_response = api_instance.bulk_create_clients(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->bulk_create_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ClientReqObj]**](ClientReqObj.md)| JSON-formatted document describing the new clients. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

[**ClientsPage**](ClientsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client**
> Client create_client(body, domain_id)

Adds new client

Adds new client to the list of clients owned by user identified using the provided access token. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientReqObj() # ClientReqObj | JSON-formatted document describing the new client to be registered
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Adds new client
    api_response = api_instance.create_client(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientReqObj**](ClientReqObj.md)| JSON-formatted document describing the new client to be registered | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_client**
> Client disable_client(domain_id, client_id)

Disables a client

Disables a specific client that is identified by the client ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Disables a client
    api_response = api_instance.disable_client(domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->disable_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_id_clients_client_id_delete**
> domain_id_clients_client_id_delete(domain_id, client_id)

Delete client for a client with the given id.

Delete client removes a client with the given id from repo and removes all the policies related to this client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Delete client for a client with the given id.
    api_instance.domain_id_clients_client_id_delete(domain_id, client_id)
except ApiException as e:
    print("Exception when calling ClientsApi->domain_id_clients_client_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_client**
> Client enable_client(domain_id, client_id)

Enables a client

Enables a specific client that is identified by the client ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Enables a client
    api_response = api_instance.enable_client(domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->enable_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> Client get_client(domain_id, client_id)

Retrieves client info

Retrieves a specific client that is identified by the client ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Retrieves client info
    api_response = api_instance.get_client(domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> ClientsPage list_clients(domain_id, limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, name=name, tags=tags, id=id, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total, channel=channel, connection_type=connection_type, group=group, user=user)

Retrieves clients

Retrieves a list of clients. Due to performance concerns, data is retrieved in subsets. The API clients must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
order = 'order_example' # str | Field by which to order the results (optional)
dir = 'dir_example' # str | Direction of ordering the results. (optional)
metadata = 'metadata_example' # str | Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. (optional)
status = 'enabled' # str | Client account status. (optional) (default to enabled)
name = 'name_example' # str | Client's name. (optional)
tags = ['tags_example'] # list[str] | Client tags. (optional)
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List clients with the given ID. (optional)
actions = 'actions_example' # str | Filter by actions. Multiple actions can be specified separated by comma. (optional)
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter by role ID. (optional)
role_name = 'role_name_example' # str | Filter by role name. (optional)
access_type = 'access_type_example' # str | Type of access the user has on the client. (optional)
only_total = false # bool | If true, the response will contain only the total number of clients that match the query parameters. (optional) (default to false)
channel = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | If provided lists clients connected to a channel with the provided ID. (optional)
connection_type = 'connection_type_example' # str | If provided with channel parameter lists clients connected to the channel with the provided connection type. (optional)
group = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | If provided lists clients belonging to a group with the provided ID. (optional)
user = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | If provided lists clients associated with a user with the provided ID. Only available for admin users. (optional)

try:
    # Retrieves clients
    api_response = api_instance.list_clients(domain_id, limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, name=name, tags=tags, id=id, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total, channel=channel, connection_type=connection_type, group=group, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **order** | **str**| Field by which to order the results | [optional] 
 **dir** | **str**| Direction of ordering the results. | [optional] 
 **metadata** | **str**| Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. | [optional] 
 **status** | **str**| Client account status. | [optional] [default to enabled]
 **name** | **str**| Client&#x27;s name. | [optional] 
 **tags** | [**list[str]**](str.md)| Client tags. | [optional] 
 **id** | [**str**](.md)| List clients with the given ID. | [optional] 
 **actions** | **str**| Filter by actions. Multiple actions can be specified separated by comma. | [optional] 
 **role_id** | [**str**](.md)| Filter by role ID. | [optional] 
 **role_name** | **str**| Filter by role name. | [optional] 
 **access_type** | **str**| Type of access the user has on the client. | [optional] 
 **only_total** | **bool**| If true, the response will contain only the total number of clients that match the query parameters. | [optional] [default to false]
 **channel** | [**str**](.md)| If provided lists clients connected to a channel with the provided ID. | [optional] 
 **connection_type** | **str**| If provided with channel parameter lists clients connected to the channel with the provided connection type. | [optional] 
 **group** | [**str**](.md)| If provided lists clients belonging to a group with the provided ID. | [optional] 
 **user** | [**str**](.md)| If provided lists clients associated with a user with the provided ID. Only available for admin users. | [optional] 

### Return type

[**ClientsPage**](ClientsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_client_parent_group**
> remove_client_parent_group(body, domain_id, client_id)

Removes a parent group from a client.

Removes a parent group from a specific client that is identified by the client ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ParentGroupReqObj() # ParentGroupReqObj | JSON-formated document describing the parent group to be set to or removed from a client.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Removes a parent group from a client.
    api_instance.remove_client_parent_group(body, domain_id, client_id)
except ApiException as e:
    print("Exception when calling ClientsApi->remove_client_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParentGroupReqObj**](ParentGroupReqObj.md)| JSON-formated document describing the parent group to be set to or removed from a client. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_client_parent_group**
> set_client_parent_group(body, domain_id, client_id)

Sets a parent group for a client

Sets a parent group for a specific client that is identified by the client ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ParentGroupReqObj() # ParentGroupReqObj | JSON-formated document describing the parent group to be set to or removed from a client.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Sets a parent group for a client
    api_instance.set_client_parent_group(body, domain_id, client_id)
except ApiException as e:
    print("Exception when calling ClientsApi->set_client_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParentGroupReqObj**](ParentGroupReqObj.md)| JSON-formated document describing the parent group to be set to or removed from a client. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> Client update_client(body, domain_id, client_id)

Updates name and metadata of the client.

Update is performed by replacing the current resource data with values provided in a request payload. Note that the client's type and ID cannot be changed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientUpdate() # ClientUpdate | JSON-formated document describing the metadata and name of client to be update
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Updates name and metadata of the client.
    api_response = api_instance.update_client(body, domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->update_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientUpdate**](ClientUpdate.md)| JSON-formated document describing the metadata and name of client to be update | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_secret**
> Client update_client_secret(body, domain_id, client_id)

Updates Secret of the identified client.

Updates secret of the identified in client. Secret is updated using authorization token and the new received info. Update is performed by replacing current key with a new one. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientSecret() # ClientSecret | Secret change data. Client can change its secret.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Updates Secret of the identified client.
    api_response = api_instance.update_client_secret(body, domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->update_client_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientSecret**](ClientSecret.md)| Secret change data. Client can change its secret. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_tags**
> Client update_client_tags(body, domain_id, client_id)

Updates tags the client.

Updates tags of the client with provided ID. Tags is updated using authorization token and the new tags received in request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientTags() # ClientTags | JSON-formated document describing the tags of client to be update
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Updates tags the client.
    api_response = api_instance.update_client_tags(body, domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->update_client_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientTags**](ClientTags.md)| JSON-formated document describing the tags of client to be update | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**Client**](Client.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


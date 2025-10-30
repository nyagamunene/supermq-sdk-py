# swagger_client.RolesApi

All URIs are relative to *http://localhost:9006*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_role_action**](RolesApi.md#add_client_role_action) | **POST** /{domainID}/clients/{clientID}/roles/{roleID}/actions | Adds a role action for a client role.
[**add_client_role_member**](RolesApi.md#add_client_role_member) | **POST** /{domainID}/clients/{clientID}/roles/{roleID}/members | Adds a member to a client role.
[**create_client_role**](RolesApi.md#create_client_role) | **POST** /{domainID}/clients/{clientID}/roles | Creates a role for a client
[**delete_all_client_role_actions**](RolesApi.md#delete_all_client_role_actions) | **POST** /{domainID}/clients/{clientID}/roles/{roleID}/actions/delete-all | Deletes all role actions for a client role.
[**delete_all_client_role_members**](RolesApi.md#delete_all_client_role_members) | **POST** /{domainID}/clients/{clientID}/roles/{roleID}/members/delete-all | Deletes all members from a client role.
[**delete_client_role**](RolesApi.md#delete_client_role) | **DELETE** /{domainID}/clients/{clientID}/roles/{roleID} | Deletes client role.
[**delete_client_role_action**](RolesApi.md#delete_client_role_action) | **POST** /{domainID}/clients/{clientID}/roles/{roleID}/actions/delete | Deletes role actions for a client role.
[**delete_client_role_members**](RolesApi.md#delete_client_role_members) | **POST** /{domainID}/clients/{clientID}/roles/{roleID}/members/delete | Deletes members from a client role.
[**get_client_members**](RolesApi.md#get_client_members) | **GET** /{domainID}/clients/{clientID}/roles/members | Retrieves client members from all roles.
[**get_client_role**](RolesApi.md#get_client_role) | **GET** /{domainID}/clients/{clientID}/roles/{roleID} | Retrieves client role.
[**list_available_actions**](RolesApi.md#list_available_actions) | **GET** /{domainID}/clients/roles/available-actions | Retrieves available actions.
[**list_client_role_actions**](RolesApi.md#list_client_role_actions) | **GET** /{domainID}/clients/{clientID}/roles/{roleID}/actions | Lists client role actions.
[**list_client_role_members**](RolesApi.md#list_client_role_members) | **GET** /{domainID}/clients/{clientID}/roles/{roleID}/members | Lists client role members.
[**list_client_roles**](RolesApi.md#list_client_roles) | **GET** /{domainID}/clients/{clientID}/roles | Retrieves clients roles.
[**update_client_role**](RolesApi.md#update_client_role) | **PUT** /{domainID}/clients/{clientID}/roles/{roleID} | Updates client role.

# **add_client_role_action**
> RoleActionsObj add_client_role_action(body, domain_id, client_id, role_id)

Adds a role action for a client role.

Adds a role action for a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleActionsObj() # RoleActionsObj | JSON- formatted object decsribing an action to be added to a role.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Adds a role action for a client role.
    api_response = api_instance.add_client_role_action(body, domain_id, client_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->add_client_role_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleActionsObj**](RoleActionsObj.md)| JSON- formatted object decsribing an action to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleActionsObj**](RoleActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_client_role_member**
> RoleMembersObj add_client_role_member(body, domain_id, client_id, role_id)

Adds a member to a client role.

Adds a member to a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleMembersObj() # RoleMembersObj | JSON- formatted object decsribing a member to be added to a role.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Adds a member to a client role.
    api_response = api_instance.add_client_role_member(body, domain_id, client_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->add_client_role_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleMembersObj**](RoleMembersObj.md)| JSON- formatted object decsribing a member to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleMembersObj**](RoleMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_role**
> NewRole create_client_role(body, domain_id, client_id)

Creates a role for a client

Creates a role for a specific client that is identified by the client ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRoleObj() # CreateRoleObj | JSON- formatted object decsribing a new role to be created.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Creates a role for a client
    api_response = api_instance.create_client_role(body, domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_client_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleObj**](CreateRoleObj.md)| JSON- formatted object decsribing a new role to be created. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**NewRole**](NewRole.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_client_role_actions**
> delete_all_client_role_actions(domain_id, client_id, role_id)

Deletes all role actions for a client role.

Deletes all role actions for a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes all role actions for a client role.
    api_instance.delete_all_client_role_actions(domain_id, client_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_all_client_role_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_client_role_members**
> delete_all_client_role_members(domain_id, client_id, role_id)

Deletes all members from a client role.

Deletes all members from a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes all members from a client role.
    api_instance.delete_all_client_role_members(domain_id, client_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_all_client_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_role**
> delete_client_role(domain_id, client_id, role_id)

Deletes client role.

Deletes a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes client role.
    api_instance.delete_client_role(domain_id, client_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_client_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_role_action**
> delete_client_role_action(body, domain_id, client_id, role_id)

Deletes role actions for a client role.

Deletes a role action for a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleActionsObj() # RoleActionsObj | JSON- formatted object decsribing an action to be added to a role.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes role actions for a client role.
    api_instance.delete_client_role_action(body, domain_id, client_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_client_role_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleActionsObj**](RoleActionsObj.md)| JSON- formatted object decsribing an action to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_role_members**
> delete_client_role_members(body, domain_id, client_id, role_id)

Deletes members from a client role.

Deletes a member from a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleMembersObj() # RoleMembersObj | JSON- formatted object decsribing a member to be added to a role.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes members from a client role.
    api_instance.delete_client_role_members(body, domain_id, client_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_client_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleMembersObj**](RoleMembersObj.md)| JSON- formatted object decsribing a member to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_members**
> EntityMembersObj get_client_members(domain_id, client_id)

Retrieves client members from all roles.

Retrieves members from role for the specific client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.

try:
    # Retrieves client members from all roles.
    api_response = api_instance.get_client_members(domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_client_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 

### Return type

[**EntityMembersObj**](EntityMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_role**
> Role get_client_role(domain_id, client_id, role_id)

Retrieves client role.

Retrieves a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Retrieves client role.
    api_response = api_instance.get_client_role(domain_id, client_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_client_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**Role**](Role.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_actions**
> AvailableActionsObj list_available_actions(domain_id)

Retrieves available actions.

Retrieves a list of available actions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Retrieves available actions.
    api_response = api_instance.list_available_actions(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_available_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

[**AvailableActionsObj**](AvailableActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_role_actions**
> RoleActionsObj list_client_role_actions(domain_id, client_id, role_id)

Lists client role actions.

Retrieves a list of client role actions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Lists client role actions.
    api_response = api_instance.list_client_role_actions(domain_id, client_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_client_role_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleActionsObj**](RoleActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_role_members**
> RoleMembersObj list_client_role_members(domain_id, client_id, role_id)

Lists client role members.

Retrieves a list of client role members. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Lists client role members.
    api_response = api_instance.list_client_role_members(domain_id, client_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_client_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleMembersObj**](RoleMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_roles**
> RolesPage list_client_roles(domain_id, client_id, limit=limit, offset=offset)

Retrieves clients roles.

Retrieves a list of client roles. Due to performance concerns, data is retrieved in subsets. The API clients must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)

try:
    # Retrieves clients roles.
    api_response = api_instance.list_client_roles(domain_id, client_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_client_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]

### Return type

[**RolesPage**](RolesPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_role**
> Role update_client_role(body, domain_id, client_id, role_id)

Updates client role.

Updates a specific client role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateRoleObj() # UpdateRoleObj | JSON- formatted object decsribing a role to be updated.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique client identifier.
role_id = 'role_id_example' # str | Role ID.

try:
    # Updates client role.
    api_response = api_instance.update_client_role(body, domain_id, client_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_client_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRoleObj**](UpdateRoleObj.md)| JSON- formatted object decsribing a role to be updated. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **client_id** | [**str**](.md)| Unique client identifier. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**Role**](Role.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


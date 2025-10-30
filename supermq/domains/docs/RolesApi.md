# swagger_client.RolesApi

All URIs are relative to *http://localhost:9003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_role_action**](RolesApi.md#add_domain_role_action) | **POST** /domains/{domainID}/roles/{roleID}/actions | Adds a role action for a domain role.
[**add_domain_role_member**](RolesApi.md#add_domain_role_member) | **POST** /domains/{domainID}/roles/{roleID}/members | Adds a member to a domain role.
[**create_domain_role**](RolesApi.md#create_domain_role) | **POST** /domains/{domainID}/roles | Creates a role for a domain
[**delete_all_domain_role_actions**](RolesApi.md#delete_all_domain_role_actions) | **POST** /domains/{domainID}/roles/{roleID}/actions/delete-all | Deletes all role actions for a domain role.
[**delete_all_domain_role_members**](RolesApi.md#delete_all_domain_role_members) | **POST** /domains/{domainID}/roles/{roleID}/members/delete-all | Deletes all members from a domain role.
[**delete_domain_role**](RolesApi.md#delete_domain_role) | **DELETE** /domains/{domainID}/roles/{roleID} | Deletes domain role.
[**delete_domain_role_action**](RolesApi.md#delete_domain_role_action) | **POST** /domains/{domainID}/roles/{roleID}/actions/delete | Deletes role actions for a domain role.
[**delete_domain_role_members**](RolesApi.md#delete_domain_role_members) | **POST** /domains/{domainID}/roles/{roleID}/members/delete | Deletes members from a domain role.
[**get_domain_members**](RolesApi.md#get_domain_members) | **GET** /domain/{domainID}/roles/members | Retrieves domain members from all roles.
[**get_domain_role**](RolesApi.md#get_domain_role) | **GET** /domains/{domainID}/roles/{roleID} | Retrieves domain role.
[**list_available_actions**](RolesApi.md#list_available_actions) | **GET** /domains/roles/available-actions | Retrieves available actions.
[**list_domain_role_actions**](RolesApi.md#list_domain_role_actions) | **GET** /domains/{domainID}/roles/{roleID}/actions | Lists domain role actions.
[**list_domain_role_members**](RolesApi.md#list_domain_role_members) | **GET** /domains/{domainID}/roles/{roleID}/members | Lists domain role members.
[**list_domain_roles**](RolesApi.md#list_domain_roles) | **GET** /domains/{domainID}/roles | Retrieves domains roles.
[**update_domain_role**](RolesApi.md#update_domain_role) | **PUT** /domains/{domainID}/roles/{roleID} | Updates domain role.

# **add_domain_role_action**
> RoleActionsObj add_domain_role_action(body, domain_id, role_id)

Adds a role action for a domain role.

Adds a role action for a specific domain role that is identified by the role name. 

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
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Adds a role action for a domain role.
    api_response = api_instance.add_domain_role_action(body, domain_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->add_domain_role_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleActionsObj**](RoleActionsObj.md)| JSON- formatted object decsribing an action to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleActionsObj**](RoleActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domain_role_member**
> RoleMembersObj add_domain_role_member(body, domain_id, role_id)

Adds a member to a domain role.

Adds a member to a specific domain role that is identified by the role name. 

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
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Adds a member to a domain role.
    api_response = api_instance.add_domain_role_member(body, domain_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->add_domain_role_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleMembersObj**](RoleMembersObj.md)| JSON- formatted object decsribing a member to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleMembersObj**](RoleMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain_role**
> NewRole create_domain_role(body, domain_id)

Creates a role for a domain

Creates a role for a specific domain that is identified by the domain ID. 

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
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Creates a role for a domain
    api_response = api_instance.create_domain_role(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleObj**](CreateRoleObj.md)| JSON- formatted object decsribing a new role to be created. | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

[**NewRole**](NewRole.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_domain_role_actions**
> delete_all_domain_role_actions(domain_id, role_id)

Deletes all role actions for a domain role.

Deletes all role actions for a specific domain role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes all role actions for a domain role.
    api_instance.delete_all_domain_role_actions(domain_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_all_domain_role_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_domain_role_members**
> delete_all_domain_role_members(domain_id, role_id)

Deletes all members from a domain role.

Deletes all members from a specific domain role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes all members from a domain role.
    api_instance.delete_all_domain_role_members(domain_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_all_domain_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_role**
> delete_domain_role(domain_id, role_id)

Deletes domain role.

Deletes a specific domain role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes domain role.
    api_instance.delete_domain_role(domain_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_role_action**
> delete_domain_role_action(body, domain_id, role_id)

Deletes role actions for a domain role.

Deletes a role action for a specific domain role that is identified by the role name. 

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
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes role actions for a domain role.
    api_instance.delete_domain_role_action(body, domain_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_domain_role_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleActionsObj**](RoleActionsObj.md)| JSON- formatted object decsribing an action to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_role_members**
> delete_domain_role_members(body, domain_id, role_id)

Deletes members from a domain role.

Deletes a member from a specific domain role that is identified by the role name. 

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
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Deletes members from a domain role.
    api_instance.delete_domain_role_members(body, domain_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_domain_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleMembersObj**](RoleMembersObj.md)| JSON- formatted object decsribing a member to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_members**
> EntityMembersObj get_domain_members(domain_id)

Retrieves domain members from all roles.

Retrieves members from role for the specific domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Retrieves domain members from all roles.
    api_response = api_instance.get_domain_members(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_domain_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

[**EntityMembersObj**](EntityMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_role**
> Role get_domain_role(domain_id, role_id)

Retrieves domain role.

Retrieves a specific domain role that is identified by the role name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Retrieves domain role.
    api_response = api_instance.get_domain_role(domain_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
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
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

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
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

[**AvailableActionsObj**](AvailableActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_role_actions**
> RoleActionsObj list_domain_role_actions(domain_id, role_id)

Lists domain role actions.

Retrieves a list of domain role actions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Lists domain role actions.
    api_response = api_instance.list_domain_role_actions(domain_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_domain_role_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleActionsObj**](RoleActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_role_members**
> RoleMembersObj list_domain_role_members(domain_id, role_id)

Lists domain role members.

Retrieves a list of domain role members. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Lists domain role members.
    api_response = api_instance.list_domain_role_members(domain_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_domain_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**RoleMembersObj**](RoleMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_roles**
> RolesPage list_domain_roles(domain_id, limit=limit, offset=offset)

Retrieves domains roles.

Retrieves a list of domain roles. Due to performance concerns, data is retrieved in subsets. The API domains must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)

try:
    # Retrieves domains roles.
    api_response = api_instance.list_domain_roles(domain_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_domain_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
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

# **update_domain_role**
> Role update_domain_role(body, domain_id, role_id)

Updates domain role.

Updates a specific domain role that is identified by the role name. 

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
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
role_id = 'role_id_example' # str | Role ID.

try:
    # Updates domain role.
    api_response = api_instance.update_domain_role(body, domain_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRoleObj**](UpdateRoleObj.md)| JSON- formatted object decsribing a role to be updated. | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **role_id** | **str**| Role ID. | 

### Return type

[**Role**](Role.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


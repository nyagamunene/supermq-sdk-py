# swagger_client.RolesApi

All URIs are relative to *http://localhost:9004*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_role_action**](RolesApi.md#add_group_role_action) | **POST** /{domainID}/groups/{groupID}/roles/{roleID}/actions | Adds a role action for a group role.
[**add_group_role_member**](RolesApi.md#add_group_role_member) | **POST** /{domainID}/groups/{groupID}/roles/{roleID}/members | Adds a member to a group role.
[**create_group_role**](RolesApi.md#create_group_role) | **POST** /{domainID}/groups/{groupID}/roles | Creates a role for a group
[**delete_all_group_role_actions**](RolesApi.md#delete_all_group_role_actions) | **POST** /{domainID}/groups/{groupID}/roles/{roleID}/actions/delete-all | Deletes all role actions for a group role.
[**delete_all_group_role_members**](RolesApi.md#delete_all_group_role_members) | **POST** /{domainID}/groups/{groupID}/roles/{roleID}/members/delete-all | Deletes all members from a group role.
[**delete_group_role**](RolesApi.md#delete_group_role) | **DELETE** /{domainID}/groups/{groupID}/roles/{roleID} | Deletes group role.
[**delete_group_role_action**](RolesApi.md#delete_group_role_action) | **POST** /{domainID}/groups/{groupID}/roles/{roleID}/actions/delete | Deletes role actions for a group role.
[**delete_group_role_members**](RolesApi.md#delete_group_role_members) | **POST** /{domainID}/groups/{groupID}/roles/{roleID}/members/delete | Deletes members from a group role.
[**get_group_members**](RolesApi.md#get_group_members) | **GET** /{domainID}/groups/{groupID}/roles/members | Retrieves group members from all roles.
[**get_group_role**](RolesApi.md#get_group_role) | **GET** /{domainID}/groups/{groupID}/roles/{roleID} | Retrieves group role.
[**list_available_actions**](RolesApi.md#list_available_actions) | **GET** /{domainID}/groups/roles/available-actions | Retrieves available actions.
[**list_group_role_actions**](RolesApi.md#list_group_role_actions) | **GET** /{domainID}/groups/{groupID}/roles/{roleID}/actions | Lists group role actions.
[**list_group_role_members**](RolesApi.md#list_group_role_members) | **GET** /{domainID}/groups/{groupID}/roles/{roleID}/members | Lists group role members.
[**list_group_roles**](RolesApi.md#list_group_roles) | **GET** /{domainID}/groups/{groupID}/roles | Retrieves groups roles.
[**update_group_role**](RolesApi.md#update_group_role) | **PUT** /{domainID}/groups/{groupID}/roles/{roleID} | Updates group role.

# **add_group_role_action**
> RoleActionsObj add_group_role_action(body, domain_id, group_id, role_id=role_id)

Adds a role action for a group role.

Adds a role action for a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Adds a role action for a group role.
    api_response = api_instance.add_group_role_action(body, domain_id, group_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->add_group_role_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleActionsObj**](RoleActionsObj.md)| JSON- formatted object decsribing an action to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

[**RoleActionsObj**](RoleActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_role_member**
> RoleMembersObj add_group_role_member(body, domain_id, group_id, role_id=role_id)

Adds a member to a group role.

Adds a member to a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Adds a member to a group role.
    api_response = api_instance.add_group_role_member(body, domain_id, group_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->add_group_role_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleMembersObj**](RoleMembersObj.md)| JSON- formatted object decsribing a member to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

[**RoleMembersObj**](RoleMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_role**
> NewRole create_group_role(body, domain_id, group_id)

Creates a role for a group

Creates a role for a specific group that is identified by the group ID. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Creates a role for a group
    api_response = api_instance.create_group_role(body, domain_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleObj**](CreateRoleObj.md)| JSON- formatted object decsribing a new role to be created. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

[**NewRole**](NewRole.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_group_role_actions**
> delete_all_group_role_actions(domain_id, group_id, role_id=role_id)

Deletes all role actions for a group role.

Deletes all role actions for a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Deletes all role actions for a group role.
    api_instance.delete_all_group_role_actions(domain_id, group_id, role_id=role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_all_group_role_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_group_role_members**
> delete_all_group_role_members(domain_id, group_id, role_id=role_id)

Deletes all members from a group role.

Deletes all members from a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Deletes all members from a group role.
    api_instance.delete_all_group_role_members(domain_id, group_id, role_id=role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_all_group_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_role**
> delete_group_role(domain_id, group_id, role_id=role_id)

Deletes group role.

Deletes a specific group role that is identifier by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Deletes group role.
    api_instance.delete_group_role(domain_id, group_id, role_id=role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_role_action**
> delete_group_role_action(body, domain_id, group_id, role_id=role_id)

Deletes role actions for a group role.

Deletes a role action for a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Deletes role actions for a group role.
    api_instance.delete_group_role_action(body, domain_id, group_id, role_id=role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_group_role_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleActionsObj**](RoleActionsObj.md)| JSON- formatted object decsribing an action to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_role_members**
> delete_group_role_members(body, domain_id, group_id, role_id=role_id)

Deletes members from a group role.

Deletes a member from a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Deletes members from a group role.
    api_instance.delete_group_role_members(body, domain_id, group_id, role_id=role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_group_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleMembersObj**](RoleMembersObj.md)| JSON- formatted object decsribing a member to be added to a role. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_members**
> EntityMembersObj get_group_members(domain_id, group_id)

Retrieves group members from all roles.

Retrieves members from role for the specific group. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Retrieves group members from all roles.
    api_response = api_instance.get_group_members(domain_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

[**EntityMembersObj**](EntityMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_role**
> Role get_group_role(domain_id, group_id, role_id=role_id)

Retrieves group role.

Retrieves a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Retrieves group role.
    api_response = api_instance.get_group_role(domain_id, group_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

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

# **list_group_role_actions**
> RoleActionsObj list_group_role_actions(domain_id, group_id, role_id=role_id)

Lists group role actions.

Retrieves a list of group role actions. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Lists group role actions.
    api_response = api_instance.list_group_role_actions(domain_id, group_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_group_role_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

[**RoleActionsObj**](RoleActionsObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_role_members**
> RoleMembersObj list_group_role_members(domain_id, group_id, role_id=role_id)

Lists group role members.

Retrieves a list of group role members. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Lists group role members.
    api_response = api_instance.list_group_role_members(domain_id, group_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_group_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

[**RoleMembersObj**](RoleMembersObj.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_roles**
> RolesPage list_group_roles(domain_id, group_id, limit=limit, offset=offset)

Retrieves groups roles.

Retrieves a list of group roles. Due to performance concerns, data is retrieved in subsets. The API groups must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)

try:
    # Retrieves groups roles.
    api_response = api_instance.list_group_roles(domain_id, group_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_group_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
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

# **update_group_role**
> Role update_group_role(body, domain_id, group_id, role_id=role_id)

Updates group role.

Updates a specific group role that is identified by the role name. 

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
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)

try:
    # Updates group role.
    api_response = api_instance.update_group_role(body, domain_id, group_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRoleObj**](UpdateRoleObj.md)| JSON- formatted object decsribing a role to be updated. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


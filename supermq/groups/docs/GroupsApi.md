# swagger_client.GroupsApi

All URIs are relative to *http://localhost:9004*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_children_groups**](GroupsApi.md#add_children_groups) | **POST** /{domainID}/groups/{groupID}/children | Add children groups.
[**create_group**](GroupsApi.md#create_group) | **POST** /{domainID}/groups | Creates new group
[**disable_group**](GroupsApi.md#disable_group) | **POST** /{domainID}/groups/{groupID}/disable | Disables a group
[**domain_id_groups_group_id_delete**](GroupsApi.md#domain_id_groups_group_id_delete) | **DELETE** /{domainID}/groups/{groupID} | Delete group for a group with the given id.
[**enable_group**](GroupsApi.md#enable_group) | **POST** /{domainID}/groups/{groupID}/enable | Enables a group
[**get_group**](GroupsApi.md#get_group) | **GET** /{domainID}/groups/{groupID} | Gets group info.
[**list_children_groups**](GroupsApi.md#list_children_groups) | **GET** /{domainID}/groups/{groupID}/children | List children of a certain group
[**list_group_hierarchy**](GroupsApi.md#list_group_hierarchy) | **GET** /{domainID}/groups/{groupID}/hierarchy | Lists groups hierarchy.
[**list_groups**](GroupsApi.md#list_groups) | **GET** /{domainID}/groups | Lists groups.
[**remove_all_children_groups**](GroupsApi.md#remove_all_children_groups) | **DELETE** /{domainID}/groups/{groupID}/children/all | Remove all children groups.
[**remove_children_groups**](GroupsApi.md#remove_children_groups) | **DELETE** /{domainID}/groups/{groupID}/children | Remove children groups.
[**remove_group_parent_group**](GroupsApi.md#remove_group_parent_group) | **DELETE** /{domainID}/groups/{groupID}/parent | Removes a parent group from a group.
[**set_group_parent_group**](GroupsApi.md#set_group_parent_group) | **POST** /{domainID}/groups/{groupID}/parent | Sets a parent group for a group.
[**update_group**](GroupsApi.md#update_group) | **PUT** /{domainID}/groups/{groupID} | Updates group data.
[**update_group_tags**](GroupsApi.md#update_group_tags) | **PATCH** /{domainID}/groups/{groupID}/tags | Updates group tags.

# **add_children_groups**
> add_children_groups(body, domain_id, group_id)

Add children groups.

Adds children groups for a specific group that is identified by the group ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChildrenGroupReqObj() # ChildrenGroupReqObj | JSON-formated document describing the children groups to be added to a group.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Add children groups.
    api_instance.add_children_groups(body, domain_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->add_children_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChildrenGroupReqObj**](ChildrenGroupReqObj.md)| JSON-formated document describing the children groups to be added to a group. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(body, domain_id)

Creates new group

Creates new group that can be used for grouping entities. New account will be uniquely identified by its identity. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupReqObj() # GroupReqObj | JSON-formatted document describing the new group to be registered
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Creates new group
    api_response = api_instance.create_group(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupReqObj**](GroupReqObj.md)| JSON-formatted document describing the new group to be registered | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_group**
> Group disable_group(domain_id, group_id)

Disables a group

Disables a specific group that is identifier by the group ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Disables a group
    api_response = api_instance.disable_group(domain_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->disable_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_id_groups_group_id_delete**
> domain_id_groups_group_id_delete(domain_id, group_id)

Delete group for a group with the given id.

Delete group removes a group with the given id from repo and removes all the policies related to this group. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Delete group for a group with the given id.
    api_instance.domain_id_groups_group_id_delete(domain_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->domain_id_groups_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_group**
> Group enable_group(domain_id, group_id)

Enables a group

Enables a specific group that is identifier by the group ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Enables a group
    api_response = api_instance.enable_group(domain_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->enable_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(domain_id, group_id)

Gets group info.

Gets info on a group specified by id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Gets group info.
    api_response = api_instance.get_group(domain_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_children_groups**
> GroupsPage list_children_groups(domain_id, group_id, limit=limit, offset=offset, start_level=start_level, end_level=end_level, tree=tree, metadata=metadata, name=name)

List children of a certain group

Lists groups up to a max level of hierarchy that can be fetched in one request ( max level = 5). Result can be filtered by metadata. Groups will be returned as JSON array or JSON tree. Due to performance concerns, result is returned in subsets. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
start_level = 56 # int | Level of hierarchy from which to start retrieving groups from given group id. (optional)
end_level = 56 # int | Level of hierarchy up to which to retrieve groups from given group id. (optional)
tree = false # bool | Specify type of response, JSON array or tree. (optional) (default to false)
metadata = 'metadata_example' # str | Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. (optional)
name = 'name_example' # str | Group's name. (optional)

try:
    # List children of a certain group
    api_response = api_instance.list_children_groups(domain_id, group_id, limit=limit, offset=offset, start_level=start_level, end_level=end_level, tree=tree, metadata=metadata, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_children_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **start_level** | **int**| Level of hierarchy from which to start retrieving groups from given group id. | [optional] 
 **end_level** | **int**| Level of hierarchy up to which to retrieve groups from given group id. | [optional] 
 **tree** | **bool**| Specify type of response, JSON array or tree. | [optional] [default to false]
 **metadata** | **str**| Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. | [optional] 
 **name** | **str**| Group&#x27;s name. | [optional] 

### Return type

[**GroupsPage**](GroupsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_hierarchy**
> GroupsHierarchyPage list_group_hierarchy(domain_id, group_id, level=level, tree=tree, direction=direction)

Lists groups hierarchy.

Lists groups heirarchy up to a max level of hierarchy that can be fetched in one request ( max level = 5). Result can be filtered by metadata. Groups will be returned as JSON array or JSON tree. Due to performance concerns, result is returned in subsets. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.
level = 56 # int | Level of hierarchy up to which to retrieve groups from given group id. (optional)
tree = false # bool | Specify type of response, JSON array or tree. (optional) (default to false)
direction = 56 # int | Direction of hierarchy traversal. (optional)

try:
    # Lists groups hierarchy.
    api_response = api_instance.list_group_hierarchy(domain_id, group_id, level=level, tree=tree, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_group_hierarchy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 
 **level** | **int**| Level of hierarchy up to which to retrieve groups from given group id. | [optional] 
 **tree** | **bool**| Specify type of response, JSON array or tree. | [optional] [default to false]
 **direction** | **int**| Direction of hierarchy traversal. | [optional] 

### Return type

[**GroupsHierarchyPage**](GroupsHierarchyPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> GroupsPage list_groups(domain_id, limit=limit, offset=offset, order=order, level=level, tree=tree, metadata=metadata, name=name, root_group=root_group, status=status, id=id, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total)

Lists groups.

Lists groups up to a max level of hierarchy that can be fetched in one request ( max level = 5). Result can be filtered by metadata. Groups will be returned as JSON array or JSON tree. Due to performance concerns, result is returned in subsets. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
order = 'order_example' # str | Direction of ordering the results. (optional)
level = 56 # int | Level of hierarchy up to which to retrieve groups from given group id. (optional)
tree = false # bool | Specify type of response, JSON array or tree. (optional) (default to false)
metadata = 'metadata_example' # str | Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. (optional)
name = 'name_example' # str | Group's name. (optional)
root_group = false # bool | List groups without a parent group. (optional) (default to false)
status = 'status_example' # str | Lists groups with the given status. (optional)
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups with the given ID. (optional)
actions = 'actions_example' # str | Lists groups that the user has the given actions on. Multiple actions can be specified separated by comma. (optional)
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List groups that the user has the given role ID on. (optional)
role_name = 'role_name_example' # str | List groups that the user has the given role name on. (optional)
access_type = 'access_type_example' # str | Type of access the user has on the group. (optional)
only_total = false # bool | If true, the response will contain only the total number of groups that match the query parameters. (optional) (default to false)

try:
    # Lists groups.
    api_response = api_instance.list_groups(domain_id, limit=limit, offset=offset, order=order, level=level, tree=tree, metadata=metadata, name=name, root_group=root_group, status=status, id=id, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **order** | **str**| Direction of ordering the results. | [optional] 
 **level** | **int**| Level of hierarchy up to which to retrieve groups from given group id. | [optional] 
 **tree** | **bool**| Specify type of response, JSON array or tree. | [optional] [default to false]
 **metadata** | **str**| Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. | [optional] 
 **name** | **str**| Group&#x27;s name. | [optional] 
 **root_group** | **bool**| List groups without a parent group. | [optional] [default to false]
 **status** | **str**| Lists groups with the given status. | [optional] 
 **id** | [**str**](.md)| List groups with the given ID. | [optional] 
 **actions** | **str**| Lists groups that the user has the given actions on. Multiple actions can be specified separated by comma. | [optional] 
 **role_id** | [**str**](.md)| List groups that the user has the given role ID on. | [optional] 
 **role_name** | **str**| List groups that the user has the given role name on. | [optional] 
 **access_type** | **str**| Type of access the user has on the group. | [optional] 
 **only_total** | **bool**| If true, the response will contain only the total number of groups that match the query parameters. | [optional] [default to false]

### Return type

[**GroupsPage**](GroupsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_children_groups**
> remove_all_children_groups(domain_id, group_id)

Remove all children groups.

Removes all children groups for a specific group that is identified by the group ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Remove all children groups.
    api_instance.remove_all_children_groups(domain_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->remove_all_children_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_children_groups**
> remove_children_groups(body, domain_id, group_id)

Remove children groups.

Removes children groups for a specific group that is identified by the group ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChildrenGroupReqObj() # ChildrenGroupReqObj | JSON-formated document describing the children groups to be added to a group.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Remove children groups.
    api_instance.remove_children_groups(body, domain_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->remove_children_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChildrenGroupReqObj**](ChildrenGroupReqObj.md)| JSON-formated document describing the children groups to be added to a group. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_parent_group**
> remove_group_parent_group(body, domain_id, group_id)

Removes a parent group from a group.

Removes a parent group from a specific group that is identified by the group ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ParentGroupReqObj() # ParentGroupReqObj | JSON-formated document describing the parent group to be set to or removed from a group.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Removes a parent group from a group.
    api_instance.remove_group_parent_group(body, domain_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->remove_group_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParentGroupReqObj**](ParentGroupReqObj.md)| JSON-formated document describing the parent group to be set to or removed from a group. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_parent_group**
> set_group_parent_group(body, domain_id, group_id)

Sets a parent group for a group.

Sets a parent group for a specific group that is identified by the group ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ParentGroupReqObj() # ParentGroupReqObj | JSON-formated document describing the parent group to be set to or removed from a group.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Sets a parent group for a group.
    api_instance.set_group_parent_group(body, domain_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->set_group_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParentGroupReqObj**](ParentGroupReqObj.md)| JSON-formated document describing the parent group to be set to or removed from a group. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(body, domain_id, group_id)

Updates group data.

Updates Name, Description or Metadata of a group. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupUpdate() # GroupUpdate | JSON-formated document describing the metadata and name of group to be update
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Updates group data.
    api_response = api_instance.update_group(body, domain_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupUpdate**](GroupUpdate.md)| JSON-formated document describing the metadata and name of group to be update | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_tags**
> Group update_group_tags(body, domain_id, group_id)

Updates group tags.

Update is performed by replacing the current resource data with values provided in a request payload. Note that the group's ID will not be affected. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupUpdateTags() # GroupUpdateTags | JSON-formated document describing the tags of group to be updated.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique group identifier.

try:
    # Updates group tags.
    api_response = api_instance.update_group_tags(body, domain_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupUpdateTags**](GroupUpdateTags.md)| JSON-formated document describing the tags of group to be updated. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **group_id** | [**str**](.md)| Unique group identifier. | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


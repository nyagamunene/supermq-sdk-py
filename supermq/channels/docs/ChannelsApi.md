# swagger_client.ChannelsApi

All URIs are relative to *http://localhost:9005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel**](ChannelsApi.md#create_channel) | **POST** /{domainID}/channels | Creates new channel
[**create_channels**](ChannelsApi.md#create_channels) | **POST** /{domainID}/channels/bulk | Creates new channels
[**disable_channel**](ChannelsApi.md#disable_channel) | **POST** /{domainID}/channels/{chanID}/disable | Disables a channel
[**domain_id_channels_chan_id_delete**](ChannelsApi.md#domain_id_channels_chan_id_delete) | **DELETE** /{domainID}/channels/{chanID} | Delete channel for given channel id.
[**enable_channel**](ChannelsApi.md#enable_channel) | **POST** /{domainID}/channels/{chanID}/enable | Enables a channel
[**get_channel**](ChannelsApi.md#get_channel) | **GET** /{domainID}/channels/{chanID} | Retrieves channel info.
[**list_channels**](ChannelsApi.md#list_channels) | **GET** /{domainID}/channels | Lists channels.
[**remove_channel_parent_group**](ChannelsApi.md#remove_channel_parent_group) | **DELETE** /{domainID}/channels/{chanID}/parent | Removes a parent group from a channel.
[**set_channel_parent_group**](ChannelsApi.md#set_channel_parent_group) | **POST** /{domainID}/channels/{chanID}/parent | Sets a parent group for a channel
[**update_channel**](ChannelsApi.md#update_channel) | **PATCH** /{domainID}/channels/{chanID} | Updates channel data.
[**update_channel_tags**](ChannelsApi.md#update_channel_tags) | **PATCH** /{domainID}/channels/{chanID}/tags | Updates channel tags.

# **create_channel**
> Channel create_channel(body, domain_id)

Creates new channel

Creates new channel in domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelReqObj() # ChannelReqObj | JSON-formatted document describing the new channel to be registered
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Creates new channel
    api_response = api_instance.create_channel(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->create_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelReqObj**](ChannelReqObj.md)| JSON-formatted document describing the new channel to be registered | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

[**Channel**](Channel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_channels**
> list[Channel] create_channels(body, domain_id)

Creates new channels

Creates new channels in domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ChannelReqObj()] # list[ChannelReqObj] | JSON-formatted document describing the new channels to be registered
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Creates new channels
    api_response = api_instance.create_channels(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->create_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChannelReqObj]**](ChannelReqObj.md)| JSON-formatted document describing the new channels to be registered | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

[**list[Channel]**](Channel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_channel**
> Channel disable_channel(domain_id, chan_id)

Disables a channel

Disables a specific channel that is identified by the channel ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Disables a channel
    api_response = api_instance.disable_channel(domain_id, chan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->disable_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

[**Channel**](Channel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_id_channels_chan_id_delete**
> domain_id_channels_chan_id_delete(domain_id, chan_id)

Delete channel for given channel id.

Delete channel remove given channel id from repo and removes all the policies related to channel. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Delete channel for given channel id.
    api_instance.domain_id_channels_chan_id_delete(domain_id, chan_id)
except ApiException as e:
    print("Exception when calling ChannelsApi->domain_id_channels_chan_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_channel**
> Channel enable_channel(domain_id, chan_id)

Enables a channel

Enables a specific channel that is identified by the channel ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Enables a channel
    api_response = api_instance.enable_channel(domain_id, chan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->enable_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

[**Channel**](Channel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> Channel get_channel(domain_id, chan_id)

Retrieves channel info.

Gets info on a channel specified by id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Retrieves channel info.
    api_response = api_instance.get_channel(domain_id, chan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

[**Channel**](Channel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channels**
> ChannelsPage list_channels(domain_id, limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, name=name, id=id, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total, client=client, group=group, user=user)

Lists channels.

Retrieves a list of channels. Due to performance concerns, data is retrieved in subsets. The API clients must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
order = 'order_example' # str | Field by which to order the results (optional)
dir = 'dir_example' # str | Direction of ordering the results. (optional)
metadata = 'metadata_example' # str | Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. (optional)
status = 'enabled' # str | Client account status. (optional) (default to enabled)
name = 'name_example' # str | Channel's name. (optional)
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List channels with the given ID. (optional)
actions = 'actions_example' # str | Lists channels that the user has the given actions on. Multiple actions can be specified separated by comma. (optional)
role_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | List channels that the user has the given role ID on. (optional)
role_name = 'role_name_example' # str | List channels that the user has the given role name on. (optional)
access_type = 'access_type_example' # str | Type of access the user has on the channel. (optional)
only_total = false # bool | If true, the response will contain only the total number of channels that match the query parameters. (optional) (default to false)
client = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | If provided lists channels that a client with the provided ID is connected to. (optional)
group = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | If provided lists channels belonging to a group with the provided ID. (optional)
user = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | If provided lists channels associated with a user with the provided ID. Only available for admin users. (optional)

try:
    # Lists channels.
    api_response = api_instance.list_channels(domain_id, limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, name=name, id=id, actions=actions, role_id=role_id, role_name=role_name, access_type=access_type, only_total=only_total, client=client, group=group, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->list_channels: %s\n" % e)
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
 **name** | **str**| Channel&#x27;s name. | [optional] 
 **id** | [**str**](.md)| List channels with the given ID. | [optional] 
 **actions** | **str**| Lists channels that the user has the given actions on. Multiple actions can be specified separated by comma. | [optional] 
 **role_id** | [**str**](.md)| List channels that the user has the given role ID on. | [optional] 
 **role_name** | **str**| List channels that the user has the given role name on. | [optional] 
 **access_type** | **str**| Type of access the user has on the channel. | [optional] 
 **only_total** | **bool**| If true, the response will contain only the total number of channels that match the query parameters. | [optional] [default to false]
 **client** | [**str**](.md)| If provided lists channels that a client with the provided ID is connected to. | [optional] 
 **group** | [**str**](.md)| If provided lists channels belonging to a group with the provided ID. | [optional] 
 **user** | [**str**](.md)| If provided lists channels associated with a user with the provided ID. Only available for admin users. | [optional] 

### Return type

[**ChannelsPage**](ChannelsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_channel_parent_group**
> remove_channel_parent_group(body, domain_id, chan_id)

Removes a parent group from a channel.

Removes a parent group from a specific channel that is identified by the channel ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ParentGroupReqObj() # ParentGroupReqObj | JSON-formated document describing the parent group to be set to or removed from a channel.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Removes a parent group from a channel.
    api_instance.remove_channel_parent_group(body, domain_id, chan_id)
except ApiException as e:
    print("Exception when calling ChannelsApi->remove_channel_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParentGroupReqObj**](ParentGroupReqObj.md)| JSON-formated document describing the parent group to be set to or removed from a channel. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_channel_parent_group**
> set_channel_parent_group(body, domain_id, chan_id)

Sets a parent group for a channel

Sets a parent group for a specific channel that is identified by the channel ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ParentGroupReqObj() # ParentGroupReqObj | JSON-formated document describing the parent group to be set to or removed from a channel.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Sets a parent group for a channel
    api_instance.set_channel_parent_group(body, domain_id, chan_id)
except ApiException as e:
    print("Exception when calling ChannelsApi->set_channel_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParentGroupReqObj**](ParentGroupReqObj.md)| JSON-formated document describing the parent group to be set to or removed from a channel. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel**
> Channel update_channel(body, domain_id, chan_id)

Updates channel data.

Update is performed by replacing the current resource data with values provided in a request payload. Note that the channel's ID will not be affected. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelUpdate() # ChannelUpdate | JSON-formated document describing the metadata and name of channel to be updated.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Updates channel data.
    api_response = api_instance.update_channel(body, domain_id, chan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->update_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelUpdate**](ChannelUpdate.md)| JSON-formated document describing the metadata and name of channel to be updated. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

[**Channel**](Channel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel_tags**
> Channel update_channel_tags(body, domain_id, chan_id)

Updates channel tags.

Update is performed by replacing the current resource data with values provided in a request payload. Note that the channel's ID will not be affected. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelUpdateTags() # ChannelUpdateTags | JSON-formated document describing the tags of channel to be updated.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Updates channel tags.
    api_response = api_instance.update_channel_tags(body, domain_id, chan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->update_channel_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelUpdateTags**](ChannelUpdateTags.md)| JSON-formated document describing the tags of channel to be updated. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 

### Return type

[**Channel**](Channel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


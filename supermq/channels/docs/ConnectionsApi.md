# swagger_client.ConnectionsApi

All URIs are relative to *http://localhost:9005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_clients_and_channels**](ConnectionsApi.md#connect_clients_and_channels) | **POST** /{domainID}/channels/connect | Connects client and channel.
[**connect_clients_to_channel**](ConnectionsApi.md#connect_clients_to_channel) | **POST** /{domainID}/channels/{chanID}/connect | Connects clients to a channel
[**disconnect_clients_and_channels**](ConnectionsApi.md#disconnect_clients_and_channels) | **POST** /{domainID}/channels/disconnect | Disconnects client and channel.
[**disconnect_clients_from_channel**](ConnectionsApi.md#disconnect_clients_from_channel) | **POST** /{domainID}/channels/{chanID}/disconnect | Disconnects clients from a channel

# **connect_clients_and_channels**
> connect_clients_and_channels(body, domain_id)

Connects client and channel.

Connect clients specified by IDs to channels specified by IDs. Channel and client are owned by user identified using the provided access token. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectionReqSchema() # ConnectionReqSchema | JSON-formatted document describing the new connection.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Connects client and channel.
    api_instance.connect_clients_and_channels(body, domain_id)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connect_clients_and_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionReqSchema**](ConnectionReqSchema.md)| JSON-formatted document describing the new connection. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_clients_to_channel**
> connect_clients_to_channel(body, domain_id, chan_id)

Connects clients to a channel

Connects clients to a channel that is identified by the channel ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelConnectionReqSchema() # ChannelConnectionReqSchema | JSON-formatted document describing the new connection.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Connects clients to a channel
    api_instance.connect_clients_to_channel(body, domain_id, chan_id)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connect_clients_to_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelConnectionReqSchema**](ChannelConnectionReqSchema.md)| JSON-formatted document describing the new connection. | 
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

# **disconnect_clients_and_channels**
> disconnect_clients_and_channels(body, domain_id)

Disconnects client and channel.

Disconnect clients specified by IDs from channels specified by IDs. Channel and client are owned by user identified using the provided access token. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectionReqSchema() # ConnectionReqSchema | JSON-formatted document describing the new connection.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.

try:
    # Disconnects client and channel.
    api_instance.disconnect_clients_and_channels(body, domain_id)
except ApiException as e:
    print("Exception when calling ConnectionsApi->disconnect_clients_and_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionReqSchema**](ConnectionReqSchema.md)| JSON-formatted document describing the new connection. | 
 **domain_id** | [**str**](.md)| Unique domain identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_clients_from_channel**
> disconnect_clients_from_channel(body, domain_id, chan_id)

Disconnects clients from a channel

Disconnects clients to a channel that is identified by the channel ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelConnectionReqSchema() # ChannelConnectionReqSchema | JSON-formatted document describing the new connection.
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.

try:
    # Disconnects clients from a channel
    api_instance.disconnect_clients_from_channel(body, domain_id, chan_id)
except ApiException as e:
    print("Exception when calling ConnectionsApi->disconnect_clients_from_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelConnectionReqSchema**](ChannelConnectionReqSchema.md)| JSON-formatted document describing the new connection. | 
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


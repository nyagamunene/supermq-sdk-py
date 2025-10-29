# swagger_client.ReadersApi

All URIs are relative to *http://localhost:9003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_messages**](ReadersApi.md#get_messages) | **GET** /{domainID}/channels/{chanId}/messages | Retrieves messages sent to single channel

# **get_messages**
> MessagesPage get_messages(domain_id, chan_id, limit=limit, offset=offset, publisher=publisher, name=name, v=v, vb=vb, vs=vs, vd=vd, _from=_from, to=to, aggregation=aggregation, interval=interval)

Retrieves messages sent to single channel

Retrieves a list of messages sent to specific channel. Due to performance concerns, data is retrieved in subsets. The API readers must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReadersApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identifier.
chan_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique channel identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
publisher = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique thing identifier. (optional)
name = 'name_example' # str | SenML message name. (optional)
v = 'v_example' # str | SenML message value. (optional)
vb = true # bool | SenML message bool value. (optional)
vs = 'vs_example' # str | SenML message string value. (optional)
vd = 'vd_example' # str | SenML message data value. (optional)
_from = 1.2 # float | SenML message time in nanoseconds (integer part represents seconds). (optional)
to = 1.2 # float | SenML message time in nanoseconds (integer part represents seconds). (optional)
aggregation = 'aggregation_example' # str | Aggregation function. (optional)
interval = 'interval_example' # str | Aggregation interval. (optional)

try:
    # Retrieves messages sent to single channel
    api_response = api_instance.get_messages(domain_id, chan_id, limit=limit, offset=offset, publisher=publisher, name=name, v=v, vb=vb, vs=vs, vd=vd, _from=_from, to=to, aggregation=aggregation, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadersApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identifier. | 
 **chan_id** | [**str**](.md)| Unique channel identifier. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **publisher** | [**str**](.md)| Unique thing identifier. | [optional] 
 **name** | **str**| SenML message name. | [optional] 
 **v** | **str**| SenML message value. | [optional] 
 **vb** | **bool**| SenML message bool value. | [optional] 
 **vs** | **str**| SenML message string value. | [optional] 
 **vd** | **str**| SenML message data value. | [optional] 
 **_from** | **float**| SenML message time in nanoseconds (integer part represents seconds). | [optional] 
 **to** | **float**| SenML message time in nanoseconds (integer part represents seconds). | [optional] 
 **aggregation** | **str**| Aggregation function. | [optional] 
 **interval** | **str**| Aggregation interval. | [optional] 

### Return type

[**MessagesPage**](MessagesPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [thingAuth](../README.md#thingAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


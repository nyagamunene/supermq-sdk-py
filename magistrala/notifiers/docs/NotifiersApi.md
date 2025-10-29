# swagger_client.NotifiersApi

All URIs are relative to *http://localhost:9014*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](NotifiersApi.md#create_subscription) | **POST** /subscriptions | Create subscription
[**list_subscriptions**](NotifiersApi.md#list_subscriptions) | **GET** /subscriptions | List subscriptions
[**remove_subscription**](NotifiersApi.md#remove_subscription) | **DELETE** /subscriptions/{id} | Delete subscription with the provided id
[**view_subscription**](NotifiersApi.md#view_subscription) | **GET** /subscriptions/{id} | Get subscription with the provided id

# **create_subscription**
> create_subscription(body)

Create subscription

Creates a new subscription give a topic and contact.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NotifiersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSubscription() # CreateSubscription | JSON-formatted document describing the new subscription to be created

try:
    # Create subscription
    api_instance.create_subscription(body)
except ApiException as e:
    print("Exception when calling NotifiersApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubscription**](CreateSubscription.md)| JSON-formatted document describing the new subscription to be created | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> Page list_subscriptions(topic=topic, contact=contact, offset=offset, limit=limit)

List subscriptions

List subscriptions given list parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NotifiersApi(swagger_client.ApiClient(configuration))
topic = 'topic_example' # str | Topic name. (optional)
contact = 'contact_example' # str | Subscription contact. (optional)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)

try:
    # List subscriptions
    api_response = api_instance.list_subscriptions(topic=topic, contact=contact, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotifiersApi->list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**| Topic name. | [optional] 
 **contact** | **str**| Subscription contact. | [optional] 
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]

### Return type

[**Page**](Page.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_subscription**
> remove_subscription(id)

Delete subscription with the provided id

Removes a subscription with the provided id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NotifiersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier.

try:
    # Delete subscription with the provided id
    api_instance.remove_subscription(id)
except ApiException as e:
    print("Exception when calling NotifiersApi->remove_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_subscription**
> Subscription view_subscription(id)

Get subscription with the provided id

Retrieves a subscription with the provided id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NotifiersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique identifier.

try:
    # Get subscription with the provided id
    api_response = api_instance.view_subscription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotifiersApi->view_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier. | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


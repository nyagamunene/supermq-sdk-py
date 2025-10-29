# swagger_client.KeysApi

All URIs are relative to *http://localhost:9001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_key**](KeysApi.md#get_key) | **GET** /keys/{keyID} | Gets API key details.
[**issue_key**](KeysApi.md#issue_key) | **POST** /keys | Issue API key
[**revoke_key**](KeysApi.md#revoke_key) | **DELETE** /keys/{keyID} | Revoke API key

# **get_key**
> Key get_key(key_id)

Gets API key details.

Gets API key details for the given key. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
key_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | API Key ID.

try:
    # Gets API key details.
    api_response = api_instance.get_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->get_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**str**](.md)| API Key ID. | 

### Return type

[**Key**](Key.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_key**
> issue_key(body)

Issue API key

Generates a new API key. Thew new API key will be uniquely identified by its ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing key request.

try:
    # Issue API key
    api_instance.issue_key(body)
except ApiException as e:
    print("Exception when calling KeysApi->issue_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing key request. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_key**
> revoke_key(key_id)

Revoke API key

Revoke API key identified by the given ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
key_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | API Key ID.

try:
    # Revoke API key
    api_instance.revoke_key(key_id)
except ApiException as e:
    print("Exception when calling KeysApi->revoke_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**str**](.md)| API Key ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


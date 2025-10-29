# swagger_client.HealthApi

All URIs are relative to *http://localhost:9002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](HealthApi.md#health) | **GET** /health | Retrieves service health check info.

# **health**
> HealthRes health()

Retrieves service health check info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try:
    # Retrieves service health check info.
    api_response = api_instance.health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthRes**](HealthRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/health+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


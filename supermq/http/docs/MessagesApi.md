# swagger_client.MessagesApi

All URIs are relative to *http://localhost:8008*

Method | HTTP request | Description
------------- | ------------- | -------------
[**m_domain_prefix_c_channel_prefix_post**](MessagesApi.md#m_domain_prefix_c_channel_prefix_post) | **POST** /m/{domainPrefix}/c/{channelPrefix} | Sends message to the communication channel

# **m_domain_prefix_c_channel_prefix_post**
> m_domain_prefix_c_channel_prefix_post(body, domain_prefix, channel_prefix)

Sends message to the communication channel

Sends message to the communication channel. Messages can be sent as JSON formatted SenML or as blob. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.SenMLRecord()] # list[SenMLRecord] | Message to be distributed. Since the platform expects messages to be
properly formatted SenML in order to be post-processed, clients are
obliged to specify Content-Type header for each published message.
Note that all messages that aren't SenML will be accepted and published,
but no post-processing will be applied.

domain_prefix = 'domain_prefix_example' # str | ID or route of the domain associated with the channel and client.
channel_prefix = 'channel_prefix_example' # str | ID or route of the channel connected to the client.

try:
    # Sends message to the communication channel
    api_instance.m_domain_prefix_c_channel_prefix_post(body, domain_prefix, channel_prefix)
except ApiException as e:
    print("Exception when calling MessagesApi->m_domain_prefix_c_channel_prefix_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SenMLRecord]**](SenMLRecord.md)| Message to be distributed. Since the platform expects messages to be
properly formatted SenML in order to be post-processed, clients are
obliged to specify Content-Type header for each published message.
Note that all messages that aren&#x27;t SenML will be accepted and published,
but no post-processing will be applied.
 | 
 **domain_prefix** | **str**| ID or route of the domain associated with the channel and client. | 
 **channel_prefix** | **str**| ID or route of the channel connected to the client. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


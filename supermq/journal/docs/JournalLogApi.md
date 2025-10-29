# swagger_client.JournalLogApi

All URIs are relative to *http://localhost:9021*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_id_journal_client_client_id_telemetry_get**](JournalLogApi.md#domain_id_journal_client_client_id_telemetry_get) | **GET** /{domainID}/journal/client/{clientID}/telemetry | View client telemetry
[**domain_id_journal_entity_type_id_get**](JournalLogApi.md#domain_id_journal_entity_type_id_get) | **GET** /{domainID}/journal/{entityType}/{id} | List entity journal log
[**journal_user_user_id_get**](JournalLogApi.md#journal_user_user_id_get) | **GET** /journal/user/{userID} | List user journal log

# **domain_id_journal_client_client_id_telemetry_get**
> Telemetry domain_id_journal_client_client_id_telemetry_get(domain_id, client_id)

View client telemetry

Retrieves telemetry data for a specific client within a domain. This includes connection status, messages sent/received, and other metrics. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JournalLogApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for a domain.
client_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for a client

try:
    # View client telemetry
    api_response = api_instance.domain_id_journal_client_client_id_telemetry_get(domain_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalLogApi->domain_id_journal_client_client_id_telemetry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique identifier for a domain. | 
 **client_id** | [**str**](.md)| Unique identifier for a client | 

### Return type

[**Telemetry**](Telemetry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_id_journal_entity_type_id_get**
> JournalPage domain_id_journal_entity_type_id_get(domain_id, entity_type, id, offset=offset, limit=limit, operation=operation, with_attributes=with_attributes, with_metadata=with_metadata, _from=_from, to=to, dir=dir)

List entity journal log

Retrieves a list of journal. Due to performance concerns, data is retrieved in subsets. The API must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JournalLogApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for a domain.
entity_type = 'entity_type_example' # str | Type of entity, e.g. group, client, channel.
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for an entity, e.g. group, channel or client. Used together with entity_type.
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
operation = 'operation_example' # str | Journal operation. (optional)
with_attributes = true # bool | Include journal attributes. (optional)
with_metadata = true # bool | Include journal metadata. (optional)
_from = '_from_example' # str | Start date in unix time. (optional)
to = 'to_example' # str | End date in unix time. (optional)
dir = 'dir_example' # str | Sort direction. (optional)

try:
    # List entity journal log
    api_response = api_instance.domain_id_journal_entity_type_id_get(domain_id, entity_type, id, offset=offset, limit=limit, operation=operation, with_attributes=with_attributes, with_metadata=with_metadata, _from=_from, to=to, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalLogApi->domain_id_journal_entity_type_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique identifier for a domain. | 
 **entity_type** | **str**| Type of entity, e.g. group, client, channel. | 
 **id** | [**str**](.md)| Unique identifier for an entity, e.g. group, channel or client. Used together with entity_type. | 
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **operation** | **str**| Journal operation. | [optional] 
 **with_attributes** | **bool**| Include journal attributes. | [optional] 
 **with_metadata** | **bool**| Include journal metadata. | [optional] 
 **_from** | **str**| Start date in unix time. | [optional] 
 **to** | **str**| End date in unix time. | [optional] 
 **dir** | **str**| Sort direction. | [optional] 

### Return type

[**JournalPage**](JournalPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_user_user_id_get**
> JournalPage journal_user_user_id_get(user_id, offset=offset, limit=limit, operation=operation, with_attributes=with_attributes, with_metadata=with_metadata, _from=_from, to=to, dir=dir)

List user journal log

Retrieves a list of journal. Due to performance concerns, data is retrieved in subsets. The API must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JournalLogApi(swagger_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for a user.
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
operation = 'operation_example' # str | Journal operation. (optional)
with_attributes = true # bool | Include journal attributes. (optional)
with_metadata = true # bool | Include journal metadata. (optional)
_from = '_from_example' # str | Start date in unix time. (optional)
to = 'to_example' # str | End date in unix time. (optional)
dir = 'dir_example' # str | Sort direction. (optional)

try:
    # List user journal log
    api_response = api_instance.journal_user_user_id_get(user_id, offset=offset, limit=limit, operation=operation, with_attributes=with_attributes, with_metadata=with_metadata, _from=_from, to=to, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalLogApi->journal_user_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Unique identifier for a user. | 
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **operation** | **str**| Journal operation. | [optional] 
 **with_attributes** | **bool**| Include journal attributes. | [optional] 
 **with_metadata** | **bool**| Include journal metadata. | [optional] 
 **_from** | **str**| Start date in unix time. | [optional] 
 **to** | **str**| End date in unix time. | [optional] 
 **dir** | **str**| Sort direction. | [optional] 

### Return type

[**JournalPage**](JournalPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.ReportsApi

All URIs are relative to *http://localhost:9017*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_report_config**](ReportsApi.md#add_report_config) | **POST** /{domainID}/reports/configs | Create a report configuration
[**delete_report_config**](ReportsApi.md#delete_report_config) | **DELETE** /{domainID}/reports/configs/{reportID} | Delete a report configuration
[**disable_report_config**](ReportsApi.md#disable_report_config) | **POST** /{domainID}/reports/configs/{reportID}/disable | Disable a report configuration
[**enable_report_config**](ReportsApi.md#enable_report_config) | **POST** /{domainID}/reports/configs/{reportID}/enable | Enable a report configuration
[**generate_report**](ReportsApi.md#generate_report) | **POST** /{domainID}/reports | Generate a report
[**list_report_configs**](ReportsApi.md#list_report_configs) | **GET** /{domainID}/reports/configs | List report configurations
[**update_report_config**](ReportsApi.md#update_report_config) | **PATCH** /{domainID}/reports/configs/{reportID} | Update a report configuration
[**update_report_schedule**](ReportsApi.md#update_report_schedule) | **PATCH** /{domainID}/reports/configs/{reportID}/schedule | Update report schedule
[**view_report_config**](ReportsApi.md#view_report_config) | **GET** /{domainID}/reports/configs/{reportID} | View a report configuration

# **add_report_config**
> ReportConfig add_report_config(domain_id, body=body)

Create a report configuration

Creates a new report configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
body = swagger_client.AddReportConfigRequest() # AddReportConfigRequest |  (optional)

try:
    # Create a report configuration
    api_response = api_instance.add_report_config(domain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->add_report_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **body** | [**AddReportConfigRequest**](AddReportConfigRequest.md)|  | [optional] 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_config**
> delete_report_config(domain_id, report_id)

Delete a report configuration

Permanently deletes a report configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
report_id = 'report_id_example' # str | 

try:
    # Delete a report configuration
    api_instance.delete_report_config(domain_id, report_id)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_report_config**
> ReportConfig disable_report_config(domain_id, report_id)

Disable a report configuration

Disables a report configuration, stopping scheduled reports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
report_id = 'report_id_example' # str | 

try:
    # Disable a report configuration
    api_response = api_instance.disable_report_config(domain_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->disable_report_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_report_config**
> ReportConfig enable_report_config(domain_id, report_id)

Enable a report configuration

Enables a report configuration to generate scheduled reports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
report_id = 'report_id_example' # str | 

try:
    # Enable a report configuration
    api_response = api_instance.enable_report_config(domain_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->enable_report_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_report**
> GenerateReportResponse generate_report(domain_id, body=body)

Generate a report

Generates a report based on the provided configuration or an existing config. The action determines the response format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
body = swagger_client.GenerateReportRequest() # GenerateReportRequest |  (optional)

try:
    # Generate a report
    api_response = api_instance.generate_report(domain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **body** | [**GenerateReportRequest**](GenerateReportRequest.md)|  | [optional] 

### Return type

[**GenerateReportResponse**](GenerateReportResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_report_configs**
> ListReportsConfigResponse list_report_configs(domain_id, offset=offset, limit=limit)

List report configurations

Retrieves a paginated list of report configurations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 10 # int |  (optional) (default to 10)

try:
    # List report configurations
    api_response = api_instance.list_report_configs(domain_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->list_report_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**ListReportsConfigResponse**](ListReportsConfigResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_config**
> ReportConfig update_report_config(domain_id, report_id, body=body)

Update a report configuration

Updates specified fields of a report configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
report_id = 'report_id_example' # str | 
body = swagger_client.UpdateReportConfigRequest() # UpdateReportConfigRequest |  (optional)

try:
    # Update a report configuration
    api_response = api_instance.update_report_config(domain_id, report_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **report_id** | **str**|  | 
 **body** | [**UpdateReportConfigRequest**](UpdateReportConfigRequest.md)|  | [optional] 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_schedule**
> ReportConfig update_report_schedule(domain_id, report_id, body=body)

Update report schedule

Updates the schedule of a report configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
report_id = 'report_id_example' # str | 
body = swagger_client.Schedule() # Schedule |  (optional)

try:
    # Update report schedule
    api_response = api_instance.update_report_schedule(domain_id, report_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **report_id** | **str**|  | 
 **body** | [**Schedule**](Schedule.md)|  | [optional] 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_report_config**
> ReportConfig view_report_config(domain_id, report_id)

View a report configuration

Retrieves details of a specific report configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 
report_id = 'report_id_example' # str | 

try:
    # View a report configuration
    api_response = api_instance.view_report_config(domain_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->view_report_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


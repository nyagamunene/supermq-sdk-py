# swagger_client.AlarmsApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alarm**](AlarmsApi.md#delete_alarm) | **DELETE** /{domainID}/alarms/{alarmID} | Delete Alarm
[**list_alarms**](AlarmsApi.md#list_alarms) | **GET** /{domainID}/alarms | List Alarms
[**update_alarm**](AlarmsApi.md#update_alarm) | **PUT** /{domainID}/alarms/{alarmID} | Update Alarm
[**view_alarm**](AlarmsApi.md#view_alarm) | **GET** /{domainID}/alarms/{alarmID} | View Alarm

# **delete_alarm**
> delete_alarm(domain_id, alarm_id)

Delete Alarm

Deletes an alarm

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlarmsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Domain ID
alarm_id = 'alarm_id_example' # str | Alarm ID

try:
    # Delete Alarm
    api_instance.delete_alarm(domain_id, alarm_id)
except ApiException as e:
    print("Exception when calling AlarmsApi->delete_alarm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID | 
 **alarm_id** | **str**| Alarm ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alarms**
> AlarmsPage list_alarms(domain_id, offset=offset, limit=limit, order=order, dir=dir, channel_id=channel_id, client_id=client_id, subtopic=subtopic, rule_id=rule_id, status=status, assignee_id=assignee_id, severity=severity, updated_by=updated_by, assigned_by=assigned_by, acknowledged_by=acknowledged_by, resolved_by=resolved_by, created_from=created_from, created_to=created_to)

List Alarms

Retrieves a list of alarms with optional filtering 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlarmsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Domain ID
offset = 0 # int | Number of items to skip (optional) (default to 0)
limit = 10 # int | Size of the subset to retrieve (optional) (default to 10)
order = 'created_at' # str | Order by field (optional) (default to created_at)
dir = 'desc' # str | Sort direction (optional) (default to desc)
channel_id = 'channel_id_example' # str | Filter by channel ID (optional)
client_id = 'client_id_example' # str | Filter by client ID (optional)
subtopic = 'subtopic_example' # str | Filter by subtopic (optional)
rule_id = 'rule_id_example' # str | Filter by rule ID (optional)
status = 'all' # str | Filter by alarm status (optional) (default to all)
assignee_id = 'assignee_id_example' # str | Filter by assignee ID (optional)
severity = 56 # int | Filter by severity level (optional)
updated_by = 'updated_by_example' # str | Filter by user who updated (optional)
assigned_by = 'assigned_by_example' # str | Filter by user who assigned (optional)
acknowledged_by = 'acknowledged_by_example' # str | Filter by user who acknowledged (optional)
resolved_by = 'resolved_by_example' # str | Filter by user who resolved (optional)
created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter alarms created after this time (RFC3339 format) (optional)
created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter alarms created before this time (RFC3339 format) (optional)

try:
    # List Alarms
    api_response = api_instance.list_alarms(domain_id, offset=offset, limit=limit, order=order, dir=dir, channel_id=channel_id, client_id=client_id, subtopic=subtopic, rule_id=rule_id, status=status, assignee_id=assignee_id, severity=severity, updated_by=updated_by, assigned_by=assigned_by, acknowledged_by=acknowledged_by, resolved_by=resolved_by, created_from=created_from, created_to=created_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsApi->list_alarms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID | 
 **offset** | **int**| Number of items to skip | [optional] [default to 0]
 **limit** | **int**| Size of the subset to retrieve | [optional] [default to 10]
 **order** | **str**| Order by field | [optional] [default to created_at]
 **dir** | **str**| Sort direction | [optional] [default to desc]
 **channel_id** | **str**| Filter by channel ID | [optional] 
 **client_id** | **str**| Filter by client ID | [optional] 
 **subtopic** | **str**| Filter by subtopic | [optional] 
 **rule_id** | **str**| Filter by rule ID | [optional] 
 **status** | **str**| Filter by alarm status | [optional] [default to all]
 **assignee_id** | **str**| Filter by assignee ID | [optional] 
 **severity** | **int**| Filter by severity level | [optional] 
 **updated_by** | **str**| Filter by user who updated | [optional] 
 **assigned_by** | **str**| Filter by user who assigned | [optional] 
 **acknowledged_by** | **str**| Filter by user who acknowledged | [optional] 
 **resolved_by** | **str**| Filter by user who resolved | [optional] 
 **created_from** | **datetime**| Filter alarms created after this time (RFC3339 format) | [optional] 
 **created_to** | **datetime**| Filter alarms created before this time (RFC3339 format) | [optional] 

### Return type

[**AlarmsPage**](AlarmsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alarm**
> Alarm update_alarm(body, domain_id, alarm_id)

Update Alarm

Updates an existing alarm

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlarmsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing the alarm update
domain_id = 'domain_id_example' # str | Domain ID
alarm_id = 'alarm_id_example' # str | Alarm ID

try:
    # Update Alarm
    api_response = api_instance.update_alarm(body, domain_id, alarm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsApi->update_alarm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing the alarm update | 
 **domain_id** | **str**| Domain ID | 
 **alarm_id** | **str**| Alarm ID | 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_alarm**
> Alarm view_alarm(domain_id, alarm_id)

View Alarm

Retrieves an alarm by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlarmsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Domain ID
alarm_id = 'alarm_id_example' # str | Alarm ID

try:
    # View Alarm
    api_response = api_instance.view_alarm(domain_id, alarm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsApi->view_alarm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID | 
 **alarm_id** | **str**| Alarm ID | 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


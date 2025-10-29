# swagger_client.RulesApi

All URIs are relative to *http://localhost:9008*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rule**](RulesApi.md#create_rule) | **POST** /{domainID}/rules | Create Rule
[**enable_rule**](RulesApi.md#enable_rule) | **PUT** /{domainID}/rules/{ruleID}/enable | Enable Rule
[**get_rule**](RulesApi.md#get_rule) | **GET** /{domainID}/rules/{ruleID} | View Rule
[**get_rules**](RulesApi.md#get_rules) | **GET** /{domainID}/rules | List Rules
[**remove_rule**](RulesApi.md#remove_rule) | **DELETE** /{domainID}/rules/{ruleID} | Delete Rule
[**update_rule**](RulesApi.md#update_rule) | **PUT** /{domainID}/rules/{ruleID} | Update Rule

# **create_rule**
> create_rule(body, domain_id)

Create Rule

Creates a new rule for message processing 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing the new rule
domain_id = 'domain_id_example' # str | Domain ID

try:
    # Create Rule
    api_instance.create_rule(body, domain_id)
except ApiException as e:
    print("Exception when calling RulesApi->create_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing the new rule | 
 **domain_id** | **str**| Domain ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_rule**
> enable_rule(domain_id, rule_id)

Enable Rule

Enables a rule for processing

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Domain ID
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Enable Rule
    api_instance.enable_rule(domain_id, rule_id)
except ApiException as e:
    print("Exception when calling RulesApi->enable_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID | 
 **rule_id** | **str**| Rule ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> Rule get_rule(domain_id, rule_id)

View Rule

Retrieves a rule by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Domain ID
rule_id = 'rule_id_example' # str | Rule ID

try:
    # View Rule
    api_response = api_instance.get_rule(domain_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID | 
 **rule_id** | **str**| Rule ID | 

### Return type

[**Rule**](Rule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules**
> RulesListRes get_rules(domain_id, offset=offset, limit=limit, input_channel=input_channel, output_channel=output_channel, status=status)

List Rules

Retrieves a list of rules with optional filtering 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Domain ID
offset = 0 # int | Number of items to skip (optional) (default to 0)
limit = 10 # int | Size of the subset (optional) (default to 10)
input_channel = 'input_channel_example' # str | Filter by input channel (optional)
output_channel = 'output_channel_example' # str | Filter by output channel (optional)
status = 'enabled' # str | Filter by rule status (optional) (default to enabled)

try:
    # List Rules
    api_response = api_instance.get_rules(domain_id, offset=offset, limit=limit, input_channel=input_channel, output_channel=output_channel, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID | 
 **offset** | **int**| Number of items to skip | [optional] [default to 0]
 **limit** | **int**| Size of the subset | [optional] [default to 10]
 **input_channel** | **str**| Filter by input channel | [optional] 
 **output_channel** | **str**| Filter by output channel | [optional] 
 **status** | **str**| Filter by rule status | [optional] [default to enabled]

### Return type

[**RulesListRes**](RulesListRes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_rule**
> remove_rule(domain_id, rule_id)

Delete Rule

Deletes a rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Domain ID
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Delete Rule
    api_instance.remove_rule(domain_id, rule_id)
except ApiException as e:
    print("Exception when calling RulesApi->remove_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID | 
 **rule_id** | **str**| Rule ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> Rule update_rule(body, domain_id, rule_id)

Update Rule

Updates an existing rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing the rule update
domain_id = 'domain_id_example' # str | Domain ID
rule_id = 'rule_id_example' # str | Rule ID

try:
    # Update Rule
    api_response = api_instance.update_rule(body, domain_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing the rule update | 
 **domain_id** | **str**| Domain ID | 
 **rule_id** | **str**| Rule ID | 

### Return type

[**Rule**](Rule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


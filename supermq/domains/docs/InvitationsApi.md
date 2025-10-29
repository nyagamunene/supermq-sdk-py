# swagger_client.InvitationsApi

All URIs are relative to *http://localhost:9003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation**](InvitationsApi.md#accept_invitation) | **POST** /invitations/accept | Accept invitation
[**delete_invitation**](InvitationsApi.md#delete_invitation) | **DELETE** /domains/{domainID}/invitations | Deletes a specific invitation
[**list_domain_invitations**](InvitationsApi.md#list_domain_invitations) | **GET** /domains/{domainID}/invitations | List domain invitations
[**list_user_invitations**](InvitationsApi.md#list_user_invitations) | **GET** /invitations | List user invitations
[**reject_invitation**](InvitationsApi.md#reject_invitation) | **POST** /invitations/reject | Reject invitation
[**send_invitation**](InvitationsApi.md#send_invitation) | **POST** /domains/{domainID}/invitations | Send invitation

# **accept_invitation**
> accept_invitation(body)

Accept invitation

Current logged in user accepts invitation to join domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing request for accepting invitation

try:
    # Accept invitation
    api_instance.accept_invitation(body)
except ApiException as e:
    print("Exception when calling InvitationsApi->accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing request for accepting invitation | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invitation**
> delete_invitation(body, domain_id)

Deletes a specific invitation

Deletes a specific invitation that is identified by the user ID and domain ID. The user ID is provided in the request body. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing request for deleting invitation
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Deletes a specific invitation
    api_instance.delete_invitation(body, domain_id)
except ApiException as e:
    print("Exception when calling InvitationsApi->delete_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing request for deleting invitation | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_invitations**
> InvitationPage list_domain_invitations(domain_id, limit=limit, offset=offset, user_id=user_id, invited_by=invited_by, state=state)

List domain invitations

Retrieves a list of invitations for a given domain. Due to performance concerns, data is retrieved in subsets. The API must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier. (optional)
invited_by = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for a user that invited the user. (optional)
state = 'state_example' # str | Invitation state. (optional)

try:
    # List domain invitations
    api_response = api_instance.list_domain_invitations(domain_id, limit=limit, offset=offset, user_id=user_id, invited_by=invited_by, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->list_domain_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique domain identified. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **user_id** | [**str**](.md)| Unique user identifier. | [optional] 
 **invited_by** | [**str**](.md)| Unique identifier for a user that invited the user. | [optional] 
 **state** | **str**| Invitation state. | [optional] 

### Return type

[**InvitationPage**](InvitationPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_invitations**
> InvitationPage list_user_invitations(domain_id=domain_id, limit=limit, offset=offset, user_id=user_id, invited_by=invited_by, state=state)

List user invitations

Retrieves a list of invitations for the current user. Due to performance concerns, data is retrieved in subsets. The API must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationsApi(swagger_client.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for a domain. (optional)
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier. (optional)
invited_by = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier for a user that invited the user. (optional)
state = 'state_example' # str | Invitation state. (optional)

try:
    # List user invitations
    api_response = api_instance.list_user_invitations(domain_id=domain_id, limit=limit, offset=offset, user_id=user_id, invited_by=invited_by, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->list_user_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| Unique identifier for a domain. | [optional] 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **user_id** | [**str**](.md)| Unique user identifier. | [optional] 
 **invited_by** | [**str**](.md)| Unique identifier for a user that invited the user. | [optional] 
 **state** | **str**| Invitation state. | [optional] 

### Return type

[**InvitationPage**](InvitationPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_invitation**
> reject_invitation(body)

Reject invitation

Current logged in user rejects invitation to join domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing request for accepting invitation

try:
    # Reject invitation
    api_instance.reject_invitation(body)
except ApiException as e:
    print("Exception when calling InvitationsApi->reject_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing request for accepting invitation | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_invitation**
> send_invitation(body, domain_id)

Send invitation

Send invitation to user to join domain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InvitationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SendInvitationReqObj() # SendInvitationReqObj | JSON-formatted document describing request for sending invitation
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique domain identified.

try:
    # Send invitation
    api_instance.send_invitation(body, domain_id)
except ApiException as e:
    print("Exception when calling InvitationsApi->send_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendInvitationReqObj**](SendInvitationReqObj.md)| JSON-formatted document describing request for sending invitation | 
 **domain_id** | [**str**](.md)| Unique domain identified. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


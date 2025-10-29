# swagger_client.PATsApi

All URIs are relative to *http://localhost:9001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scope**](PATsApi.md#add_scope) | **PATCH** /pats/{patID}/scope/add | Add scope to a Personal Access Token
[**clear_all_pats**](PATsApi.md#clear_all_pats) | **DELETE** /pats | Remove all Personal Access Tokens
[**clear_all_scopes**](PATsApi.md#clear_all_scopes) | **DELETE** /pats/{patID}/scope | Remove all scopes from a Personal Access Token
[**create_pat**](PATsApi.md#create_pat) | **POST** /pats | Create a new Personal Access Token
[**delete_pat**](PATsApi.md#delete_pat) | **DELETE** /pats/{patID} | Delete a Personal Access Token
[**list_pats**](PATsApi.md#list_pats) | **GET** /pats | List all Personal Access Tokens
[**list_scopes**](PATsApi.md#list_scopes) | **GET** /pats/{patID}/scope | List scopes for a Personal Access Token
[**remove_scope**](PATsApi.md#remove_scope) | **PATCH** /pats/{patID}/scope/remove | Remove scope from a Personal Access Token
[**reset_pat_secret**](PATsApi.md#reset_pat_secret) | **PATCH** /pats/{patID}/secret/reset | Reset Personal Access Token secret
[**retrieve_pat**](PATsApi.md#retrieve_pat) | **GET** /pats/{patID} | Retrieve a Personal Access Token
[**revoke_pat_secret**](PATsApi.md#revoke_pat_secret) | **PATCH** /pats/{patID}/secret/revoke | Revoke Personal Access Token secret
[**update_pat_description**](PATsApi.md#update_pat_description) | **PATCH** /pats/{patID}/description | Update Personal Access Token description
[**update_pat_name**](PATsApi.md#update_pat_name) | **PATCH** /pats/{patID}/name | Update Personal Access Token name

# **add_scope**
> add_scope(body, pat_id)

Add scope to a Personal Access Token

Adds a scope to a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing add scope request.
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Add scope to a Personal Access Token
    api_instance.add_scope(body, pat_id)
except ApiException as e:
    print("Exception when calling PATsApi->add_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing add scope request. | 
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_all_pats**
> clear_all_pats()

Remove all Personal Access Tokens

Removes all Personal Access Tokens (PATs) for the authenticated user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))

try:
    # Remove all Personal Access Tokens
    api_instance.clear_all_pats()
except ApiException as e:
    print("Exception when calling PATsApi->clear_all_pats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_all_scopes**
> clear_all_scopes(pat_id)

Remove all scopes from a Personal Access Token

Removes all scopes from a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Remove all scopes from a Personal Access Token
    api_instance.clear_all_scopes(pat_id)
except ApiException as e:
    print("Exception when calling PATsApi->clear_all_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pat**
> PAT create_pat(body)

Create a new Personal Access Token

Creates a new Personal Access Token (PAT) for the authenticated user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing PAT creation request.

try:
    # Create a new Personal Access Token
    api_response = api_instance.create_pat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PATsApi->create_pat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing PAT creation request. | 

### Return type

[**PAT**](PAT.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pat**
> delete_pat(pat_id)

Delete a Personal Access Token

Deletes a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Delete a Personal Access Token
    api_instance.delete_pat(pat_id)
except ApiException as e:
    print("Exception when calling PATsApi->delete_pat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pats**
> PATsPage list_pats(limit=limit, offset=offset)

List all Personal Access Tokens

Lists all Personal Access Tokens (PATs) for the authenticated user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)

try:
    # List all Personal Access Tokens
    api_response = api_instance.list_pats(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PATsApi->list_pats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]

### Return type

[**PATsPage**](PATsPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scopes**
> ScopesPage list_scopes(pat_id, limit=limit, offset=offset)

List scopes for a Personal Access Token

Lists all scopes for a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)

try:
    # List scopes for a Personal Access Token
    api_response = api_instance.list_scopes(pat_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PATsApi->list_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]

### Return type

[**ScopesPage**](ScopesPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_scope**
> remove_scope(body, pat_id)

Remove scope from a Personal Access Token

Removes a scope from a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing remove scope request.
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Remove scope from a Personal Access Token
    api_instance.remove_scope(body, pat_id)
except ApiException as e:
    print("Exception when calling PATsApi->remove_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing remove scope request. | 
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_pat_secret**
> PAT reset_pat_secret(body, pat_id)

Reset Personal Access Token secret

Resets the secret of a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing PAT secret reset request.
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Reset Personal Access Token secret
    api_response = api_instance.reset_pat_secret(body, pat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PATsApi->reset_pat_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing PAT secret reset request. | 
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

[**PAT**](PAT.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_pat**
> PAT retrieve_pat(pat_id)

Retrieve a Personal Access Token

Retrieves details of a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Retrieve a Personal Access Token
    api_response = api_instance.retrieve_pat(pat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PATsApi->retrieve_pat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

[**PAT**](PAT.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_pat_secret**
> revoke_pat_secret(pat_id)

Revoke Personal Access Token secret

Revokes the secret of a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Revoke Personal Access Token secret
    api_instance.revoke_pat_secret(pat_id)
except ApiException as e:
    print("Exception when calling PATsApi->revoke_pat_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pat_description**
> PAT update_pat_description(body, pat_id)

Update Personal Access Token description

Updates the description of a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing PAT description update request.
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Update Personal Access Token description
    api_response = api_instance.update_pat_description(body, pat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PATsApi->update_pat_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing PAT description update request. | 
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

[**PAT**](PAT.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pat_name**
> PAT update_pat_name(body, pat_id)

Update Personal Access Token name

Updates the name of a specific Personal Access Token (PAT). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PATsApi(swagger_client.ApiClient(configuration))
body = NULL # object | JSON-formatted document describing PAT name update request.
pat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Personal Access Token ID.

try:
    # Update Personal Access Token name
    api_response = api_instance.update_pat_name(body, pat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PATsApi->update_pat_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON-formatted document describing PAT name update request. | 
 **pat_id** | [**str**](.md)| Personal Access Token ID. | 

### Return type

[**PAT**](PAT.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


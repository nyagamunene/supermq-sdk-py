# swagger_client.UsersApi

All URIs are relative to *http://localhost:9002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Registers user account
[**disable_user**](UsersApi.md#disable_user) | **POST** /users/{userID}/disable | Disables a user
[**enable_user**](UsersApi.md#enable_user) | **POST** /users/{userID}/enable | Enables a user
[**get_profile**](UsersApi.md#get_profile) | **GET** /users/profile | Gets info on currently logged in user.
[**get_user**](UsersApi.md#get_user) | **GET** /users/{userID} | Retrieves a user
[**issue_token**](UsersApi.md#issue_token) | **POST** /users/tokens/issue | Issue Token
[**list_users**](UsersApi.md#list_users) | **GET** /users | List users
[**refresh_token**](UsersApi.md#refresh_token) | **POST** /users/tokens/refresh | Refresh Token
[**request_password_reset**](UsersApi.md#request_password_reset) | **POST** /password/reset-request | User password reset request
[**reset_password**](UsersApi.md#reset_password) | **PUT** /password/reset | User password reset endpoint
[**search_users**](UsersApi.md#search_users) | **GET** /users/search | Search users
[**send_verification**](UsersApi.md#send_verification) | **POST** /users/send-verification | Sends a verification email
[**update_email**](UsersApi.md#update_email) | **PATCH** /users/{userID}/email | Updates email of the user.
[**update_profile_picture**](UsersApi.md#update_profile_picture) | **PATCH** /users/{userID}/picture | Updates the user&#x27;s profile picture.
[**update_role**](UsersApi.md#update_role) | **PATCH** /users/{userID}/role | Updates the user&#x27;s role.
[**update_secret**](UsersApi.md#update_secret) | **PATCH** /users/secret | Updates secret of currently logged in user.
[**update_tags**](UsersApi.md#update_tags) | **PATCH** /users/{userID}/tags | Updates tags of the user.
[**update_user**](UsersApi.md#update_user) | **PATCH** /users/{userID} | Updates first, last name and metadata of the user.
[**update_username**](UsersApi.md#update_username) | **PATCH** /users/{userID}/username | Updates user&#x27;s username.
[**users_user_id_delete**](UsersApi.md#users_user_id_delete) | **DELETE** /users/{userID} | Delete a user
[**verify_email**](UsersApi.md#verify_email) | **GET** /verify-email | Verify user&#x27;s email

# **create_user**
> User create_user(body)

Registers user account

Registers new user account given email and password. New account will be uniquely identified by its email address. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UserReqObj() # UserReqObj | JSON-formatted document describing the new user to be registered

try:
    # Registers user account
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserReqObj**](UserReqObj.md)| JSON-formatted document describing the new user to be registered | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_user**
> User disable_user(user_id)

Disables a user

Disables a specific user that is identifier by the user ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Disables a user
    api_response = api_instance.disable_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->disable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_user**
> User enable_user(user_id)

Enables a user

Enables a specific user that is identifier by the user ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Enables a user
    api_response = api_instance.enable_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->enable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> User get_profile()

Gets info on currently logged in user.

Gets info on currently logged in user. Info is obtained using authorization token 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Gets info on currently logged in user.
    api_response = api_instance.get_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Retrieves a user

Retrieves a specific user that is identifier by the user ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Retrieves a user
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_token**
> InlineResponse200 issue_token(body)

Issue Token

Issue Access and Refresh Token used for authenticating into the system. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.IssueToken() # IssueToken | Login credentials.

try:
    # Issue Token
    api_response = api_instance.issue_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->issue_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IssueToken**](IssueToken.md)| Login credentials. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [refreshAuth](../README.md#refreshAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> UsersPage list_users(limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, first_name=first_name, last_name=last_name, username=username, email=email, tag=tag, only_total=only_total)

List users

Retrieves a list of users. Due to performance concerns, data is retrieved in subsets. The API must ensure that the entire dataset is consumed either by making subsequent requests, or by increasing the subset size of the initial request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
order = 'order_example' # str | Field by which to order the results (optional)
dir = 'dir_example' # str | Direction of ordering the results. (optional)
metadata = swagger_client.Metadata() # Metadata | Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. (optional)
status = 'enabled' # str | User account status. (optional) (default to enabled)
first_name = 'first_name_example' # str | User's first name. (optional)
last_name = 'last_name_example' # str | User's last name. (optional)
username = 'username_example' # str | User's username. (optional)
email = 'email_example' # str | User's email address. (optional)
tag = 'tag_example' # str | User tag. (optional)
only_total = false # bool | If true, the response will contain only the total number of users that match the query parameters. (optional) (default to false)

try:
    # List users
    api_response = api_instance.list_users(limit=limit, offset=offset, order=order, dir=dir, metadata=metadata, status=status, first_name=first_name, last_name=last_name, username=username, email=email, tag=tag, only_total=only_total)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **order** | **str**| Field by which to order the results | [optional] 
 **dir** | **str**| Direction of ordering the results. | [optional] 
 **metadata** | [**Metadata**](.md)| Metadata filter. Filtering is performed matching the parameter with metadata on top level. Parameter is json. | [optional] 
 **status** | **str**| User account status. | [optional] [default to enabled]
 **first_name** | **str**| User&#x27;s first name. | [optional] 
 **last_name** | **str**| User&#x27;s last name. | [optional] 
 **username** | **str**| User&#x27;s username. | [optional] 
 **email** | **str**| User&#x27;s email address. | [optional] 
 **tag** | **str**| User tag. | [optional] 
 **only_total** | **bool**| If true, the response will contain only the total number of users that match the query parameters. | [optional] [default to false]

### Return type

[**UsersPage**](UsersPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> InlineResponse200 refresh_token()

Refresh Token

Refreshes Access and Refresh Token used for authenticating into the system. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Refresh Token
    api_response = api_instance.refresh_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->refresh_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[refreshAuth](../README.md#refreshAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_reset**
> request_password_reset(body, referer)

User password reset request

Generates a reset token and sends and email with link for resetting password. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = NULL # object | Initiate password request procedure.
referer = 'referer_example' # str | Host being sent by browser.

try:
    # User password reset request
    api_instance.request_password_reset(body, referer)
except ApiException as e:
    print("Exception when calling UsersApi->request_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Initiate password request procedure. | 
 **referer** | **str**| Host being sent by browser. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth), [refreshAuth](../README.md#refreshAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(body=body)

User password reset endpoint

When user gets reset token, after he submitted email to `/password/reset-request`, posting a   new password along to this endpoint will change password. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = NULL # object | Password reset request data, new password and token that is appended on password reset link received in email. (optional)

try:
    # User password reset endpoint
    api_instance.reset_password(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Password reset request data, new password and token that is appended on password reset link received in email. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth), [refreshAuth](../README.md#refreshAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> UsersPage search_users(user_id, limit=limit, offset=offset, username=username, first_name=first_name, last_name=last_name, email=email)

Search users

Search users by name and identity. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.
limit = 10 # int | Size of the subset to retrieve. (optional) (default to 10)
offset = 0 # int | Number of items to skip during retrieval. (optional) (default to 0)
username = 'username_example' # str | User's username. (optional)
first_name = 'first_name_example' # str | User's first name. (optional)
last_name = 'last_name_example' # str | User's last name. (optional)
email = 'email_example' # str | User's email address. (optional)

try:
    # Search users
    api_response = api_instance.search_users(user_id, limit=limit, offset=offset, username=username, first_name=first_name, last_name=last_name, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Unique user identifier. | 
 **limit** | **int**| Size of the subset to retrieve. | [optional] [default to 10]
 **offset** | **int**| Number of items to skip during retrieval. | [optional] [default to 0]
 **username** | **str**| User&#x27;s username. | [optional] 
 **first_name** | **str**| User&#x27;s first name. | [optional] 
 **last_name** | **str**| User&#x27;s last name. | [optional] 
 **email** | **str**| User&#x27;s email address. | [optional] 

### Return type

[**UsersPage**](UsersPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_verification**
> send_verification()

Sends a verification email

Sends a verification email to the user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Sends a verification email
    api_instance.send_verification()
except ApiException as e:
    print("Exception when calling UsersApi->send_verification: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email**
> User update_email(body, user_id)

Updates email of the user.

Updates email of the user with provided ID. Email is updated using authorization token and the new received email. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Email() # Email | Email change data. User can change its email.
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Updates email of the user.
    api_response = api_instance.update_email(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Email**](Email.md)| Email change data. User can change its email. | 
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_picture**
> User update_profile_picture(body, user_id)

Updates the user's profile picture.

Updates the user's profile picture with provided ID. Profile picture is updated using authorization token and the new received picture. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserProfilePicture() # UserProfilePicture | JSON-formated document describing the profile picture of user to be update
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Updates the user's profile picture.
    api_response = api_instance.update_profile_picture(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_profile_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserProfilePicture**](UserProfilePicture.md)| JSON-formated document describing the profile picture of user to be update | 
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> User update_role(body, user_id)

Updates the user's role.

Updates role for the user with provided ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserRole() # UserRole | JSON-formated document describing the role of the user to be updated
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Updates the user's role.
    api_response = api_instance.update_role(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRole**](UserRole.md)| JSON-formated document describing the role of the user to be updated | 
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret**
> User update_secret(body)

Updates secret of currently logged in user.

Updates secret of currently logged in user. Secret is updated using authorization token and the new received info. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserSecret() # UserSecret | Secret change data. User can change its secret.

try:
    # Updates secret of currently logged in user.
    api_response = api_instance.update_secret(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSecret**](UserSecret.md)| Secret change data. User can change its secret. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tags**
> User update_tags(body, user_id)

Updates tags of the user.

Updates tags of the user with provided ID. Tags is updated using authorization token and the new tags received in request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserTags() # UserTags | JSON-formated document describing the tags of user to be update
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Updates tags of the user.
    api_response = api_instance.update_tags(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserTags**](UserTags.md)| JSON-formated document describing the tags of user to be update | 
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(body, user_id)

Updates first, last name and metadata of the user.

Updates name and metadata of the user with provided ID. Name and metadata is updated using authorization token and the new received info. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserUpdate() # UserUpdate | JSON-formated document describing the metadata and name of user to be update
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Updates first, last name and metadata of the user.
    api_response = api_instance.update_user(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdate**](UserUpdate.md)| JSON-formated document describing the metadata and name of user to be update | 
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_username**
> User update_username(body, user_id)

Updates user's username.

Updates username of the user with provided ID. Username is updated using authorization token and the new received username. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Username() # Username | JSON-formated document describing the username of the user to be updated
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Updates user's username.
    api_response = api_instance.update_username(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Username**](Username.md)| JSON-formated document describing the username of the user to be updated | 
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Delete a user

Delete a specific user that is identifier by the user ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique user identifier.

try:
    # Delete a user
    api_instance.users_user_id_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Unique user identifier. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email**
> verify_email(token)

Verify user's email

Verify user's email using the token from the verification link. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | Verification token.

try:
    # Verify user's email
    api_instance.verify_email(token)
except ApiException as e:
    print("Exception when calling UsersApi->verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Verification token. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth), [refreshAuth](../README.md#refreshAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


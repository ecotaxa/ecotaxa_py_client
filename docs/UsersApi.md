# ecotaxa_cli_py.UsersApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user_prefs_users_my_preferences_project_id_get**](UsersApi.md#get_current_user_prefs_users_my_preferences_project_id_get) | **GET** /users/my_preferences/{project_id} | Get Current User Prefs
[**get_user_users_user_id_get**](UsersApi.md#get_user_users_user_id_get) | **GET** /users/{user_id} | Get User
[**get_users_users_get**](UsersApi.md#get_users_users_get) | **GET** /users | Get Users
[**search_user_users_search_get**](UsersApi.md#search_user_users_search_get) | **GET** /users/search | Search User
[**set_current_user_prefs_users_my_preferences_project_id_put**](UsersApi.md#set_current_user_prefs_users_my_preferences_project_id_put) | **PUT** /users/my_preferences/{project_id} | Set Current User Prefs
[**show_current_user_users_me_get**](UsersApi.md#show_current_user_users_me_get) | **GET** /users/me | Show Current User


# **get_current_user_prefs_users_my_preferences_project_id_get**
> str get_current_user_prefs_users_my_preferences_project_id_get(project_id)

Get Current User Prefs

**Returns one preference**, for a project and the currently authenticated user.  Available keys are **cwd**, **img_import** and **filters**.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import users_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    project_id = 1 # int | 
    key = "filters" # str | The preference key. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Current User Prefs
        api_response = api_instance.get_current_user_prefs_users_my_preferences_project_id_get(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->get_current_user_prefs_users_my_preferences_project_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Current User Prefs
        api_response = api_instance.get_current_user_prefs_users_my_preferences_project_id_get(project_id, key=key)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->get_current_user_prefs_users_my_preferences_project_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **key** | **str**| The preference key. | [optional]

### Return type

**str**

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_users_user_id_get**
> UserModel get_user_users_user_id_get(user_id)

Get User

Returns **information about the user** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import users_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get User
        api_response = api_instance.get_user_users_user_id_get(user_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->get_user_users_user_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |

### Return type

[**UserModel**](UserModel.md)

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_users_get**
> [UserModel] get_users_users_get()

Get Users

Returns the list of **all users** with their information.   🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import users_api
from ecotaxa_cli_py.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Users
        api_response = api_instance.get_users_users_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->get_users_users_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserModel]**](UserModel.md)

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_users_search_get**
> [UserModel] search_user_users_search_get()

Search User

**Search users using various criteria**, search is case insensitive and might contain % chars.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import users_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    by_name = "%userNa%" # str | Search by name, use % for searching with 'any char'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search User
        api_response = api_instance.search_user_users_search_get(by_name=by_name)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->search_user_users_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by_name** | **str**| Search by name, use % for searching with &#39;any char&#39;. | [optional]

### Return type

[**[UserModel]**](UserModel.md)

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_current_user_prefs_users_my_preferences_project_id_put**
> bool, date, datetime, dict, float, int, list, str, none_type set_current_user_prefs_users_my_preferences_project_id_put(project_id)

Set Current User Prefs

**Sets one preference**, for a project and for the currently authenticated user.  Available keys are **cwd**, **img_import** and **filters**.  The key disappears if set to empty string.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import users_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    project_id = 1 # int | 
    key = "filters" # str | The preference key. (optional)
    value = "{"dispfield": " dispfield_orig_id dispfield_classif_auto_score dispfield_classif_when dispfield_random_value", "ipp": "500", "magenabled": "1", "popupenabled": "1", "sortby": "orig_id", "sortorder": "asc", "statusfilter": "", "zoom": "90"}" # str | The value to set this preference to. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set Current User Prefs
        api_response = api_instance.set_current_user_prefs_users_my_preferences_project_id_put(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->set_current_user_prefs_users_my_preferences_project_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set Current User Prefs
        api_response = api_instance.set_current_user_prefs_users_my_preferences_project_id_put(project_id, key=key, value=value)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->set_current_user_prefs_users_my_preferences_project_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **key** | **str**| The preference key. | [optional]
 **value** | **str**| The value to set this preference to. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_current_user_users_me_get**
> UserModelWithRights show_current_user_users_me_get()

Show Current User

Returns **currently authenticated user's** information, permissions and last used projects.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import users_api
from ecotaxa_cli_py.model.user_model_with_rights import UserModelWithRights
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Show Current User
        api_response = api_instance.show_current_user_users_me_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling UsersApi->show_current_user_users_me_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserModelWithRights**](UserModelWithRights.md)

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


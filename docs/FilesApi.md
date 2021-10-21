# ecotaxa_py_client.FilesApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_common_files_common_files_get**](FilesApi.md#list_common_files_common_files_get) | **GET** /common_files/ | List Common Files
[**list_user_files_my_files_sub_path_get**](FilesApi.md#list_user_files_my_files_sub_path_get) | **GET** /my_files/{sub_path} | List User Files
[**put_user_file_my_files_post**](FilesApi.md#put_user_file_my_files_post) | **POST** /my_files/ | Put User File


# **list_common_files_common_files_get**
> DirectoryModel list_common_files_common_files_get(path)

List Common Files

List the common files which are usable for some file-related operations e.g. import.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import files_api
from ecotaxa_py_client.model.directory_model import DirectoryModel
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    path = "path_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List Common Files
        api_response = api_instance.list_common_files_common_files_get(path)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling FilesApi->list_common_files_common_files_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

[**DirectoryModel**](DirectoryModel.md)

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

# **list_user_files_my_files_sub_path_get**
> DirectoryModel list_user_files_my_files_sub_path_get(sub_path)

List User Files

List the private files which are usable for some file-related operations e.g. import.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import files_api
from ecotaxa_py_client.model.directory_model import DirectoryModel
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    sub_path = "sub_path_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List User Files
        api_response = api_instance.list_user_files_my_files_sub_path_get(sub_path)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling FilesApi->list_user_files_my_files_sub_path_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_path** | **str**|  |

### Return type

[**DirectoryModel**](DirectoryModel.md)

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

# **put_user_file_my_files_post**
> str put_user_file_my_files_post(file)

Put User File

Upload a file for the current user. The returned text will contain a serve-side path which is usable for some file-related operations e.g. import.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import files_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | 
    path = "path_example" # str |  (optional)
    tag = "tag_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Put User File
        api_response = api_instance.put_user_file_my_files_post(file)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling FilesApi->put_user_file_my_files_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Put User File
        api_response = api_instance.put_user_file_my_files_post(file, path=path, tag=tag)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling FilesApi->put_user_file_my_files_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  |
 **path** | **str**|  | [optional]
 **tag** | **str**|  | [optional]

### Return type

**str**

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


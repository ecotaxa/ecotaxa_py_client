# ecotaxa_py_client.FilesApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_common_files**](FilesApi.md#list_common_files) | **GET** /common_files/ | List Common Files
[**list_user_files**](FilesApi.md#list_user_files) | **GET** /my_files/{sub_path} | List User Files
[**post_user_file**](FilesApi.md#post_user_file) | **POST** /my_files/ | Put User File


# **list_common_files**
> DirectoryModel list_common_files(path)

List Common Files

**List the common files** which are usable for some file-related operations.  *e.g. import.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.directory_model import DirectoryModel
from ecotaxa_py_client.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_py_client.FilesApi(api_client)
    path = '/ftp_plankton/Ecotaxa_Exported_data' # str | 

    try:
        # List Common Files
        api_response = api_instance.list_common_files(path)
        print("The response of FilesApi->list_common_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->list_common_files: %s\n" % e)
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

# **list_user_files**
> DirectoryModel list_user_files(sub_path)

List User Files

**List the private files** which are usable for some file-related operations. A sub_path starting with \"/\" is considered relative to user folder.  *e.g. import.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.directory_model import DirectoryModel
from ecotaxa_py_client.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_py_client.FilesApi(api_client)
    sub_path = 'sub_path_example' # str | 

    try:
        # List User Files
        api_response = api_instance.list_user_files(sub_path)
        print("The response of FilesApi->list_user_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->list_user_files: %s\n" % e)
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

# **post_user_file**
> str post_user_file(file, path=path, tag=tag)

Put User File

**Upload a file for the current user.**  The returned text will contain a server-side path which is usable for some file-related operations.  *e.g. import.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_py_client.FilesApi(api_client)
    file = None # bytearray | 
    path = 'path_example' # str | The client-side full path of the file. (optional)
    tag = 'tag_example' # str | If a tag is provided, then all files with the same tag are grouped (in a sub-directory). Otherwise, a temp directory with only this file will be created. (optional)

    try:
        # Put User File
        api_response = api_instance.post_user_file(file, path=path, tag=tag)
        print("The response of FilesApi->post_user_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->post_user_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **path** | **str**| The client-side full path of the file. | [optional] 
 **tag** | **str**| If a tag is provided, then all files with the same tag are grouped (in a sub-directory). Otherwise, a temp directory with only this file will be created. | [optional] 

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


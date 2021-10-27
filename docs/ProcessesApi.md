# ecotaxa_py_client.ProcessesApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_query_process_process_id_get**](ProcessesApi.md#process_query_process_process_id_get) | **GET** /process/{process_id} | Process Query
[**update_processes_process_set_update_post**](ProcessesApi.md#update_processes_process_set_update_post) | **POST** /process_set/update | Update Processes


# **process_query_process_process_id_get**
> ProcessModel process_query_process_process_id_get(process_id)

Process Query

Returns **information about the process** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import processes_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.process_model import ProcessModel
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
    api_instance = processes_api.ProcessesApi(api_client)
    process_id = 1 # int | Internal, the unique numeric id of this process.

    # example passing only required values which don't have defaults set
    try:
        # Process Query
        api_response = api_instance.process_query_process_process_id_get(process_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling ProcessesApi->process_query_process_process_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **int**| Internal, the unique numeric id of this process. |

### Return type

[**ProcessModel**](ProcessModel.md)

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

# **update_processes_process_set_update_post**
> int update_processes_process_set_update_post(bulk_update_req)

Update Processes

Do the required **update for each process in the set.**  **Returns the number of updated entities.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import processes_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.bulk_update_req import BulkUpdateReq
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
    api_instance = processes_api.ProcessesApi(api_client)
    bulk_update_req = BulkUpdateReq(
        target_ids=[1,5,290],
        updates=[{"ucol":"sub_part","uval":"2"}],
    ) # BulkUpdateReq | 

    # example passing only required values which don't have defaults set
    try:
        # Update Processes
        api_response = api_instance.update_processes_process_set_update_post(bulk_update_req)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling ProcessesApi->update_processes_process_set_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_update_req** | [**BulkUpdateReq**](BulkUpdateReq.md)|  |

### Return type

**int**

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


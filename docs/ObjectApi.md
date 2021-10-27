# ecotaxa_py_client.ObjectApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**object_query_history_object_object_id_history_get**](ObjectApi.md#object_query_history_object_object_id_history_get) | **GET** /object/{object_id}/history | Object Query History
[**object_query_object_object_id_get**](ObjectApi.md#object_query_object_object_id_get) | **GET** /object/{object_id} | Object Query


# **object_query_history_object_object_id_history_get**
> [HistoricalClassification] object_query_history_object_object_id_history_get(object_id)

Object Query History

Returns **information about the object's history** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import object_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.historical_classification import HistoricalClassification
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
    api_instance = object_api.ObjectApi(api_client)
    object_id = 1 # int | Internal, the unique numeric id of this object.

    # example passing only required values which don't have defaults set
    try:
        # Object Query History
        api_response = api_instance.object_query_history_object_object_id_history_get(object_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling ObjectApi->object_query_history_object_object_id_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **int**| Internal, the unique numeric id of this object. |

### Return type

[**[HistoricalClassification]**](HistoricalClassification.md)

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

# **object_query_object_object_id_get**
> ObjectModel object_query_object_object_id_get(object_id)

Object Query

Returns **information about the object** corresponding to the given id.   🔒 Anonymous reader can do if the project has the right rights :)

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import object_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.object_model import ObjectModel
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
    api_instance = object_api.ObjectApi(api_client)
    object_id = 1 # int | Internal, the unique numeric id of this object.

    # example passing only required values which don't have defaults set
    try:
        # Object Query
        api_response = api_instance.object_query_object_object_id_get(object_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling ObjectApi->object_query_object_object_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **int**| Internal, the unique numeric id of this object. |

### Return type

[**ObjectModel**](ObjectModel.md)

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


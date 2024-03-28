# ecotaxa_py_client.MiscApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_nothing**](MiscApi.md#do_nothing) | **GET** /noop | Do Nothing
[**query_ml_models**](MiscApi.md#query_ml_models) | **GET** /ml_models | Query Ml Models
[**system_error**](MiscApi.md#system_error) | **GET** /error | System Error
[**used_constants**](MiscApi.md#used_constants) | **GET** /constants | Used Constants


# **do_nothing**
> ResponseDoNothingNoopGet do_nothing()

Do Nothing

**This entry point will just do nothing.**  It's also used for exporting models we need on client side.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.response_do_nothing_noop_get import ResponseDoNothingNoopGet
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
    api_instance = ecotaxa_py_client.MiscApi(api_client)

    try:
        # Do Nothing
        api_response = api_instance.do_nothing()
        print("The response of MiscApi->do_nothing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscApi->do_nothing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseDoNothingNoopGet**](ResponseDoNothingNoopGet.md)

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

# **query_ml_models**
> List[MLModel] query_ml_models()

Query Ml Models

**Return the list of machine learning models, which can be used for extracting image features.**

### Example


```python
import ecotaxa_py_client
from ecotaxa_py_client.models.ml_model import MLModel
from ecotaxa_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_py_client.MiscApi(api_client)

    try:
        # Query Ml Models
        api_response = api_instance.query_ml_models()
        print("The response of MiscApi->query_ml_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscApi->query_ml_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MLModel]**](MLModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_error**
> object system_error()

System Error

**Return a 500 internal error**, on purpose so the stack trace is visible and client can see what it gives.

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
    api_instance = ecotaxa_py_client.MiscApi(api_client)

    try:
        # System Error
        api_response = api_instance.system_error()
        print("The response of MiscApi->system_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscApi->system_error: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **used_constants**
> Constants used_constants()

Used Constants

**Return useful strings for user dialog.**  Now also used for values extracted from Config.

### Example


```python
import ecotaxa_py_client
from ecotaxa_py_client.models.constants import Constants
from ecotaxa_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_py_client.MiscApi(api_client)

    try:
        # Used Constants
        api_response = api_instance.used_constants()
        print("The response of MiscApi->used_constants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscApi->used_constants: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Constants**](Constants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


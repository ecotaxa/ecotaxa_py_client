# ecotaxa_cli_py.MiscApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_nothing_noop_get**](MiscApi.md#do_nothing_noop_get) | **GET** /noop | Do Nothing
[**system_error_error_get**](MiscApi.md#system_error_error_get) | **GET** /error | System Error
[**used_constants_constants_get**](MiscApi.md#used_constants_constants_get) | **GET** /constants | Used Constants


# **do_nothing_noop_get**
> dict do_nothing_noop_get()

Do Nothing

This entry point will just do nothing.     It's also used for exporting models we need on client side.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import misc_api
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
    api_instance = misc_api.MiscApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Do Nothing
        api_response = api_instance.do_nothing_noop_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling MiscApi->do_nothing_noop_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**dict**

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

# **system_error_error_get**
> bool, date, datetime, dict, float, int, list, str, none_type system_error_error_get()

System Error

This entry point will return a 500 internal error, on purpose so the stack trace is visible and client can see what it gives.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import misc_api
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
    api_instance = misc_api.MiscApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # System Error
        api_response = api_instance.system_error_error_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling MiscApi->system_error_error_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **used_constants_constants_get**
> Constants used_constants_constants_get()

Used Constants

This entry point will return useful strings for user dialog. Now also used for values extracted from Config.

### Example


```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import misc_api
from ecotaxa_cli_py.model.constants import Constants
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = misc_api.MiscApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Used Constants
        api_response = api_instance.used_constants_constants_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling MiscApi->used_constants_constants_get: %s\n" % e)
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


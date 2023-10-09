# ecotaxa_py_client.WIPApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

| Method                                       | HTTP request    | Description   |
| -------------------------------------------- | --------------- | ------------- |
| [**system_status**](WIPApi.md#system_status) | **GET** /status | System Status |


# **system_status**
> bool, date, datetime, dict, float, int, list, str, none_type system_status()

System Status

**Report the status**, mainly used for verifying that the server is up. Depending on provided credentials, you get more or less information.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import wip_api
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
    api_instance = wip_api.WIPApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # System Status
        api_response = api_instance.system_status()
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling WIPApi->system_status: %s\n" % e)
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

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


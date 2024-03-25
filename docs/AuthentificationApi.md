# ecotaxa_py_client.AuthentificationApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthentificationApi.md#login) | **POST** /login | Login


# **login**
> str login(login_req)

Login

**Login barrier,**  If successful, the login will returns a **JWT** which will have to be used in bearer authentication scheme for subsequent calls.

### Example


```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import authentification_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.login_req import LoginReq
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentification_api.AuthentificationApi(api_client)
    login_req = LoginReq(
        password="test!",
        username="ecotaxa.api.user@gmail.com",
    ) # LoginReq | 

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login(login_req)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling AuthentificationApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_req** | [**LoginReq**](LoginReq.md)|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


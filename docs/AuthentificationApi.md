# ecotaxa_py_client.AuthentificationApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

| Method                                    | HTTP request    | Description |
| ----------------------------------------- | --------------- | ----------- |
| [**login**](AuthentificationApi.md#login) | **POST** /login | Login       |


# **login**
> str login(login_req)

Login

**Login barrier,**  If successful, the login will returns a **JWT** which will have to be used in bearer authentication scheme for subsequent calls.

### Example


```python
import ecotaxa_py_client
from ecotaxa_py_client.models.login_req import LoginReq
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
    api_instance = ecotaxa_py_client.AuthentificationApi(api_client)
    login_req = ecotaxa_py_client.LoginReq(
            password="test!",
            username="ecotaxa.api.user@gmail.com",
        ) # LoginReq | 

    try:
        # Login
        api_response = api_instance.login(login_req)
        os.environ["ACCESS_TOKEN"]=api_response
        print("The response of AuthentificationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthentificationApi->login: %s\n" % e)
```



### Parameters


| Name          | Type                        | Description | Notes |
| ------------- | --------------------------- | ----------- | ----- |
| **login_req** | [**LoginReq**](LoginReq.md) |             |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


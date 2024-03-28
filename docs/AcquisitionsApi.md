# ecotaxa_py_client.AcquisitionsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquisition_query**](AcquisitionsApi.md#acquisition_query) | **GET** /acquisition/{acquisition_id} | Acquisition Query
[**acquisitions_search**](AcquisitionsApi.md#acquisitions_search) | **GET** /acquisitions/search | Acquisitions Search
[**update_acquisitions**](AcquisitionsApi.md#update_acquisitions) | **POST** /acquisition_set/update | Update Acquisitions


# **acquisition_query**
> AcquisitionModel acquisition_query(acquisition_id)

Acquisition Query

Returns **information about the acquisition** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.acquisition_model import AcquisitionModel
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
    api_instance = ecotaxa_py_client.AcquisitionsApi(api_client)
    acquisition_id = 1 # int | Internal, the unique numeric id of this acquisition.

    try:
        # Acquisition Query
        api_response = api_instance.acquisition_query(acquisition_id)
        print("The response of AcquisitionsApi->acquisition_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcquisitionsApi->acquisition_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acquisition_id** | **int**| Internal, the unique numeric id of this acquisition. | 

### Return type

[**AcquisitionModel**](AcquisitionModel.md)

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

# **acquisitions_search**
> List[AcquisitionModel] acquisitions_search(project_id)

Acquisitions Search

Returns the **list of all acquisitions for a given project**.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.acquisition_model import AcquisitionModel
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
    api_instance = ecotaxa_py_client.AcquisitionsApi(api_client)
    project_id = 1 # int | The project id.

    try:
        # Acquisitions Search
        api_response = api_instance.acquisitions_search(project_id)
        print("The response of AcquisitionsApi->acquisitions_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcquisitionsApi->acquisitions_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project id. | 

### Return type

[**List[AcquisitionModel]**](AcquisitionModel.md)

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

# **update_acquisitions**
> int update_acquisitions(bulk_update_req)

Update Acquisitions

Do the required **update for each acquisition in the set**.  **Return the number of updated entities.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.bulk_update_req import BulkUpdateReq
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
    api_instance = ecotaxa_py_client.AcquisitionsApi(api_client)
    bulk_update_req = ecotaxa_py_client.BulkUpdateReq() # BulkUpdateReq | 

    try:
        # Update Acquisitions
        api_response = api_instance.update_acquisitions(bulk_update_req)
        print("The response of AcquisitionsApi->update_acquisitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcquisitionsApi->update_acquisitions: %s\n" % e)
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


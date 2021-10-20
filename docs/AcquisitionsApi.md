# ecotaxa_cli_py.AcquisitionsApi

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
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import acquisitions_api
from ecotaxa_cli_py.model.acquisition_model import AcquisitionModel
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
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
    api_instance = acquisitions_api.AcquisitionsApi(api_client)
    acquisition_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Acquisition Query
        api_response = api_instance.acquisition_query(acquisition_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling AcquisitionsApi->acquisition_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acquisition_id** | **int**|  |

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
> [AcquisitionModel] acquisitions_search()

Acquisitions Search

Returns the **list of all acquisitions for a given project**.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import acquisitions_api
from ecotaxa_cli_py.model.acquisition_model import AcquisitionModel
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
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
    api_instance = acquisitions_api.AcquisitionsApi(api_client)
    project_id = 1 # int | The project id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Acquisitions Search
        api_response = api_instance.acquisitions_search(project_id=project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling AcquisitionsApi->acquisitions_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project id | [optional]

### Return type

[**[AcquisitionModel]**](AcquisitionModel.md)

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

Do the required **update for each acquisition in the set**.  Return the number of updated entities.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import acquisitions_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.bulk_update_req import BulkUpdateReq
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
    api_instance = acquisitions_api.AcquisitionsApi(api_client)
    bulk_update_req = BulkUpdateReq(
        target_ids=[1,5,290],
        updates=[{"ucol":"sub_part","uval":"2"}],
    ) # BulkUpdateReq | 

    # example passing only required values which don't have defaults set
    try:
        # Update Acquisitions
        api_response = api_instance.update_acquisitions(bulk_update_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
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


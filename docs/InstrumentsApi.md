# ecotaxa_py_client.InstrumentsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instrument_query**](InstrumentsApi.md#instrument_query) | **GET** /instruments/ | Instrument Query


# **instrument_query**
> List[str] instrument_query(project_ids)

Instrument Query

Returns the list of instruments, inside specific project(s) or globally.

### Example


```python
import ecotaxa_py_client
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
    api_instance = ecotaxa_py_client.InstrumentsApi(api_client)
    project_ids = '1,2,3' # str | String containing the list of one or more project ids, separated by non-num char, or 'all' for all instruments.

    try:
        # Instrument Query
        api_response = api_instance.instrument_query(project_ids)
        print("The response of InstrumentsApi->instrument_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->instrument_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| String containing the list of one or more project ids, separated by non-num char, or &#39;all&#39; for all instruments. | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


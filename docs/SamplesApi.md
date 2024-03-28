# ecotaxa_py_client.SamplesApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sample_query**](SamplesApi.md#sample_query) | **GET** /sample/{sample_id} | Sample Query
[**sample_set_get_stats**](SamplesApi.md#sample_set_get_stats) | **GET** /sample_set/taxo_stats | Sample Set Get Stats
[**samples_search**](SamplesApi.md#samples_search) | **GET** /samples/search | Samples Search
[**update_samples**](SamplesApi.md#update_samples) | **POST** /sample_set/update | Update Samples


# **sample_query**
> SampleModel sample_query(sample_id)

Sample Query

Returns **information about the sample** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.sample_model import SampleModel
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
    api_instance = ecotaxa_py_client.SamplesApi(api_client)
    sample_id = 1 # int | Internal, the unique numeric id of this sample.

    try:
        # Sample Query
        api_response = api_instance.sample_query(sample_id)
        print("The response of SamplesApi->sample_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SamplesApi->sample_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**| Internal, the unique numeric id of this sample. | 

### Return type

[**SampleModel**](SampleModel.md)

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

# **sample_set_get_stats**
> List[SampleTaxoStatsModel] sample_set_get_stats(sample_ids)

Sample Set Get Stats

Returns **classification statistics** for each sample of the given list. One block of stats is returned for each input ID.  EXPECT A SLOW RESPONSE : No cache of such information anywhere.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.sample_taxo_stats_model import SampleTaxoStatsModel
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
    api_instance = ecotaxa_py_client.SamplesApi(api_client)
    sample_ids = '15,5' # str | String containing the list of one or more sample ids separated by non-num char.

    try:
        # Sample Set Get Stats
        api_response = api_instance.sample_set_get_stats(sample_ids)
        print("The response of SamplesApi->sample_set_get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SamplesApi->sample_set_get_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_ids** | **str**| String containing the list of one or more sample ids separated by non-num char. | 

### Return type

[**List[SampleTaxoStatsModel]**](SampleTaxoStatsModel.md)

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

# **samples_search**
> List[SampleModel] samples_search(project_ids, id_pattern)

Samples Search

**Search for samples.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.sample_model import SampleModel
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
    api_instance = ecotaxa_py_client.SamplesApi(api_client)
    project_ids = '1,55' # str | String containing the list of one or more project id separated by non-num char.
    id_pattern = '*' # str | Sample id textual pattern. Use * or '' for 'any matches'. Match is case-insensitive.

    try:
        # Samples Search
        api_response = api_instance.samples_search(project_ids, id_pattern)
        print("The response of SamplesApi->samples_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SamplesApi->samples_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| String containing the list of one or more project id separated by non-num char. | 
 **id_pattern** | **str**| Sample id textual pattern. Use * or &#39;&#39; for &#39;any matches&#39;. Match is case-insensitive. | 

### Return type

[**List[SampleModel]**](SampleModel.md)

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

# **update_samples**
> int update_samples(bulk_update_req)

Update Samples

Do the required **update for each sample in the set.**  Any non-null field in the model is written to every impacted sample.  **Returns the number of updated entities.**

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
    api_instance = ecotaxa_py_client.SamplesApi(api_client)
    bulk_update_req = ecotaxa_py_client.BulkUpdateReq() # BulkUpdateReq | 

    try:
        # Update Samples
        api_response = api_instance.update_samples(bulk_update_req)
        print("The response of SamplesApi->update_samples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SamplesApi->update_samples: %s\n" % e)
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


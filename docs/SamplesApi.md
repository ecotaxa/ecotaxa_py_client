# ecotaxa_cli_py.SamplesApi

All URIs are relative to *https://raw.githubusercontent.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sample_query_sample_sample_id_get**](SamplesApi.md#sample_query_sample_sample_id_get) | **GET** /sample/{sample_id} | Sample Query
[**sample_set_get_stats_sample_set_taxo_stats_get**](SamplesApi.md#sample_set_get_stats_sample_set_taxo_stats_get) | **GET** /sample_set/taxo_stats | Sample Set Get Stats
[**samples_search_samples_search_get**](SamplesApi.md#samples_search_samples_search_get) | **GET** /samples/search | Samples Search
[**update_samples_sample_set_update_post**](SamplesApi.md#update_samples_sample_set_update_post) | **POST** /sample_set/update | Update Samples


# **sample_query_sample_sample_id_get**
> SampleModel sample_query_sample_sample_id_get(sample_id)

Sample Query

Returns **information about the sample** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import samples_api
from ecotaxa_cli_py.model.sample_model import SampleModel
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_id = 1 # int | Internal, the unique numeric id of this sample.

    # example passing only required values which don't have defaults set
    try:
        # Sample Query
        api_response = api_instance.sample_query_sample_sample_id_get(sample_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling SamplesApi->sample_query_sample_sample_id_get: %s\n" % e)
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

# **sample_set_get_stats_sample_set_taxo_stats_get**
> [SampleTaxoStatsModel] sample_set_get_stats_sample_set_taxo_stats_get(sample_ids)

Sample Set Get Stats

Returns **classification statistics** for the given set of samples.  EXPECT A SLOW RESPONSE : No cache of such information anywhere.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import samples_api
from ecotaxa_cli_py.model.sample_taxo_stats_model import SampleTaxoStatsModel
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    sample_ids = "15,5" # str | String containing the list of one or more sample ids separated by non-num char.

    # example passing only required values which don't have defaults set
    try:
        # Sample Set Get Stats
        api_response = api_instance.sample_set_get_stats_sample_set_taxo_stats_get(sample_ids)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling SamplesApi->sample_set_get_stats_sample_set_taxo_stats_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_ids** | **str**| String containing the list of one or more sample ids separated by non-num char. |

### Return type

[**[SampleTaxoStatsModel]**](SampleTaxoStatsModel.md)

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

# **samples_search_samples_search_get**
> [SampleModel] samples_search_samples_search_get(project_ids, id_pattern)

Samples Search

**Search for samples.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import samples_api
from ecotaxa_cli_py.model.sample_model import SampleModel
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    project_ids = "1,55" # str | String containing the list of one or more project id separated by non-num char.
    id_pattern = "*" # str | Sample id textual pattern. Use * or '' for 'any matches'. Match is case-insensitive.

    # example passing only required values which don't have defaults set
    try:
        # Samples Search
        api_response = api_instance.samples_search_samples_search_get(project_ids, id_pattern)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling SamplesApi->samples_search_samples_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| String containing the list of one or more project id separated by non-num char. |
 **id_pattern** | **str**| Sample id textual pattern. Use * or &#39;&#39; for &#39;any matches&#39;. Match is case-insensitive. |

### Return type

[**[SampleModel]**](SampleModel.md)

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

# **update_samples_sample_set_update_post**
> int update_samples_sample_set_update_post(bulk_update_req)

Update Samples

Do the required **update for each sample in the set.**   Any non-null field in the model is written to every impacted sample.  **Returns the number of updated entities.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import samples_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.bulk_update_req import BulkUpdateReq
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samples_api.SamplesApi(api_client)
    bulk_update_req = BulkUpdateReq(
        target_ids=[1,5,290],
        updates=[{"ucol":"sub_part","uval":"2"}],
    ) # BulkUpdateReq | 

    # example passing only required values which don't have defaults set
    try:
        # Update Samples
        api_response = api_instance.update_samples_sample_set_update_post(bulk_update_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling SamplesApi->update_samples_sample_set_update_post: %s\n" % e)
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


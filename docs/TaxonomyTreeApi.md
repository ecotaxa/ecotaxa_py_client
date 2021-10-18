# ecotaxa_cli_py.TaxonomyTreeApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_taxon_in_central_taxon_central_put**](TaxonomyTreeApi.md#add_taxon_in_central_taxon_central_put) | **PUT** /taxon/central | Add Taxon In Central
[**get_taxon_in_central_taxon_central_taxon_id_get**](TaxonomyTreeApi.md#get_taxon_in_central_taxon_central_taxon_id_get) | **GET** /taxon/central/{taxon_id} | Get Taxon In Central
[**pull_taxa_update_from_central_taxa_pull_from_central_get**](TaxonomyTreeApi.md#pull_taxa_update_from_central_taxa_pull_from_central_get) | **GET** /taxa/pull_from_central | Pull Taxa Update From Central
[**push_taxa_stats_in_central_taxa_stats_push_to_central_get**](TaxonomyTreeApi.md#push_taxa_stats_in_central_taxa_stats_push_to_central_get) | **GET** /taxa/stats/push_to_central | Push Taxa Stats In Central
[**query_root_taxa_taxa_get**](TaxonomyTreeApi.md#query_root_taxa_taxa_get) | **GET** /taxa | Query Root Taxa
[**query_taxa_set_taxon_set_query_get**](TaxonomyTreeApi.md#query_taxa_set_taxon_set_query_get) | **GET** /taxon_set/query | Query Taxa Set
[**query_taxa_taxon_taxon_id_get**](TaxonomyTreeApi.md#query_taxa_taxon_taxon_id_get) | **GET** /taxon/{taxon_id} | Query Taxa
[**query_taxa_usage_taxon_taxon_id_usage_get**](TaxonomyTreeApi.md#query_taxa_usage_taxon_taxon_id_usage_get) | **GET** /taxon/{taxon_id}/usage | Query Taxa Usage
[**reclassif_project_stats_taxa_reclassification_history_project_id_get**](TaxonomyTreeApi.md#reclassif_project_stats_taxa_reclassification_history_project_id_get) | **GET** /taxa/reclassification_history/{project_id} | Reclassif Project Stats
[**reclassif_stats_taxa_reclassification_stats_get**](TaxonomyTreeApi.md#reclassif_stats_taxa_reclassification_stats_get) | **GET** /taxa/reclassification_stats | Reclassif Stats
[**search_taxa_taxon_set_search_get**](TaxonomyTreeApi.md#search_taxa_taxon_set_search_get) | **GET** /taxon_set/search | Search Taxa
[**taxa_tree_status_taxa_status_get**](TaxonomyTreeApi.md#taxa_tree_status_taxa_status_get) | **GET** /taxa/status | Taxa Tree Status


# **add_taxon_in_central_taxon_central_put**
> bool, date, datetime, dict, float, int, list, str, none_type add_taxon_in_central_taxon_central_put(name, parent_id, taxotype, creator_email)

Add Taxon In Central

Create a taxon on EcoTaxoServer. Logged user must be manager (on any project) or application admin.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    name = "name_example" # str | 
    parent_id = 1 # int | 
    taxotype = "taxotype_example" # str | 
    creator_email = "creator_email_example" # str | 
    source_desc = "source_desc_example" # str |  (optional)
    source_url = "source_url_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Taxon In Central
        api_response = api_instance.add_taxon_in_central_taxon_central_put(name, parent_id, taxotype, creator_email)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->add_taxon_in_central_taxon_central_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Taxon In Central
        api_response = api_instance.add_taxon_in_central_taxon_central_put(name, parent_id, taxotype, creator_email, source_desc=source_desc, source_url=source_url)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->add_taxon_in_central_taxon_central_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **parent_id** | **int**|  |
 **taxotype** | **str**|  |
 **creator_email** | **str**|  |
 **source_desc** | **str**|  | [optional]
 **source_url** | **str**|  | [optional]

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxon_in_central_taxon_central_taxon_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_taxon_in_central_taxon_central_taxon_id_get(taxon_id)

Get Taxon In Central

Get EcoTaxoServer full record for this taxon.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    taxon_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Taxon In Central
        api_response = api_instance.get_taxon_in_central_taxon_central_taxon_id_get(taxon_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->get_taxon_in_central_taxon_central_taxon_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_id** | **int**|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_taxa_update_from_central_taxa_pull_from_central_get**
> bool, date, datetime, dict, float, int, list, str, none_type pull_taxa_update_from_central_taxa_pull_from_central_get()

Pull Taxa Update From Central

Get what changed in EcoTaxoServer managed tree and update local tree accordingly.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Pull Taxa Update From Central
        api_response = api_instance.pull_taxa_update_from_central_taxa_pull_from_central_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->pull_taxa_update_from_central_taxa_pull_from_central_get: %s\n" % e)
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

# **push_taxa_stats_in_central_taxa_stats_push_to_central_get**
> bool, date, datetime, dict, float, int, list, str, none_type push_taxa_stats_in_central_taxa_stats_push_to_central_get()

Push Taxa Stats In Central

Push present instance stats into EcoTaxoServer.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Push Taxa Stats In Central
        api_response = api_instance.push_taxa_stats_in_central_taxa_stats_push_to_central_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->push_taxa_stats_in_central_taxa_stats_push_to_central_get: %s\n" % e)
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

# **query_root_taxa_taxa_get**
> [TaxonModel] query_root_taxa_taxa_get()

Query Root Taxa

Return all taxa with no parent.

### Example


```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
from ecotaxa_cli_py.model.taxon_model import TaxonModel
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Query Root Taxa
        api_response = api_instance.query_root_taxa_taxa_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->query_root_taxa_taxa_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[TaxonModel]**](TaxonModel.md)

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

# **query_taxa_set_taxon_set_query_get**
> [TaxonModel] query_taxa_set_taxon_set_query_get(ids)

Query Taxa Set

Information about several taxa, including their lineage. The separator between numbers is arbitrary non-digit, e.g. \":\", \"|\" or \",\"

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
from ecotaxa_cli_py.model.taxon_model import TaxonModel
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    ids = "ids_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Query Taxa Set
        api_response = api_instance.query_taxa_set_taxon_set_query_get(ids)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->query_taxa_set_taxon_set_query_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  |

### Return type

[**[TaxonModel]**](TaxonModel.md)

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

# **query_taxa_taxon_taxon_id_get**
> TaxonModel query_taxa_taxon_taxon_id_get(taxon_id)

Query Taxa

Information about a single taxon, including its lineage.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
from ecotaxa_cli_py.model.taxon_model import TaxonModel
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    taxon_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Query Taxa
        api_response = api_instance.query_taxa_taxon_taxon_id_get(taxon_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->query_taxa_taxon_taxon_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_id** | **int**|  |

### Return type

[**TaxonModel**](TaxonModel.md)

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

# **query_taxa_usage_taxon_taxon_id_usage_get**
> [TaxonUsageModel] query_taxa_usage_taxon_taxon_id_usage_get(taxon_id)

Query Taxa Usage

Where a given taxon is used. Only validated uses are returned.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
from ecotaxa_cli_py.model.taxon_usage_model import TaxonUsageModel
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    taxon_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Query Taxa Usage
        api_response = api_instance.query_taxa_usage_taxon_taxon_id_usage_get(taxon_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->query_taxa_usage_taxon_taxon_id_usage_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_id** | **int**|  |

### Return type

[**[TaxonUsageModel]**](TaxonUsageModel.md)

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

# **reclassif_project_stats_taxa_reclassification_history_project_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type reclassif_project_stats_taxa_reclassification_history_project_id_get(project_id)

Reclassif Project Stats

Dig into reclassification logs and return the associations source->target for previous reclassifications.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    project_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Reclassif Project Stats
        api_response = api_instance.reclassif_project_stats_taxa_reclassification_history_project_id_get(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->reclassif_project_stats_taxa_reclassification_history_project_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reclassif_stats_taxa_reclassification_stats_get**
> [TaxonModel] reclassif_stats_taxa_reclassification_stats_get(taxa_ids)

Reclassif Stats

Dig into reclassification logs and, for each input category id, determine the most chosen target category, excluding the advised one. By convention, if nothing relevant is found, the input category itself is returned. So one can expect that the returned list has the same size as the required one.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
from ecotaxa_cli_py.model.taxon_model import TaxonModel
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    taxa_ids = "taxa_ids_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Reclassif Stats
        api_response = api_instance.reclassif_stats_taxa_reclassification_stats_get(taxa_ids)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->reclassif_stats_taxa_reclassification_stats_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxa_ids** | **str**|  |

### Return type

[**[TaxonModel]**](TaxonModel.md)

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

# **search_taxa_taxon_set_search_get**
> [TaxaSearchRsp] search_taxa_taxon_set_search_get(query)

Search Taxa

Search for taxa by name.  Queries can be 'small', i.e. of length < 3 and even zero-length. For a public, unauthenticated call: - zero-length and small queries always return nothing. - otherwise, a full search is done and results are returned in alphabetical order.  Behavior for an authenticated call: - zero-length queries: return the MRU list in full. - small queries: the MRU list is searched, so that taxa in the recent list are returned, if matching. - otherwise, a full search is done. Results are ordered so that taxa in the project list are in first,     and are signalled as such in the response.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.taxa_search_rsp import TaxaSearchRsp
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)
    query = "query_example" # str | 
    project_id = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Taxa
        api_response = api_instance.search_taxa_taxon_set_search_get(query)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->search_taxa_taxon_set_search_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Taxa
        api_response = api_instance.search_taxa_taxon_set_search_get(query, project_id=project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->search_taxa_taxon_set_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  |
 **project_id** | **int**|  | [optional]

### Return type

[**[TaxaSearchRsp]**](TaxaSearchRsp.md)

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

# **taxa_tree_status_taxa_status_get**
> TaxonomyTreeStatus taxa_tree_status_taxa_status_get()

Taxa Tree Status

Return the status of taxonomy tree w/r to freshness.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import taxonomy_tree_api
from ecotaxa_cli_py.model.taxonomy_tree_status import TaxonomyTreeStatus
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
    api_instance = taxonomy_tree_api.TaxonomyTreeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Taxa Tree Status
        api_response = api_instance.taxa_tree_status_taxa_status_get()
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling TaxonomyTreeApi->taxa_tree_status_taxa_status_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxonomyTreeStatus**](TaxonomyTreeStatus.md)

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


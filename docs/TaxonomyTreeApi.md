# ecotaxa_py_client.TaxonomyTreeApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_taxon_in_central**](TaxonomyTreeApi.md#add_taxon_in_central) | **PUT** /taxon/central | Add Taxon In Central
[**get_taxon_in_central**](TaxonomyTreeApi.md#get_taxon_in_central) | **GET** /taxon/central/{taxon_id} | Get Taxon In Central
[**pull_taxa_update_from_central**](TaxonomyTreeApi.md#pull_taxa_update_from_central) | **GET** /taxa/pull_from_central | Pull Taxa Update From Central
[**push_taxa_stats_in_central**](TaxonomyTreeApi.md#push_taxa_stats_in_central) | **GET** /taxa/stats/push_to_central | Push Taxa Stats In Central
[**query_root_taxa**](TaxonomyTreeApi.md#query_root_taxa) | **GET** /taxa | Query Root Taxa
[**query_taxa**](TaxonomyTreeApi.md#query_taxa) | **GET** /taxon/{taxon_id} | Query Taxa
[**query_taxa_set**](TaxonomyTreeApi.md#query_taxa_set) | **GET** /taxon_set/query | Query Taxa Set
[**query_taxa_usage**](TaxonomyTreeApi.md#query_taxa_usage) | **GET** /taxon/{taxon_id}/usage | Query Taxa Usage
[**reclassif_project_stats**](TaxonomyTreeApi.md#reclassif_project_stats) | **GET** /taxa/reclassification_history/{project_id} | Reclassif Project Stats
[**reclassif_stats**](TaxonomyTreeApi.md#reclassif_stats) | **GET** /taxa/reclassification_stats | Reclassif Stats
[**search_taxa**](TaxonomyTreeApi.md#search_taxa) | **GET** /taxon_set/search | Search Taxa
[**taxa_tree_status**](TaxonomyTreeApi.md#taxa_tree_status) | **GET** /taxa/status | Taxa Tree Status


# **add_taxon_in_central**
> object add_taxon_in_central(name, parent_id, taxotype, creator_email, source_desc=source_desc, source_url=source_url)

Add Taxon In Central

**Create a taxon** on EcoTaxoServer.  🔒 Logged user must be manager (on any project) or application admin.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    name = 'Echinodermata' # str | The taxon/category verbatim name.
    parent_id = 2367 # int | It's not possible to create a root taxon.
    taxotype = 'P' # str | The taxon type, 'M' for Morpho or 'P' for Phylo.
    creator_email = 'user.creator@email.com' # str | The email of the taxo creator.
    source_desc = 'null' # str | The source description. (optional)
    source_url = 'http://www.google.fr/' # str | The source url. (optional)

    try:
        # Add Taxon In Central
        api_response = api_instance.add_taxon_in_central(name, parent_id, taxotype, creator_email, source_desc=source_desc, source_url=source_url)
        print("The response of TaxonomyTreeApi->add_taxon_in_central:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->add_taxon_in_central: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The taxon/category verbatim name. | 
 **parent_id** | **int**| It&#39;s not possible to create a root taxon. | 
 **taxotype** | **str**| The taxon type, &#39;M&#39; for Morpho or &#39;P&#39; for Phylo. | 
 **creator_email** | **str**| The email of the taxo creator. | 
 **source_desc** | **str**| The source description. | [optional] 
 **source_url** | **str**| The source url. | [optional] 

### Return type

**object**

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

# **get_taxon_in_central**
> List[TaxonCentral] get_taxon_in_central(taxon_id)

Get Taxon In Central

Return **EcoTaxoServer full record for this taxon**.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxon_central import TaxonCentral
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    taxon_id = 12876 # int | Internal, the unique numeric id of this taxon.

    try:
        # Get Taxon In Central
        api_response = api_instance.get_taxon_in_central(taxon_id)
        print("The response of TaxonomyTreeApi->get_taxon_in_central:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->get_taxon_in_central: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_id** | **int**| Internal, the unique numeric id of this taxon. | 

### Return type

[**List[TaxonCentral]**](TaxonCentral.md)

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

# **pull_taxa_update_from_central**
> object pull_taxa_update_from_central()

Pull Taxa Update From Central

**Returns what changed in EcoTaxoServer managed tree** and update local tree accordingly.  i.e. : the number of inserts as nbr_inserts, updates as nbr_updates and errors as errors.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)

    try:
        # Pull Taxa Update From Central
        api_response = api_instance.pull_taxa_update_from_central()
        print("The response of TaxonomyTreeApi->pull_taxa_update_from_central:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->pull_taxa_update_from_central: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **push_taxa_stats_in_central**
> object push_taxa_stats_in_central()

Push Taxa Stats In Central

**Push present instance stats**, into EcoTaxoServer.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)

    try:
        # Push Taxa Stats In Central
        api_response = api_instance.push_taxa_stats_in_central()
        print("The response of TaxonomyTreeApi->push_taxa_stats_in_central:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->push_taxa_stats_in_central: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **query_root_taxa**
> List[TaxonModel] query_root_taxa()

Query Root Taxa

**Return all taxa with no parent.**

### Example


```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxon_model import TaxonModel
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)

    try:
        # Query Root Taxa
        api_response = api_instance.query_root_taxa()
        print("The response of TaxonomyTreeApi->query_root_taxa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->query_root_taxa: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TaxonModel]**](TaxonModel.md)

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

# **query_taxa**
> TaxonModel query_taxa(taxon_id)

Query Taxa

Returns **information about the taxon** corresponding to the given id, including its lineage.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxon_model import TaxonModel
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    taxon_id = 12876 # int | Internal, the unique numeric id of this taxon.

    try:
        # Query Taxa
        api_response = api_instance.query_taxa(taxon_id)
        print("The response of TaxonomyTreeApi->query_taxa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->query_taxa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_id** | **int**| Internal, the unique numeric id of this taxon. | 

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

# **query_taxa_set**
> List[TaxonModel] query_taxa_set(ids)

Query Taxa Set

Returns **information about several taxa**, including their lineage.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxon_model import TaxonModel
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    ids = '1:2:3' # str | The separator between numbers is arbitrary non-digit, e.g. ':', '|' or ','.

    try:
        # Query Taxa Set
        api_response = api_instance.query_taxa_set(ids)
        print("The response of TaxonomyTreeApi->query_taxa_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->query_taxa_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| The separator between numbers is arbitrary non-digit, e.g. &#39;:&#39;, &#39;|&#39; or &#39;,&#39;. | 

### Return type

[**List[TaxonModel]**](TaxonModel.md)

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

# **query_taxa_usage**
> List[TaxonUsageModel] query_taxa_usage(taxon_id)

Query Taxa Usage

**Where a given taxon is used.**  Only validated uses are returned.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxon_usage_model import TaxonUsageModel
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    taxon_id = 12876 # int | Internal, the unique numeric id of this taxon.

    try:
        # Query Taxa Usage
        api_response = api_instance.query_taxa_usage(taxon_id)
        print("The response of TaxonomyTreeApi->query_taxa_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->query_taxa_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_id** | **int**| Internal, the unique numeric id of this taxon. | 

### Return type

[**List[TaxonUsageModel]**](TaxonUsageModel.md)

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

# **reclassif_project_stats**
> List[object] reclassif_project_stats(project_id)

Reclassif Project Stats

Dig into reclassification logs and **return the associations (source → target) for previous reclassifications.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.

    try:
        # Reclassif Project Stats
        api_response = api_instance.reclassif_project_stats(project_id)
        print("The response of TaxonomyTreeApi->reclassif_project_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->reclassif_project_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 

### Return type

**List[object]**

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

# **reclassif_stats**
> List[TaxonModel] reclassif_stats(taxa_ids)

Reclassif Stats

Dig into reclassification logs and, for each input category id, **determine the most chosen target category, excluding the advised one.**  By convention, if nothing relevant is found, the input category itself is returned. So one can expect that the returned list has the same size as the required one.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxon_model import TaxonModel
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    taxa_ids = '12876' # str | String containing the list of one or more taxa id separated by non-num char.

    try:
        # Reclassif Stats
        api_response = api_instance.reclassif_stats(taxa_ids)
        print("The response of TaxonomyTreeApi->reclassif_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->reclassif_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxa_ids** | **str**| String containing the list of one or more taxa id separated by non-num char. | 

### Return type

[**List[TaxonModel]**](TaxonModel.md)

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

# **search_taxa**
> List[TaxaSearchRsp] search_taxa(query, project_id=project_id)

Search Taxa

**Search for taxa by name.**  Queries can be 'small', i.e. of length ﹤3 and even zero-length.  🔓 For a public, unauthenticated call : - zero-length and small queries always return nothing. - otherwise, a full search is done and results are returned in alphabetical order.  🔒 For an authenticated call : - zero-length queries: return the MRU list in full. - small queries: the MRU list is searched, so that taxa in the recent list are returned, if matching. - otherwise, a full search is done. Results are ordered so that taxa in the project list are in first,     and are signalled as such in the response.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxa_search_rsp import TaxaSearchRsp
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)
    query = 'Ban' # str | Use this query for matching returned taxa names.
    project_id = 1 # int | Internal, numeric id of the project. (optional)

    try:
        # Search Taxa
        api_response = api_instance.search_taxa(query, project_id=project_id)
        print("The response of TaxonomyTreeApi->search_taxa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->search_taxa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Use this query for matching returned taxa names. | 
 **project_id** | **int**| Internal, numeric id of the project. | [optional] 

### Return type

[**List[TaxaSearchRsp]**](TaxaSearchRsp.md)

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

# **taxa_tree_status**
> TaxonomyTreeStatus taxa_tree_status()

Taxa Tree Status

**Return the status of taxonomy tree** w/r to freshness.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxonomy_tree_status import TaxonomyTreeStatus
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
    api_instance = ecotaxa_py_client.TaxonomyTreeApi(api_client)

    try:
        # Taxa Tree Status
        api_response = api_instance.taxa_tree_status()
        print("The response of TaxonomyTreeApi->taxa_tree_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTreeApi->taxa_tree_status: %s\n" % e)
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


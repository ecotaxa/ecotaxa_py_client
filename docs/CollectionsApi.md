# ecotaxa_py_client.CollectionsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collection_by_short_title**](CollectionsApi.md#collection_by_short_title) | **GET** /collections/by_short_title | Collection By Short Title
[**collection_by_title**](CollectionsApi.md#collection_by_title) | **GET** /collections/by_title | Collection By Title
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /collections/create | Create Collection
[**darwin_core_format_export**](CollectionsApi.md#darwin_core_format_export) | **POST** /collections/export/darwin_core | Darwin Core Format Export
[**erase_collection**](CollectionsApi.md#erase_collection) | **DELETE** /collections/{collection_id} | Erase Collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /collections/{collection_id} | Get Collection
[**get_collection_taxonomy_recast**](CollectionsApi.md#get_collection_taxonomy_recast) | **GET** /collections/{collection_id}/taxo_recast | Read Collection Taxo Recast
[**search_collections**](CollectionsApi.md#search_collections) | **GET** /collections/search | Search Collections
[**update_collection**](CollectionsApi.md#update_collection) | **PUT** /collections/{collection_id} | Update Collection
[**update_collection_taxonomy_recast**](CollectionsApi.md#update_collection_taxonomy_recast) | **PUT** /collections/{collection_id}/taxo_recast | Update Collection Taxo Recast


# **collection_by_short_title**
> CollectionModel collection_by_short_title(q)

Collection By Short Title

Return the **single collection with this short title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️

### Example


```python
import ecotaxa_py_client
from ecotaxa_py_client.models.collection_model import CollectionModel
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    q = 'My coll' # str | Search by **exact** short title.

    try:
        # Collection By Short Title
        api_response = api_instance.collection_by_short_title(q)
        print("The response of CollectionsApi->collection_by_short_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collection_by_short_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search by **exact** short title. | 

### Return type

[**CollectionModel**](CollectionModel.md)

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

# **collection_by_title**
> CollectionModel collection_by_title(q)

Collection By Title

Return the **single collection with this title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️

### Example


```python
import ecotaxa_py_client
from ecotaxa_py_client.models.collection_model import CollectionModel
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    q = 'My collection' # str | Search by **exact** title.

    try:
        # Collection By Title
        api_response = api_instance.collection_by_title(q)
        print("The response of CollectionsApi->collection_by_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collection_by_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search by **exact** title. | 

### Return type

[**CollectionModel**](CollectionModel.md)

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

# **create_collection**
> int create_collection(create_collection_req)

Create Collection

**Create a collection** with at least one project inside.  Returns the created collection Id.  Note: 'manage' right is required on all underlying projects.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.create_collection_req import CreateCollectionReq
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    create_collection_req = ecotaxa_py_client.CreateCollectionReq() # CreateCollectionReq | 

    try:
        # Create Collection
        api_response = api_instance.create_collection(create_collection_req)
        print("The response of CollectionsApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collection_req** | [**CreateCollectionReq**](CreateCollectionReq.md)|  | 

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

# **darwin_core_format_export**
> ExportRsp darwin_core_format_export(darwin_core_export_req)

Darwin Core Format Export

**Export the collection in Darwin Core format, e.g. for EMODnet portal**, @see https://www.emodnet-ingestion.eu  Produces a DwC-A (https://dwc.tdwg.org/) archive into a temporary directory, ready for download.  Maybe useful, a reader in Python: https://python-dwca-reader.readthedocs.io/en/latest/index.html  Note: Only manageable collections can be exported.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.darwin_core_export_req import DarwinCoreExportReq
from ecotaxa_py_client.models.export_rsp import ExportRsp
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    darwin_core_export_req = ecotaxa_py_client.DarwinCoreExportReq() # DarwinCoreExportReq | 

    try:
        # Darwin Core Format Export
        api_response = api_instance.darwin_core_format_export(darwin_core_export_req)
        print("The response of CollectionsApi->darwin_core_format_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->darwin_core_format_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **darwin_core_export_req** | [**DarwinCoreExportReq**](DarwinCoreExportReq.md)|  | 

### Return type

[**ExportRsp**](ExportRsp.md)

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

# **erase_collection**
> int erase_collection(collection_id)

Erase Collection

**Delete the collection**,  i.e. the precious fields, as the projects are just linked-at from the collection.  Note: Only manageable collections can be deleted.

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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    collection_id = 1 # int | Internal, the unique numeric id of this collection.

    try:
        # Erase Collection
        api_response = api_instance.erase_collection(collection_id)
        print("The response of CollectionsApi->erase_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->erase_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Internal, the unique numeric id of this collection. | 

### Return type

**int**

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

# **get_collection**
> CollectionModel get_collection(collection_id)

Get Collection

Returns **information about the collection** corresponding to the given id.  Note: The collection is returned only if manageable.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.collection_model import CollectionModel
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    collection_id = 1 # int | Internal, the unique numeric id of this collection.

    try:
        # Get Collection
        api_response = api_instance.get_collection(collection_id)
        print("The response of CollectionsApi->get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Internal, the unique numeric id of this collection. | 

### Return type

[**CollectionModel**](CollectionModel.md)

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

# **get_collection_taxonomy_recast**
> object get_collection_taxonomy_recast(collection_id)

Read Collection Taxo Recast

**Read the collection taxonomy recast**.   **Returns NULL upon success.**   Note: The collection data is returned only if manageable.

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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    collection_id = 1 # int | Internal, the unique numeric id of this collection.

    try:
        # Read Collection Taxo Recast
        api_response = api_instance.get_collection_taxonomy_recast(collection_id)
        print("The response of CollectionsApi->get_collection_taxonomy_recast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collection_taxonomy_recast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Internal, the unique numeric id of this collection. | 

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

# **search_collections**
> List[CollectionModel] search_collections(title)

Search Collections

**Search for collections.**  Note: Only manageable collections are returned.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.collection_model import CollectionModel
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    title = '%coll%' # str | Search by title, use % for searching with 'any char'.

    try:
        # Search Collections
        api_response = api_instance.search_collections(title)
        print("The response of CollectionsApi->search_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->search_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Search by title, use % for searching with &#39;any char&#39;. | 

### Return type

[**List[CollectionModel]**](CollectionModel.md)

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

# **update_collection**
> object update_collection(collection_id, collection_model)

Update Collection

**Update the collection**. Note that some updates are silently failing when not compatible  with the composing projects.   **Returns NULL upon success.**   Note: The collection is updated only if manageable.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.collection_model import CollectionModel
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    collection_id = 1 # int | Internal, the unique numeric id of this collection.
    collection_model = ecotaxa_py_client.CollectionModel() # CollectionModel | 

    try:
        # Update Collection
        api_response = api_instance.update_collection(collection_id, collection_model)
        print("The response of CollectionsApi->update_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Internal, the unique numeric id of this collection. | 
 **collection_model** | [**CollectionModel**](CollectionModel.md)|  | 

### Return type

**object**

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

# **update_collection_taxonomy_recast**
> object update_collection_taxonomy_recast(collection_id, taxonomy_recast)

Update Collection Taxo Recast

**Create or Update the collection taxonomy recast**.   **Returns NULL upon success.**   Note: The collection is updated only if manageable.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.taxonomy_recast import TaxonomyRecast
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
    api_instance = ecotaxa_py_client.CollectionsApi(api_client)
    collection_id = 1 # int | Internal, the unique numeric id of this collection.
    taxonomy_recast = ecotaxa_py_client.TaxonomyRecast() # TaxonomyRecast | 

    try:
        # Update Collection Taxo Recast
        api_response = api_instance.update_collection_taxonomy_recast(collection_id, taxonomy_recast)
        print("The response of CollectionsApi->update_collection_taxonomy_recast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->update_collection_taxonomy_recast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Internal, the unique numeric id of this collection. | 
 **taxonomy_recast** | [**TaxonomyRecast**](TaxonomyRecast.md)|  | 

### Return type

**object**

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


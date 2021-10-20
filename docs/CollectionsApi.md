# ecotaxa_cli_py.CollectionsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collection_by_short_title**](CollectionsApi.md#collection_by_short_title) | **GET** /collections/by_short_title | Collection By Short Title
[**collection_by_title**](CollectionsApi.md#collection_by_title) | **GET** /collections/by_title | Collection By Title
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /collections/create | Create Collection
[**emodnet_format_export**](CollectionsApi.md#emodnet_format_export) | **GET** /collections/{collection_id}/export/emodnet | Emodnet Format Export
[**erase_collection**](CollectionsApi.md#erase_collection) | **DELETE** /collections/{collection_id} | Erase Collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /collections/{collection_id} | Get Collection
[**search_collections**](CollectionsApi.md#search_collections) | **GET** /collections/search | Search Collections
[**update_collection**](CollectionsApi.md#update_collection) | **PUT** /collections/{collection_id} | Update Collection


# **collection_by_short_title**
> CollectionModel collection_by_short_title(q=q)

Collection By Short Title

Return the **single collection with this short title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️ 

### Example

```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    q = 'My coll' # str | Search by **exact** short title (optional)

    try:
        # Collection By Short Title
        api_response = api_instance.collection_by_short_title(q=q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->collection_by_short_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search by **exact** short title | [optional] 

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
> CollectionModel collection_by_title(q=q)

Collection By Title

Return the **single collection with this title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️ 

### Example

```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    q = 'My collection' # str | Search by **exact** title (optional)

    try:
        # Collection By Title
        api_response = api_instance.collection_by_title(q=q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->collection_by_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search by **exact** title | [optional] 

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

**Create a collection** with at least one project inside.  Returns the created collection Id.  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):
```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
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
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    create_collection_req = ecotaxa_cli_py.CreateCollectionReq() # CreateCollectionReq | 

    try:
        # Create Collection
        api_response = api_instance.create_collection(create_collection_req)
        pprint(api_response)
    except ApiException as e:
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

# **emodnet_format_export**
> EMODnetExportRsp emodnet_format_export(collection_id, dry_run=dry_run, with_zeroes=with_zeroes, auto_morpho=auto_morpho, with_computations=with_computations)

Emodnet Format Export

**Export the collection in EMODnet format**, @see https://www.emodnet-ingestion.eu  Produces a DwC-A archive into a temporary directory, ready for download.  Maybe useful, a reader in Python: https://python-dwca-reader.readthedocs.io/en/latest/index.html  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):
```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
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
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    collection_id = 56 # int | 
dry_run = false # bool | If set, then only a diagnostic of doability will be done. (optional)
with_zeroes = false # bool | If set, then *absent* records will be generated, in the relevant samples, for categories present in other samples. (optional)
auto_morpho = false # bool | If set, then any object classified on a Morpho category will be added to the count of the nearest Phylo parent, upward in the tree. (optional)
with_computations = false # bool | If set, then an attempt will be made to compute organisms concentrations and biovolumes. (optional)

    try:
        # Emodnet Format Export
        api_response = api_instance.emodnet_format_export(collection_id, dry_run=dry_run, with_zeroes=with_zeroes, auto_morpho=auto_morpho, with_computations=with_computations)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->emodnet_format_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  | 
 **dry_run** | **bool**| If set, then only a diagnostic of doability will be done. | [optional] 
 **with_zeroes** | **bool**| If set, then *absent* records will be generated, in the relevant samples, for categories present in other samples. | [optional] 
 **auto_morpho** | **bool**| If set, then any object classified on a Morpho category will be added to the count of the nearest Phylo parent, upward in the tree. | [optional] 
 **with_computations** | **bool**| If set, then an attempt will be made to compute organisms concentrations and biovolumes. | [optional] 

### Return type

[**EMODnetExportRsp**](EMODnetExportRsp.md)

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

# **erase_collection**
> int erase_collection(collection_id)

Erase Collection

**Delete the collection**,   i.e. the precious fields, as the projects are just linked-at from the collection.  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):
```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
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
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    collection_id = 56 # int | 

    try:
        # Erase Collection
        api_response = api_instance.erase_collection(collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->erase_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  | 

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

Returns **information about the collection** corresponding to the given id.   🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):
```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
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
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    collection_id = 56 # int | 

    try:
        # Get Collection
        api_response = api_instance.get_collection(collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  | 

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

# **search_collections**
> list[CollectionModel] search_collections(title=title)

Search Collections

**Search for collections.**  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):
```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
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
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    title = '%coll%' # str | Search by title, use % for searching with 'any char'. (optional)

    try:
        # Search Collections
        api_response = api_instance.search_collections(title=title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->search_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Search by title, use % for searching with &#39;any char&#39;. | [optional] 

### Return type

[**list[CollectionModel]**](CollectionModel.md)

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

**Update the collection**. Note that some updates are silently failing when not compatible  with the composing projects.   🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):
```python
from __future__ import print_function
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
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
    api_instance = ecotaxa_cli_py.CollectionsApi(api_client)
    collection_id = 56 # int | 
collection_model = ecotaxa_cli_py.CollectionModel() # CollectionModel | 

    try:
        # Update Collection
        api_response = api_instance.update_collection(collection_id, collection_model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  | 
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


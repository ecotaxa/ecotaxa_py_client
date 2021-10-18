# ecotaxa_cli_py.CollectionsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collection_by_short_title_collections_by_short_title_get**](CollectionsApi.md#collection_by_short_title_collections_by_short_title_get) | **GET** /collections/by_short_title | Collection By Short Title
[**collection_by_title_collections_by_title_get**](CollectionsApi.md#collection_by_title_collections_by_title_get) | **GET** /collections/by_title | Collection By Title
[**create_collection_collections_create_post**](CollectionsApi.md#create_collection_collections_create_post) | **POST** /collections/create | Create Collection
[**emodnet_format_export_collections_collection_id_export_emodnet_get**](CollectionsApi.md#emodnet_format_export_collections_collection_id_export_emodnet_get) | **GET** /collections/{collection_id}/export/emodnet | Emodnet Format Export
[**erase_collection_collections_collection_id_delete**](CollectionsApi.md#erase_collection_collections_collection_id_delete) | **DELETE** /collections/{collection_id} | Erase Collection
[**get_collection_collections_collection_id_get**](CollectionsApi.md#get_collection_collections_collection_id_get) | **GET** /collections/{collection_id} | Get Collection
[**search_collections_collections_search_get**](CollectionsApi.md#search_collections_collections_search_get) | **GET** /collections/search | Search Collections
[**update_collection_collections_collection_id_put**](CollectionsApi.md#update_collection_collections_collection_id_put) | **PUT** /collections/{collection_id} | Update Collection


# **collection_by_short_title_collections_by_short_title_get**
> CollectionModel collection_by_short_title_collections_by_short_title_get()

Collection By Short Title

Return the **single collection with this short title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️ 

### Example


```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.collection_model import CollectionModel
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = collections_api.CollectionsApi(api_client)
    q = "My coll" # str | Search by **exact** short title (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Collection By Short Title
        api_response = api_instance.collection_by_short_title_collections_by_short_title_get(q=q)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->collection_by_short_title_collections_by_short_title_get: %s\n" % e)
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

# **collection_by_title_collections_by_title_get**
> CollectionModel collection_by_title_collections_by_title_get()

Collection By Title

Return the **single collection with this title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️ 

### Example


```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.collection_model import CollectionModel
from pprint import pprint
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = collections_api.CollectionsApi(api_client)
    q = "My collection" # str | Search by **exact** title (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Collection By Title
        api_response = api_instance.collection_by_title_collections_by_title_get(q=q)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->collection_by_title_collections_by_title_get: %s\n" % e)
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

# **create_collection_collections_create_post**
> int create_collection_collections_create_post(create_collection_req)

Create Collection

**Create a collection** with at least one project inside.  Returns the created collection Id.  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
from ecotaxa_cli_py.model.create_collection_req import CreateCollectionReq
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
    api_instance = collections_api.CollectionsApi(api_client)
    create_collection_req = CreateCollectionReq(
        title="My collection",
        project_ids=[1],
    ) # CreateCollectionReq | 

    # example passing only required values which don't have defaults set
    try:
        # Create Collection
        api_response = api_instance.create_collection_collections_create_post(create_collection_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->create_collection_collections_create_post: %s\n" % e)
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

# **emodnet_format_export_collections_collection_id_export_emodnet_get**
> EMODnetExportRsp emodnet_format_export_collections_collection_id_export_emodnet_get(collection_id)

Emodnet Format Export

**Export the collection in EMODnet format**, @see https://www.emodnet-ingestion.eu  Produces a DwC-A archive into a temporary directory, ready for download.  Maybe useful, a reader in Python: https://python-dwca-reader.readthedocs.io/en/latest/index.html  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
from ecotaxa_cli_py.model.emo_dnet_export_rsp import EMODnetExportRsp
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # int | 
    dry_run = False # bool | If set, then only a diagnostic of doability will be done. (optional)
    with_zeroes = False # bool | If set, then *absent* records will be generated, in the relevant samples, for categories present in other samples. (optional)
    auto_morpho = False # bool | If set, then any object classified on a Morpho category will be added to the count of the nearest Phylo parent, upward in the tree. (optional)
    with_computations = False # bool | If set, then an attempt will be made to compute organisms concentrations and biovolumes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Emodnet Format Export
        api_response = api_instance.emodnet_format_export_collections_collection_id_export_emodnet_get(collection_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->emodnet_format_export_collections_collection_id_export_emodnet_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Emodnet Format Export
        api_response = api_instance.emodnet_format_export_collections_collection_id_export_emodnet_get(collection_id, dry_run=dry_run, with_zeroes=with_zeroes, auto_morpho=auto_morpho, with_computations=with_computations)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->emodnet_format_export_collections_collection_id_export_emodnet_get: %s\n" % e)
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

# **erase_collection_collections_collection_id_delete**
> int erase_collection_collections_collection_id_delete(collection_id)

Erase Collection

**Delete the collection**,   i.e. the precious fields, as the projects are just linked-at from the collection.  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Erase Collection
        api_response = api_instance.erase_collection_collections_collection_id_delete(collection_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->erase_collection_collections_collection_id_delete: %s\n" % e)
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

# **get_collection_collections_collection_id_get**
> CollectionModel get_collection_collections_collection_id_get(collection_id)

Get Collection

Returns **information about the collection** corresponding to the given id.   🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.collection_model import CollectionModel
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Collection
        api_response = api_instance.get_collection_collections_collection_id_get(collection_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->get_collection_collections_collection_id_get: %s\n" % e)
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

# **search_collections_collections_search_get**
> [CollectionModel] search_collections_collections_search_get()

Search Collections

**Search for collections.**  🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.collection_model import CollectionModel
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
    api_instance = collections_api.CollectionsApi(api_client)
    title = "%coll%" # str | Search by title, use % for searching with 'any char'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Collections
        api_response = api_instance.search_collections_collections_search_get(title=title)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->search_collections_collections_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Search by title, use % for searching with &#39;any char&#39;. | [optional]

### Return type

[**[CollectionModel]**](CollectionModel.md)

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

# **update_collection_collections_collection_id_put**
> bool, date, datetime, dict, float, int, list, str, none_type update_collection_collections_collection_id_put(collection_id, collection_model)

Update Collection

**Update the collection**. Note that some updates are silently failing when not compatible  with the composing projects.   🔒 *For admins only.*

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import collections_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.collection_model import CollectionModel
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # int | 
    collection_model = CollectionModel(
        project_ids=[1],
        provider_user=,
        contact_user=,
        creator_users=[
            UserModel(
                id=1,
                email="user@email.com",
                name="userName",
                organisation="Oceanographic Laboratory of Villefranche sur Mer - LOV",
                active=True,
                country="France",
                usercreationdate=dateutil_parser('1970-01-01T00:00:00.00Z'),
                usercreationreason="Analysis of size and shapes of plastic particles",
            ),
        ],
        creator_organisations=[],
        associate_users=[
            UserModel(
                id=1,
                email="user@email.com",
                name="userName",
                organisation="Oceanographic Laboratory of Villefranche sur Mer - LOV",
                active=True,
                country="France",
                usercreationdate=dateutil_parser('1970-01-01T00:00:00.00Z'),
                usercreationreason="Analysis of size and shapes of plastic particles",
            ),
        ],
        associate_organisations=[],
        id=1,
        external_id="",
        external_id_system="",
        title="My collection",
        short_title="My coll",
        citation="",
        license="CC BY 4.0",
        abstract="",
        description="",
    ) # CollectionModel | 

    # example passing only required values which don't have defaults set
    try:
        # Update Collection
        api_response = api_instance.update_collection_collections_collection_id_put(collection_id, collection_model)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling CollectionsApi->update_collection_collections_collection_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  |
 **collection_model** | [**CollectionModel**](CollectionModel.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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


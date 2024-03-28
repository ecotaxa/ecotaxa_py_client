# ecotaxa_py_client.ProjectsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects/create | Create Project
[**erase_project**](ProjectsApi.md#erase_project) | **DELETE** /projects/{project_id} | Erase Project
[**import_file**](ProjectsApi.md#import_file) | **POST** /file_import/{project_id} | Import File
[**project_check**](ProjectsApi.md#project_check) | **GET** /projects/{project_id}/check | Project Check
[**project_merge**](ProjectsApi.md#project_merge) | **POST** /projects/{project_id}/merge | Project Merge
[**project_query**](ProjectsApi.md#project_query) | **GET** /projects/{project_id} | Project Query
[**project_recompute_geography**](ProjectsApi.md#project_recompute_geography) | **POST** /projects/{project_id}/recompute_geo | Project Recompute Geography
[**project_recompute_sunpos**](ProjectsApi.md#project_recompute_sunpos) | **POST** /projects/{project_id}/recompute_sunpos | Project Recompute Sunpos
[**project_set_get_column_stats**](ProjectsApi.md#project_set_get_column_stats) | **GET** /project_set/column_stats | Project Set Get Column Stats
[**project_set_get_stats**](ProjectsApi.md#project_set_get_stats) | **GET** /project_set/taxo_stats | Project Set Get Stats
[**project_set_get_user_stats**](ProjectsApi.md#project_set_get_user_stats) | **GET** /project_set/user_stats | Project Set Get User Stats
[**project_stats**](ProjectsApi.md#project_stats) | **GET** /projects/{project_id}/stats | Project Stats
[**project_subset**](ProjectsApi.md#project_subset) | **POST** /projects/{project_id}/subset | Project Subset
[**search_projects**](ProjectsApi.md#search_projects) | **GET** /projects/search | Search Projects
[**set_project_predict_settings**](ProjectsApi.md#set_project_predict_settings) | **PUT** /projects/{project_id}/prediction_settings | Set Project Predict Settings
[**simple_import**](ProjectsApi.md#simple_import) | **POST** /simple_import/{project_id} | Simple Import
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{project_id} | Update Project


# **create_project**
> int create_project(create_project_req)

Create Project

**Create an empty project with only a title,** and **return the numeric id of this newly created project**.  The project will be managed by current user.  🔒 The user has to be *app administrator* or *project creator*.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.create_project_req import CreateProjectReq
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    create_project_req = ecotaxa_py_client.CreateProjectReq() # CreateProjectReq | 

    try:
        # Create Project
        api_response = api_instance.create_project(create_project_req)
        print("The response of ProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_req** | [**CreateProjectReq**](CreateProjectReq.md)|  | 

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

# **erase_project**
> object erase_project(project_id, only_objects=only_objects)

Erase Project

**Delete the project.**  Optionally, if \"only_objects\" is set, the project structure is kept, but emptied from any object, sample, acquisition and process.  Otherwise, no trace of the project will remain in the database.  **Returns** the number of  : **deleted objects**, 0, **deleated image rows** and **deleated image files**.

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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    only_objects = False # bool | If set, the project structure is kept, but emptied from any object, sample, acquisition and process. (optional) (default to False)

    try:
        # Erase Project
        api_response = api_instance.erase_project(project_id, only_objects=only_objects)
        print("The response of ProjectsApi->erase_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->erase_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **only_objects** | **bool**| If set, the project structure is kept, but emptied from any object, sample, acquisition and process. | [optional] [default to False]

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

# **import_file**
> ImportRsp import_file(project_id, import_req)

Import File

**Validate or do a real import** of an EcoTaxa archive or directory.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.import_req import ImportReq
from ecotaxa_py_client.models.import_rsp import ImportRsp
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    import_req = ecotaxa_py_client.ImportReq() # ImportReq | 

    try:
        # Import File
        api_response = api_instance.import_file(project_id, import_req)
        print("The response of ProjectsApi->import_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->import_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **import_req** | [**ImportReq**](ImportReq.md)|  | 

### Return type

[**ImportRsp**](ImportRsp.md)

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

# **project_check**
> List[str] project_check(project_id)

Project Check

**Check consistency of a project**.  With time and bugs, some consistency problems could be introduced in projects. This service aims at listing them.

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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.

    try:
        # Project Check
        api_response = api_instance.project_check(project_id)
        print("The response of ProjectsApi->project_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 

### Return type

**List[str]**

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

# **project_merge**
> MergeRsp project_merge(project_id, source_project_id, dry_run)

Project Merge

**Merge another project into this one.**  It's more a phagocytosis than a merge, as all objects from this source project will be moved to the project_id above and the source project itself will be deleted.  TODO: Explain a bit with it might fail (too many free columns, unique orig_ids collision)

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.merge_rsp import MergeRsp
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    source_project_id = 2 # int | Id of the other project. All objects from this source project will be moved to the project_id above and the source project itself will be deleted.
    dry_run = true # bool | If set, then only a diagnostic of doability will be done.

    try:
        # Project Merge
        api_response = api_instance.project_merge(project_id, source_project_id, dry_run)
        print("The response of ProjectsApi->project_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **source_project_id** | **int**| Id of the other project. All objects from this source project will be moved to the project_id above and the source project itself will be deleted. | 
 **dry_run** | **bool**| If set, then only a diagnostic of doability will be done. | 

### Return type

[**MergeRsp**](MergeRsp.md)

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

# **project_query**
> ProjectModel project_query(project_id, for_managing=for_managing)

Project Query

**Returns project** if it exists for current user, eventually for managing it.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_model import ProjectModel
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    for_managing = False # bool | For managing this project. (optional) (default to False)

    try:
        # Project Query
        api_response = api_instance.project_query(project_id, for_managing=for_managing)
        print("The response of ProjectsApi->project_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **for_managing** | **bool**| For managing this project. | [optional] [default to False]

### Return type

[**ProjectModel**](ProjectModel.md)

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

# **project_recompute_geography**
> object project_recompute_geography(project_id)

Project Recompute Geography

**Recompute geography information** for all samples in project.  **Returns NULL upon success.**  🔒 The user has to be *project manager*.

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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.

    try:
        # Project Recompute Geography
        api_response = api_instance.project_recompute_geography(project_id)
        print("The response of ProjectsApi->project_recompute_geography:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_recompute_geography: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 

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

# **project_recompute_sunpos**
> object project_recompute_sunpos(project_id)

Project Recompute Sunpos

**Recompute sun position field** for all objects in project.  **Returns NULL upon success.**  🔒 The user has to be *project manager* on the referenced project.

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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.

    try:
        # Project Recompute Sunpos
        api_response = api_instance.project_recompute_sunpos(project_id)
        print("The response of ProjectsApi->project_recompute_sunpos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_recompute_sunpos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 

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

# **project_set_get_column_stats**
> ProjectSetColumnStatsModel project_set_get_column_stats(ids, names, limit=limit, categories=categories)

Project Set Get Column Stats

**Returns projects validated data statistics**, for all named columns, in all given projects.  The free columns here are named by the alias e.g. 'area', not technical name e.g. 'n43'.  This allows getting stats on projects with different mappings, but common names.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_set_column_stats_model import ProjectSetColumnStatsModel
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    ids = '1400+1453' # str | String containing the list of one or more id separated by non-num char.
    names = 'fre.area,obj.depth_min,fre.nb2' # str | Coma-separated prefixed columns, on which stats are needed.
    limit = 5000 # int | Only compute stats on this number of objects per category. (optional)
    categories = '493,567' # str | String containing the Categories, one or more id separated by non-num char. (optional)

    try:
        # Project Set Get Column Stats
        api_response = api_instance.project_set_get_column_stats(ids, names, limit=limit, categories=categories)
        print("The response of ProjectsApi->project_set_get_column_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_set_get_column_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| String containing the list of one or more id separated by non-num char. | 
 **names** | **str**| Coma-separated prefixed columns, on which stats are needed. | 
 **limit** | **int**| Only compute stats on this number of objects per category. | [optional] 
 **categories** | **str**| String containing the Categories, one or more id separated by non-num char. | [optional] 

### Return type

[**ProjectSetColumnStatsModel**](ProjectSetColumnStatsModel.md)

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

# **project_set_get_stats**
> List[ProjectTaxoStatsModel] project_set_get_stats(ids, taxa_ids=taxa_ids)

Project Set Get Stats

**Returns projects statistics**, i.e. used taxa and classification states.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_taxo_stats_model import ProjectTaxoStatsModel
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    ids = '1' # str | String containing the list of one or more project id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project.
    taxa_ids = '' # str | **If several taxa_ids are provided**, one stat record will be returned per requested taxa, if populated.    **If taxa_ids is all**, all valued taxa in the project(s) are returned. (optional) (default to '')

    try:
        # Project Set Get Stats
        api_response = api_instance.project_set_get_stats(ids, taxa_ids=taxa_ids)
        print("The response of ProjectsApi->project_set_get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_set_get_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| String containing the list of one or more project id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project. | 
 **taxa_ids** | **str**| **If several taxa_ids are provided**, one stat record will be returned per requested taxa, if populated.    **If taxa_ids is all**, all valued taxa in the project(s) are returned. | [optional] [default to &#39;&#39;]

### Return type

[**List[ProjectTaxoStatsModel]**](ProjectTaxoStatsModel.md)

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

# **project_set_get_user_stats**
> List[ProjectUserStatsModel] project_set_get_user_stats(ids)

Project Set Get User Stats

**Returns projects user statistics**, i.e. a summary of the work done by users in the required projects.  The returned values are a detail per project, so size of input list equals size of output list.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_user_stats_model import ProjectUserStatsModel
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    ids = '1' # str | String containing the list of one or more id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project.

    try:
        # Project Set Get User Stats
        api_response = api_instance.project_set_get_user_stats(ids)
        print("The response of ProjectsApi->project_set_get_user_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_set_get_user_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| String containing the list of one or more id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project. | 

### Return type

[**List[ProjectUserStatsModel]**](ProjectUserStatsModel.md)

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

# **project_stats**
> List[str] project_stats(project_id)

Project Stats

**Returns stats** for a project.  These stats will be returned as a list containing at index : - 0 : The **title** of the project, - 1 : A string containing all **freecols name and related column number**,  - 2 : **\"(0):\"** - 3 :  **\"Total: 0 values, dup 0 values\"**  Then for each acquisition a pair of strings will be added to the list : -  A string containing the **acquisition origin id** (the **number of objects for this acquisition**) : and then **small stats for an acquisition of a free column values inside** : [ min of values ; max of values ; distribution of the different values ; mode, i.e. freq of most frequent value] -  A string containing the **number of total values** and the **number of duplicates values** \"Total: ... values, dup ... values\"

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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.

    try:
        # Project Stats
        api_response = api_instance.project_stats(project_id)
        print("The response of ProjectsApi->project_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 

### Return type

**List[str]**

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

# **project_subset**
> SubsetRsp project_subset(project_id, subset_req)

Project Subset

**Subset a project into another one.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.subset_req import SubsetReq
from ecotaxa_py_client.models.subset_rsp import SubsetRsp
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    subset_req = ecotaxa_py_client.SubsetReq() # SubsetReq | 

    try:
        # Project Subset
        api_response = api_instance.project_subset(project_id, subset_req)
        print("The response of ProjectsApi->project_subset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_subset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **subset_req** | [**SubsetReq**](SubsetReq.md)|  | 

### Return type

[**SubsetRsp**](SubsetRsp.md)

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

# **search_projects**
> List[ProjectModel] search_projects(also_others=also_others, not_granted=not_granted, for_managing=for_managing, title_filter=title_filter, instrument_filter=instrument_filter, filter_subset=filter_subset, order_field=order_field, window_start=window_start, window_size=window_size)

Search Projects

Returns **projects which the current user has explicit permission to access, with search options.**  Note that, for performance reasons, in returned ProjectModels, field 'highest_rank' is NOT valued (unlike in simple query). The same information can be found in 'managers', 'annotators' and 'viewers' lists.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_model import ProjectModel
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    also_others = False # bool |  (optional) (default to False)
    not_granted = False # bool | Return projects on which the current user has _no permission_, but visible to him/her. (optional) (default to False)
    for_managing = False # bool | Return projects that can be written to (including erased) by the current user. (optional) (default to False)
    title_filter = '' # str | Use this pattern for matching returned projects names. (optional) (default to '')
    instrument_filter = '' # str | Only return projects where this instrument was used. (optional) (default to '')
    filter_subset = False # bool | Only return projects having 'subset' in their names. (optional) (default to False)
    order_field = 'instrument' # str | One of ['instrument', 'instrument_url', 'highest_right', 'projid', 'title', 'visible', 'status', 'objcount', 'pctvalidated', 'pctclassified', 'classifsettings', 'classiffieldlist', 'popoverfieldlist', 'comments', 'description', 'rf_models_used', 'cnn_network_id'] (optional)
    window_start = 0 # int | Skip `window_start` before returning data. (optional)
    window_size = 100 # int | Return only `window_size` lines. (optional)

    try:
        # Search Projects
        api_response = api_instance.search_projects(also_others=also_others, not_granted=not_granted, for_managing=for_managing, title_filter=title_filter, instrument_filter=instrument_filter, filter_subset=filter_subset, order_field=order_field, window_start=window_start, window_size=window_size)
        print("The response of ProjectsApi->search_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->search_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **also_others** | **bool**|  | [optional] [default to False]
 **not_granted** | **bool**| Return projects on which the current user has _no permission_, but visible to him/her. | [optional] [default to False]
 **for_managing** | **bool**| Return projects that can be written to (including erased) by the current user. | [optional] [default to False]
 **title_filter** | **str**| Use this pattern for matching returned projects names. | [optional] [default to &#39;&#39;]
 **instrument_filter** | **str**| Only return projects where this instrument was used. | [optional] [default to &#39;&#39;]
 **filter_subset** | **bool**| Only return projects having &#39;subset&#39; in their names. | [optional] [default to False]
 **order_field** | **str**| One of [&#39;instrument&#39;, &#39;instrument_url&#39;, &#39;highest_right&#39;, &#39;projid&#39;, &#39;title&#39;, &#39;visible&#39;, &#39;status&#39;, &#39;objcount&#39;, &#39;pctvalidated&#39;, &#39;pctclassified&#39;, &#39;classifsettings&#39;, &#39;classiffieldlist&#39;, &#39;popoverfieldlist&#39;, &#39;comments&#39;, &#39;description&#39;, &#39;rf_models_used&#39;, &#39;cnn_network_id&#39;] | [optional] 
 **window_start** | **int**| Skip &#x60;window_start&#x60; before returning data. | [optional] 
 **window_size** | **int**| Return only &#x60;window_size&#x60; lines. | [optional] 

### Return type

[**List[ProjectModel]**](ProjectModel.md)

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

# **set_project_predict_settings**
> object set_project_predict_settings(project_id, settings)

Set Project Predict Settings

**Update the project's prediction settings**, return **NULL upon success.**  🔒 Unlike during full project update above, which needs high permissions, this entry point is accessible to **project annotators**, as it mirrors the prediction privileges.

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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 4223 # int | Internal, numeric id of the project.
    settings = 'seltaxo=84963,59996,56545 baseproject=2562,2571' # str | The new prediction settings.

    try:
        # Set Project Predict Settings
        api_response = api_instance.set_project_predict_settings(project_id, settings)
        print("The response of ProjectsApi->set_project_predict_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->set_project_predict_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **settings** | **str**| The new prediction settings. | 

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

# **simple_import**
> SimpleImportRsp simple_import(project_id, dry_run, simple_import_req)

Simple Import

**Import images only**, with same metadata for all.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.simple_import_req import SimpleImportReq
from ecotaxa_py_client.models.simple_import_rsp import SimpleImportRsp
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    dry_run = true # bool | If set, then only a diagnostic of doability will be done. In this case, plain value check. If no dry_run, this call will create a background job.
    simple_import_req = ecotaxa_py_client.SimpleImportReq() # SimpleImportReq | 

    try:
        # Simple Import
        api_response = api_instance.simple_import(project_id, dry_run, simple_import_req)
        print("The response of ProjectsApi->simple_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->simple_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **dry_run** | **bool**| If set, then only a diagnostic of doability will be done. In this case, plain value check. If no dry_run, this call will create a background job. | 
 **simple_import_req** | [**SimpleImportReq**](SimpleImportReq.md)|  | 

### Return type

[**SimpleImportRsp**](SimpleImportRsp.md)

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

# **update_project**
> object update_project(project_id, project_model)

Update Project

**Update the project**, return **NULL upon success.**  Note that some fields will **NOT** be updated and simply ignored, e.g. *free_cols*.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_model import ProjectModel
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
    api_instance = ecotaxa_py_client.ProjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    project_model = ecotaxa_py_client.ProjectModel() # ProjectModel | 

    try:
        # Update Project
        api_response = api_instance.update_project(project_id, project_model)
        print("The response of ProjectsApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **project_model** | [**ProjectModel**](ProjectModel.md)|  | 

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


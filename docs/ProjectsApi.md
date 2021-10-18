# ecotaxa_cli_py.ProjectsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_projects_create_post**](ProjectsApi.md#create_project_projects_create_post) | **POST** /projects/create | Create Project
[**erase_project_projects_project_id_delete**](ProjectsApi.md#erase_project_projects_project_id_delete) | **DELETE** /projects/{project_id} | Erase Project
[**import_file_file_import_project_id_post**](ProjectsApi.md#import_file_file_import_project_id_post) | **POST** /file_import/{project_id} | Import File
[**project_check_projects_project_id_check_get**](ProjectsApi.md#project_check_projects_project_id_check_get) | **GET** /projects/{project_id}/check | Project Check
[**project_merge_projects_project_id_merge_post**](ProjectsApi.md#project_merge_projects_project_id_merge_post) | **POST** /projects/{project_id}/merge | Project Merge
[**project_query_projects_project_id_get**](ProjectsApi.md#project_query_projects_project_id_get) | **GET** /projects/{project_id} | Project Query
[**project_recompute_geography_projects_project_id_recompute_geo_post**](ProjectsApi.md#project_recompute_geography_projects_project_id_recompute_geo_post) | **POST** /projects/{project_id}/recompute_geo | Project Recompute Geography
[**project_set_get_stats_project_set_taxo_stats_get**](ProjectsApi.md#project_set_get_stats_project_set_taxo_stats_get) | **GET** /project_set/taxo_stats | Project Set Get Stats
[**project_set_get_user_stats_project_set_user_stats_get**](ProjectsApi.md#project_set_get_user_stats_project_set_user_stats_get) | **GET** /project_set/user_stats | Project Set Get User Stats
[**project_stats_projects_project_id_stats_get**](ProjectsApi.md#project_stats_projects_project_id_stats_get) | **GET** /projects/{project_id}/stats | Project Stats
[**project_subset_projects_project_id_subset_post**](ProjectsApi.md#project_subset_projects_project_id_subset_post) | **POST** /projects/{project_id}/subset | Project Subset
[**search_projects_projects_search_get**](ProjectsApi.md#search_projects_projects_search_get) | **GET** /projects/search | Search Projects
[**simple_import_simple_import_project_id_post**](ProjectsApi.md#simple_import_simple_import_project_id_post) | **POST** /simple_import/{project_id} | Simple Import
[**update_project_projects_project_id_put**](ProjectsApi.md#update_project_projects_project_id_put) | **PUT** /projects/{project_id} | Update Project


# **create_project_projects_create_post**
> int create_project_projects_create_post(create_project_req)

Create Project

**Create an empty project with only a title,** and **return its id**.  The project will be managed by current user.  🔒 The user has to be *app administrator* or *project creator*.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.create_project_req import CreateProjectReq
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
    api_instance = projects_api.ProjectsApi(api_client)
    create_project_req = CreateProjectReq(
        clone_of_id=2,
        title="My new project title",
        visible=True,
    ) # CreateProjectReq | 

    # example passing only required values which don't have defaults set
    try:
        # Create Project
        api_response = api_instance.create_project_projects_create_post(create_project_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_projects_create_post: %s\n" % e)
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

# **erase_project_projects_project_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type erase_project_projects_project_id_delete(project_id)

Erase Project

**Delete the project.**      Optionally, if \"only_objects\" is set, the project structure is kept, but emptied from any object, sample, acquisition and process.  Otherwise, no trace of the project will remain in the database.  **Returns** the number of  : **deleted objects**, 0, **deleated image rows** and **deleated image files**.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 
    only_objects = False # bool | If set, the project structure is kept, but emptied from any object, sample, acquisition and process. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Erase Project
        api_response = api_instance.erase_project_projects_project_id_delete(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->erase_project_projects_project_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Erase Project
        api_response = api_instance.erase_project_projects_project_id_delete(project_id, only_objects=only_objects)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->erase_project_projects_project_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **only_objects** | **bool**| If set, the project structure is kept, but emptied from any object, sample, acquisition and process. | [optional] if omitted the server will use the default value of False

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

# **import_file_file_import_project_id_post**
> ImportRsp import_file_file_import_project_id_post(project_id, import_req)

Import File

Validate or do a real import of an EcoTaxa archive or directory.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.import_req import ImportReq
from ecotaxa_cli_py.model.import_rsp import ImportRsp
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 
    import_req = ImportReq(
        source_path="source_path_example",
        taxo_mappings={
            "key": "key_example",
        },
        skip_loaded_files=False,
        skip_existing_objects=False,
        update_mode="",
    ) # ImportReq | 

    # example passing only required values which don't have defaults set
    try:
        # Import File
        api_response = api_instance.import_file_file_import_project_id_post(project_id, import_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->import_file_file_import_project_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
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

# **project_check_projects_project_id_check_get**
> [str] project_check_projects_project_id_check_get(project_id)

Project Check

**Check consistency of a project**.  With time and bugs, some consistency problems could be introduced in projects. This service aims at listing them.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Project Check
        api_response = api_instance.project_check_projects_project_id_check_get(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_check_projects_project_id_check_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |

### Return type

**[str]**

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

# **project_merge_projects_project_id_merge_post**
> MergeRsp project_merge_projects_project_id_merge_post(project_id)

Project Merge

**Merge another project into this one.**  It's more a phagocytosis than a merge, as the source will see all its objects gone and will be erased.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.merge_rsp import MergeRsp
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 
    source_project_id = 2 # int | Id of the other project. This source project will see all its objects gone and will be erased. (optional)
    dry_run = True # bool | If set, then only a diagnostic of doability will be done. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Project Merge
        api_response = api_instance.project_merge_projects_project_id_merge_post(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_merge_projects_project_id_merge_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Project Merge
        api_response = api_instance.project_merge_projects_project_id_merge_post(project_id, source_project_id=source_project_id, dry_run=dry_run)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_merge_projects_project_id_merge_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **source_project_id** | **int**| Id of the other project. This source project will see all its objects gone and will be erased. | [optional]
 **dry_run** | **bool**| If set, then only a diagnostic of doability will be done. | [optional]

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

# **project_query_projects_project_id_get**
> ProjectModel project_query_projects_project_id_get(project_id)

Project Query

**Returns project** if it exists for current user, eventually for managing it.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.project_model import ProjectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 
    for_managing = False # bool | For managing this project. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Project Query
        api_response = api_instance.project_query_projects_project_id_get(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_query_projects_project_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Project Query
        api_response = api_instance.project_query_projects_project_id_get(project_id, for_managing=for_managing)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_query_projects_project_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **for_managing** | **bool**| For managing this project. | [optional] if omitted the server will use the default value of False

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

# **project_recompute_geography_projects_project_id_recompute_geo_post**
> bool, date, datetime, dict, float, int, list, str, none_type project_recompute_geography_projects_project_id_recompute_geo_post(project_id)

Project Recompute Geography

**Recompute geography information** for all samples in project.  🔒 The user has to be *project manager*.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Project Recompute Geography
        api_response = api_instance.project_recompute_geography_projects_project_id_recompute_geo_post(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_recompute_geography_projects_project_id_recompute_geo_post: %s\n" % e)
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

# **project_set_get_stats_project_set_taxo_stats_get**
> [ProjectTaxoStatsModel] project_set_get_stats_project_set_taxo_stats_get()

Project Set Get Stats

**Returns projects statistics**, i.e. used taxa and classification states.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.project_taxo_stats_model import ProjectTaxoStatsModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    ids = "1" # str | String containing the list of one or more id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project. (optional)
    taxa_ids = "all" # str | **If several taxa_ids are provided**, one stat record will be returned per requested taxa, if populated.    **If taxa_ids is all**, all valued taxa in the project(s) are returned. (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Project Set Get Stats
        api_response = api_instance.project_set_get_stats_project_set_taxo_stats_get(ids=ids, taxa_ids=taxa_ids)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_set_get_stats_project_set_taxo_stats_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| String containing the list of one or more id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project. | [optional]
 **taxa_ids** | **str**| **If several taxa_ids are provided**, one stat record will be returned per requested taxa, if populated.    **If taxa_ids is all**, all valued taxa in the project(s) are returned. | [optional] if omitted the server will use the default value of ""

### Return type

[**[ProjectTaxoStatsModel]**](ProjectTaxoStatsModel.md)

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

# **project_set_get_user_stats_project_set_user_stats_get**
> [ProjectUserStatsModel] project_set_get_user_stats_project_set_user_stats_get()

Project Set Get User Stats

**Returns projects user statistics**, i.e. a summary of the work done by users in the required projects.   The returned values are a detail per project, so size of input list equals size of output list.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.project_user_stats_model import ProjectUserStatsModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    ids = "1" # str | String containing the list of one or more id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Project Set Get User Stats
        api_response = api_instance.project_set_get_user_stats_project_set_user_stats_get(ids=ids)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_set_get_user_stats_project_set_user_stats_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| String containing the list of one or more id separated by non-num char.     **If several ids are provided**, one stat record will be returned per project. | [optional]

### Return type

[**[ProjectUserStatsModel]**](ProjectUserStatsModel.md)

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

# **project_stats_projects_project_id_stats_get**
> bool, date, datetime, dict, float, int, list, str, none_type project_stats_projects_project_id_stats_get(project_id)

Project Stats

Check consistency of a project.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Project Stats
        api_response = api_instance.project_stats_projects_project_id_stats_get(project_id)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_stats_projects_project_id_stats_get: %s\n" % e)
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

# **project_subset_projects_project_id_subset_post**
> SubsetRsp project_subset_projects_project_id_subset_post(project_id, subset_req)

Project Subset

**Subset a project into another one.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.subset_req import SubsetReq
from ecotaxa_cli_py.model.subset_rsp import SubsetRsp
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 
    subset_req = SubsetReq(
        filters={
            "key": "key_example",
        },
        dest_prj_id=22,
        group_type=,
        limit_type=,
        limit_value=10.0,
        do_images=True,
    ) # SubsetReq | 

    # example passing only required values which don't have defaults set
    try:
        # Project Subset
        api_response = api_instance.project_subset_projects_project_id_subset_post(project_id, subset_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->project_subset_projects_project_id_subset_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
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

# **search_projects_projects_search_get**
> [ProjectModel] search_projects_projects_search_get()

Search Projects

Returns **projects which the current user has explicit permission to access, with search options.**  Note that, for performance reasons, in returned ProjectModels, field 'highest_rank' is NOT valued (unlike in simple query). The same information can be found in 'managers', 'annotators' and 'viewers' lists.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.project_model import ProjectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    also_others = False # bool |  (optional) if omitted the server will use the default value of False
    not_granted = False # bool | Return projects on which the current user has _no permission_, but visible to him/her (optional) if omitted the server will use the default value of False
    for_managing = False # bool | Return projects that can be written to (including erased) by the current user (optional) if omitted the server will use the default value of False
    title_filter = "Tara" # str | Use this pattern for matching returned projects names (optional) if omitted the server will use the default value of ""
    instrument_filter = "uvp5" # str | Only return projects where this instrument was used (optional) if omitted the server will use the default value of ""
    filter_subset = True # bool | Only return projects having 'subset' in their names (optional) if omitted the server will use the default value of False
    order_field = "instrument" # str | One of ['instrument', 'highest_right', 'license', 'projid', 'title', 'visible', 'status', 'objcount', 'pctvalidated', 'pctclassified', 'classifsettings', 'classiffieldlist', 'popoverfieldlist', 'comments', 'projtype', 'rf_models_used', 'cnn_network_id'] (optional)
    window_start = 0 # int | Skip `window_start` before returning data (optional)
    window_size = 100 # int | Return only `window_size` lines (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Projects
        api_response = api_instance.search_projects_projects_search_get(also_others=also_others, not_granted=not_granted, for_managing=for_managing, title_filter=title_filter, instrument_filter=instrument_filter, filter_subset=filter_subset, order_field=order_field, window_start=window_start, window_size=window_size)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->search_projects_projects_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **also_others** | **bool**|  | [optional] if omitted the server will use the default value of False
 **not_granted** | **bool**| Return projects on which the current user has _no permission_, but visible to him/her | [optional] if omitted the server will use the default value of False
 **for_managing** | **bool**| Return projects that can be written to (including erased) by the current user | [optional] if omitted the server will use the default value of False
 **title_filter** | **str**| Use this pattern for matching returned projects names | [optional] if omitted the server will use the default value of ""
 **instrument_filter** | **str**| Only return projects where this instrument was used | [optional] if omitted the server will use the default value of ""
 **filter_subset** | **bool**| Only return projects having &#39;subset&#39; in their names | [optional] if omitted the server will use the default value of False
 **order_field** | **str**| One of [&#39;instrument&#39;, &#39;highest_right&#39;, &#39;license&#39;, &#39;projid&#39;, &#39;title&#39;, &#39;visible&#39;, &#39;status&#39;, &#39;objcount&#39;, &#39;pctvalidated&#39;, &#39;pctclassified&#39;, &#39;classifsettings&#39;, &#39;classiffieldlist&#39;, &#39;popoverfieldlist&#39;, &#39;comments&#39;, &#39;projtype&#39;, &#39;rf_models_used&#39;, &#39;cnn_network_id&#39;] | [optional]
 **window_start** | **int**| Skip &#x60;window_start&#x60; before returning data | [optional]
 **window_size** | **int**| Return only &#x60;window_size&#x60; lines | [optional]

### Return type

[**[ProjectModel]**](ProjectModel.md)

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

# **simple_import_simple_import_project_id_post**
> SimpleImportRsp simple_import_simple_import_project_id_post(project_id, dry_run, simple_import_req)

Simple Import

Import images only, with same metadata for all. - param `dry_run`: If set, then _only_ a diagnostic of do-ability will be done.     In this case, plain value check. If no dry_run, this call will create a background job.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.simple_import_rsp import SimpleImportRsp
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.simple_import_req import SimpleImportReq
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 
    dry_run = True # bool | 
    simple_import_req = SimpleImportReq(
        source_path="source_path_example",
        values={
            "key": "key_example",
        },
        possible_values=["imgdate","imgtime","latitude","longitude","depthmin","depthmax","taxolb","userlb","status"],
    ) # SimpleImportReq | 

    # example passing only required values which don't have defaults set
    try:
        # Simple Import
        api_response = api_instance.simple_import_simple_import_project_id_post(project_id, dry_run, simple_import_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->simple_import_simple_import_project_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **dry_run** | **bool**|  |
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

# **update_project_projects_project_id_put**
> bool, date, datetime, dict, float, int, list, str, none_type update_project_projects_project_id_put(project_id, project_model)

Update Project

**Update the project**.  Note that some fields will **NOT** be updated and simply ignored, e.g. *free_cols*.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import projects_api
from ecotaxa_cli_py.model.project_model import ProjectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = 1 # int | 
    project_model = ProjectModel(
        obj_free_cols={
            "key": "key_example",
        },
        sample_free_cols={
            "key": "key_example",
        },
        acquisition_free_cols={
            "key": "key_example",
        },
        process_free_cols={
            "key": "key_example",
        },
        init_classif_list=[5,11493,11498,11509],
        managers=[
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
        annotators=[
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
        viewers=[
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
        instrument="zooscan",
        contact=,
        highest_right="View",
        license="license_example",
        projid=4824,
        title="MyProject",
        visible=False,
        status="Annotate",
        objcount=32292.0,
        pctvalidated=0.015483711135885049,
        pctclassified=100.0,
        classifsettings='''baseproject=1602
critvar=%area,angle,area,area_exc,bx,by,cdexc,centroids,circ.,circex,convarea,convperim,cv,elongation,esd,fcons,feret,feretareaexc,fractal,height,histcum1,histcum2,histcum3,intden,kurt,lat_end,lon_end,major,max,mean,meanpos,median,min,minor,mode,nb1,nb2,perim.,perimareaexc,perimferet,perimmajor,range,skelarea,skew,slope,sr,stddev,symetrieh,symetriehc,symetriev,symetrievc,thickr,width,x,xm,xstart,y,ym,ystart
posttaxomapping=
seltaxo=45074,84963,61990,13333,82399,61973,62005,25930,25932,61996,78426,81941,11514,85076,85061,30815,85185,92230,85079,84993,25824,85115,85004,26525,25944,11509,26524,92112,84976,25942,84980,85078,78418,84977,85060,61993,61991,85069,81871,74144,11758,72431,13381,11518,5,18758,85117,92042,84968,84997,87826,92236,92237,92039,84989,85193,83281,78412,92239,71617,81977,45071,12865,85044,81940,85067,12908,85116,56693,85008,92139,92068
usemodel_foldername=testln1''',
        classiffieldlist='''depth_min=depth_min
depth_max=depth_max
area=area [pixel]
mean=mean [0-255]
fractal=fractal
major=major [pixel]
symetrieh=symetrieh
circ.=circ
feret = Feret [pixel]''',
        popoverfieldlist='''depth_min=depth_min
depth_max=depth_max
area=area [pixel]
mean=mean [0-255]
fractal=fractal
major=major [pixel]
symetrieh=symetrieh
circ.=circ
feret = Feret [pixel]''',
        comments="",
        projtype="",
        rf_models_used="",
        cnn_network_id="SCN_zooscan_group1",
    ) # ProjectModel | 

    # example passing only required values which don't have defaults set
    try:
        # Update Project
        api_response = api_instance.update_project_projects_project_id_put(project_id, project_model)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling ProjectsApi->update_project_projects_project_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **project_model** | [**ProjectModel**](ProjectModel.md)|  |

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


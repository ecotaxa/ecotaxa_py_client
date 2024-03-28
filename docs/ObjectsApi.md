# ecotaxa_py_client.ObjectsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classify_auto_object_set**](ObjectsApi.md#classify_auto_object_set) | **POST** /object_set/classify_auto | Classify Auto Object Set
[**classify_object_set**](ObjectsApi.md#classify_object_set) | **POST** /object_set/classify | Classify Object Set
[**erase_object_set**](ObjectsApi.md#erase_object_set) | **DELETE** /object_set/ | Erase Object Set
[**export_object_set**](ObjectsApi.md#export_object_set) | **POST** /object_set/export | Export Object Set
[**export_object_set_backup**](ObjectsApi.md#export_object_set_backup) | **POST** /object_set/export/backup | Export Object Set Backup
[**export_object_set_general**](ObjectsApi.md#export_object_set_general) | **POST** /object_set/export/general | Export Object Set General
[**export_object_set_summary**](ObjectsApi.md#export_object_set_summary) | **POST** /object_set/export/summary | Export Object Set Summary
[**get_object_set**](ObjectsApi.md#get_object_set) | **POST** /object_set/{project_id}/query | Get Object Set
[**get_object_set_summary**](ObjectsApi.md#get_object_set_summary) | **POST** /object_set/{project_id}/summary | Get Object Set Summary
[**predict_object_set**](ObjectsApi.md#predict_object_set) | **POST** /object_set/predict | Predict Object Set
[**query_object_set_parents**](ObjectsApi.md#query_object_set_parents) | **POST** /object_set/parents | Query Object Set Parents
[**reclassify_object_set**](ObjectsApi.md#reclassify_object_set) | **POST** /object_set/{project_id}/reclassify | Reclassify Object Set
[**reset_object_set_to_predicted**](ObjectsApi.md#reset_object_set_to_predicted) | **POST** /object_set/{project_id}/reset_to_predicted | Reset Object Set To Predicted
[**revert_object_set_to_history**](ObjectsApi.md#revert_object_set_to_history) | **POST** /object_set/{project_id}/revert_to_history | Revert Object Set To History
[**update_object_set**](ObjectsApi.md#update_object_set) | **POST** /object_set/update | Update Object Set


# **classify_auto_object_set**
> int classify_auto_object_set(classify_auto_req)

Classify Auto Object Set

**Set automatic classification** of a set of objects.  **Returns the number of updated entities.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.classify_auto_req import ClassifyAutoReq
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    classify_auto_req = ecotaxa_py_client.ClassifyAutoReq() # ClassifyAutoReq | 

    try:
        # Classify Auto Object Set
        api_response = api_instance.classify_auto_object_set(classify_auto_req)
        print("The response of ObjectsApi->classify_auto_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->classify_auto_object_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classify_auto_req** | [**ClassifyAutoReq**](ClassifyAutoReq.md)|  | 

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

# **classify_object_set**
> int classify_object_set(classify_req)

Classify Object Set

**Change classification and/or qualification for a set of objects.**  **Returns the number of updated entities.**  🔒 Current user needs at *least Annotate* right on all projects of specified objects.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.classify_req import ClassifyReq
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    classify_req = ecotaxa_py_client.ClassifyReq() # ClassifyReq | 

    try:
        # Classify Object Set
        api_response = api_instance.classify_object_set(classify_req)
        print("The response of ObjectsApi->classify_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->classify_object_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classify_req** | [**ClassifyReq**](ClassifyReq.md)|  | 

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

# **erase_object_set**
> object erase_object_set(request_body)

Erase Object Set

**Delete the objects with given object ids.**  **Returns** the number of  : **deleted objects**, 0, **deleated image rows** and **deleated image files**.  🔒 Current user needs *Manage* right on all projects of specified objects.

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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    request_body = [634509,6234516,976544] # List[int] | 

    try:
        # Erase Object Set
        api_response = api_instance.erase_object_set(request_body)
        print("The response of ObjectsApi->erase_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->erase_object_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

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

# **export_object_set**
> ExportRsp export_object_set(body_export_object_set_object_set_export_post)

Export Object Set

⚠️ Deprecated, see general, summary and backup exports for alternatives.  Start an export job for the given object set and options.  🔒 Current user needs *at least Read* right on the requested project.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.body_export_object_set_object_set_export_post import BodyExportObjectSetObjectSetExportPost
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    body_export_object_set_object_set_export_post = ecotaxa_py_client.BodyExportObjectSetObjectSetExportPost() # BodyExportObjectSetObjectSetExportPost | 

    try:
        # Export Object Set
        api_response = api_instance.export_object_set(body_export_object_set_object_set_export_post)
        print("The response of ObjectsApi->export_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->export_object_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_export_object_set_object_set_export_post** | [**BodyExportObjectSetObjectSetExportPost**](BodyExportObjectSetObjectSetExportPost.md)|  | 

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

# **export_object_set_backup**
> ExportRsp export_object_set_backup(body_export_object_set_backup_object_set_export_backup_post)

Export Object Set Backup

Start a backup export job for the given object set and options. If filters are empty, the produced zip will contain the full project.  🔒 Current user needs *at least Read* right on the requested project.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.body_export_object_set_backup_object_set_export_backup_post import BodyExportObjectSetBackupObjectSetExportBackupPost
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    body_export_object_set_backup_object_set_export_backup_post = ecotaxa_py_client.BodyExportObjectSetBackupObjectSetExportBackupPost() # BodyExportObjectSetBackupObjectSetExportBackupPost | 

    try:
        # Export Object Set Backup
        api_response = api_instance.export_object_set_backup(body_export_object_set_backup_object_set_export_backup_post)
        print("The response of ObjectsApi->export_object_set_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->export_object_set_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_export_object_set_backup_object_set_export_backup_post** | [**BodyExportObjectSetBackupObjectSetExportBackupPost**](BodyExportObjectSetBackupObjectSetExportBackupPost.md)|  | 

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

# **export_object_set_general**
> ExportRsp export_object_set_general(body_export_object_set_general_object_set_export_general_post)

Export Object Set General

Start a general-purpose export job for the given object set and options.  🔒 Current user needs *at least Read* right on the requested project.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.body_export_object_set_general_object_set_export_general_post import BodyExportObjectSetGeneralObjectSetExportGeneralPost
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    body_export_object_set_general_object_set_export_general_post = ecotaxa_py_client.BodyExportObjectSetGeneralObjectSetExportGeneralPost() # BodyExportObjectSetGeneralObjectSetExportGeneralPost | 

    try:
        # Export Object Set General
        api_response = api_instance.export_object_set_general(body_export_object_set_general_object_set_export_general_post)
        print("The response of ObjectsApi->export_object_set_general:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->export_object_set_general: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_export_object_set_general_object_set_export_general_post** | [**BodyExportObjectSetGeneralObjectSetExportGeneralPost**](BodyExportObjectSetGeneralObjectSetExportGeneralPost.md)|  | 

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

# **export_object_set_summary**
> ExportRsp export_object_set_summary(body_export_object_set_summary_object_set_export_summary_post)

Export Object Set Summary

Start a summary export job for the given object set and options.  🔒 Current user needs *at least Read* right on the requested project.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.body_export_object_set_summary_object_set_export_summary_post import BodyExportObjectSetSummaryObjectSetExportSummaryPost
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    body_export_object_set_summary_object_set_export_summary_post = ecotaxa_py_client.BodyExportObjectSetSummaryObjectSetExportSummaryPost() # BodyExportObjectSetSummaryObjectSetExportSummaryPost | 

    try:
        # Export Object Set Summary
        api_response = api_instance.export_object_set_summary(body_export_object_set_summary_object_set_export_summary_post)
        print("The response of ObjectsApi->export_object_set_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->export_object_set_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_export_object_set_summary_object_set_export_summary_post** | [**BodyExportObjectSetSummaryObjectSetExportSummaryPost**](BodyExportObjectSetSummaryObjectSetExportSummaryPost.md)|  | 

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

# **get_object_set**
> ObjectSetQueryRsp get_object_set(project_id, project_filters, fields=fields, order_field=order_field, window_start=window_start, window_size=window_size)

Get Object Set

Returns **filtered object Ids** for the given project.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.object_set_query_rsp import ObjectSetQueryRsp
from ecotaxa_py_client.models.project_filters import ProjectFilters
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    project_filters = ecotaxa_py_client.ProjectFilters() # ProjectFilters | 
    fields = 'obj.longitude,fre.feret' # str |   Specify the needed object (and ancillary entities) fields.  It follows the naming convention 'prefix.field' : Prefix is either 'obj' for main object, 'fre' for free fields, 'img' for the visible image.  The column obj.imgcount contains the total count of images for the object.  Use a comma to separate fields.  💡 More help :  You can get the field labels by parsing the classiffieldlist returned by a call to https://ecotaxa.obs-vlfr.fr/api/docs#/projects/project_query_projects__project_id__get.  **Note that the following fields must be prefixed with the header \"obj.\"** (for example → obj.orig_id):  acquisid classif_auto_id, classif_auto_score, classif_auto_when, classif_crossvalidation_id, classif_id, classif_qual, classif_who, classif_when, complement_info, depth_max, depth_min, latitude, longitude, objdate, object_link, objid, objtime, orig_id, random_value, similarity, sunpos.  **Note that the following fields must be prefixed with the header \"img.\"** (for example → img.file_name):  file_name, height, imgid, imgrank, file_name, orig, objid, file_name thumb_file_name, thumb_height, thumb_width, width.  **Note that the following fields must be prefixed with the header \"txo.\"** (for example → txo.display_name):  creation_datetime, creator_email, display_name, id, id_instance, id_source, lastupdate_datetime, name, nbrobj, nbrobjcum, parent_id, rename_to source_desc, source_url, taxostatus, taxotype.  **All other fields must be prefixed by the header \"fre.\"** (for example → fre.circ.).                     (optional)
    order_field = 'obj.longitude' # str | Order the result using given field. If prefixed with \"-\" then it will be reversed. (optional)
    window_start = 10 # int |  Allows to return only a slice of the result, by skipping window_start objects before returning data. If no **unique order** is specified, the result can vary for same call and conditions. (optional)
    window_size = 100 # int |  Allows to return only a slice of the result, by returning a _maximum_ of window_size lines. If no **unique order** is specified, the result can vary for same call and conditions. (optional)

    try:
        # Get Object Set
        api_response = api_instance.get_object_set(project_id, project_filters, fields=fields, order_field=order_field, window_start=window_start, window_size=window_size)
        print("The response of ObjectsApi->get_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_object_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **project_filters** | [**ProjectFilters**](ProjectFilters.md)|  | 
 **fields** | **str**|   Specify the needed object (and ancillary entities) fields.  It follows the naming convention &#39;prefix.field&#39; : Prefix is either &#39;obj&#39; for main object, &#39;fre&#39; for free fields, &#39;img&#39; for the visible image.  The column obj.imgcount contains the total count of images for the object.  Use a comma to separate fields.  💡 More help :  You can get the field labels by parsing the classiffieldlist returned by a call to https://ecotaxa.obs-vlfr.fr/api/docs#/projects/project_query_projects__project_id__get.  **Note that the following fields must be prefixed with the header \&quot;obj.\&quot;** (for example → obj.orig_id):  acquisid classif_auto_id, classif_auto_score, classif_auto_when, classif_crossvalidation_id, classif_id, classif_qual, classif_who, classif_when, complement_info, depth_max, depth_min, latitude, longitude, objdate, object_link, objid, objtime, orig_id, random_value, similarity, sunpos.  **Note that the following fields must be prefixed with the header \&quot;img.\&quot;** (for example → img.file_name):  file_name, height, imgid, imgrank, file_name, orig, objid, file_name thumb_file_name, thumb_height, thumb_width, width.  **Note that the following fields must be prefixed with the header \&quot;txo.\&quot;** (for example → txo.display_name):  creation_datetime, creator_email, display_name, id, id_instance, id_source, lastupdate_datetime, name, nbrobj, nbrobjcum, parent_id, rename_to source_desc, source_url, taxostatus, taxotype.  **All other fields must be prefixed by the header \&quot;fre.\&quot;** (for example → fre.circ.).                     | [optional] 
 **order_field** | **str**| Order the result using given field. If prefixed with \&quot;-\&quot; then it will be reversed. | [optional] 
 **window_start** | **int**|  Allows to return only a slice of the result, by skipping window_start objects before returning data. If no **unique order** is specified, the result can vary for same call and conditions. | [optional] 
 **window_size** | **int**|  Allows to return only a slice of the result, by returning a _maximum_ of window_size lines. If no **unique order** is specified, the result can vary for same call and conditions. | [optional] 

### Return type

[**ObjectSetQueryRsp**](ObjectSetQueryRsp.md)

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

# **get_object_set_summary**
> ObjectSetSummaryRsp get_object_set_summary(project_id, only_total, project_filters)

Get Object Set Summary

For the given project, with given filters, **return the classification summary**.  i.e.:  - Total number of objects  And optionally  - Number of Validated ones - Number of Dubious ones - Number of Predicted ones

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.object_set_summary_rsp import ObjectSetSummaryRsp
from ecotaxa_py_client.models.project_filters import ProjectFilters
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    only_total = True # bool | If True, returns only the **Total number of objects**. Else returns also the **Number of validated ones**, the **number of Dubious ones** and the number of **predicted ones**.
    project_filters = ecotaxa_py_client.ProjectFilters() # ProjectFilters | 

    try:
        # Get Object Set Summary
        api_response = api_instance.get_object_set_summary(project_id, only_total, project_filters)
        print("The response of ObjectsApi->get_object_set_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_object_set_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **only_total** | **bool**| If True, returns only the **Total number of objects**. Else returns also the **Number of validated ones**, the **number of Dubious ones** and the number of **predicted ones**. | 
 **project_filters** | [**ProjectFilters**](ProjectFilters.md)|  | 

### Return type

[**ObjectSetSummaryRsp**](ObjectSetSummaryRsp.md)

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

# **predict_object_set**
> PredictionRsp predict_object_set(body_predict_object_set_object_set_predict_post)

Predict Object Set

**Start a prediction** AKA automatic classification for the given object set and options.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.body_predict_object_set_object_set_predict_post import BodyPredictObjectSetObjectSetPredictPost
from ecotaxa_py_client.models.prediction_rsp import PredictionRsp
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    body_predict_object_set_object_set_predict_post = ecotaxa_py_client.BodyPredictObjectSetObjectSetPredictPost() # BodyPredictObjectSetObjectSetPredictPost | 

    try:
        # Predict Object Set
        api_response = api_instance.predict_object_set(body_predict_object_set_object_set_predict_post)
        print("The response of ObjectsApi->predict_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->predict_object_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_predict_object_set_object_set_predict_post** | [**BodyPredictObjectSetObjectSetPredictPost**](BodyPredictObjectSetObjectSetPredictPost.md)|  | 

### Return type

[**PredictionRsp**](PredictionRsp.md)

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

# **query_object_set_parents**
> ObjectSetQueryRsp query_object_set_parents(request_body)

Query Object Set Parents

**Return object ids, with parent ones and projects** for the objects in given list.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.object_set_query_rsp import ObjectSetQueryRsp
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    request_body = [634509,6234516,976544] # List[int] | 

    try:
        # Query Object Set Parents
        api_response = api_instance.query_object_set_parents(request_body)
        print("The response of ObjectsApi->query_object_set_parents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->query_object_set_parents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

[**ObjectSetQueryRsp**](ObjectSetQueryRsp.md)

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

# **reclassify_object_set**
> int reclassify_object_set(project_id, forced_id, reason, project_filters)

Reclassify Object Set

Regardless of present classification or state, **set the new classification for this object set.**  If the filter designates \"all with given classification\", add a TaxonomyChangeLog entry.  **Returns the number of affected objects.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_filters import ProjectFilters
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    forced_id = 23025 # int | The new classification Id.
    reason = 'W' # str | The reason of this new classification.
    project_filters = ecotaxa_py_client.ProjectFilters() # ProjectFilters | 

    try:
        # Reclassify Object Set
        api_response = api_instance.reclassify_object_set(project_id, forced_id, reason, project_filters)
        print("The response of ObjectsApi->reclassify_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->reclassify_object_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **forced_id** | **int**| The new classification Id. | 
 **reason** | **str**| The reason of this new classification. | 
 **project_filters** | [**ProjectFilters**](ProjectFilters.md)|  | 

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

# **reset_object_set_to_predicted**
> object reset_object_set_to_predicted(project_id, project_filters)

Reset Object Set To Predicted

**Reset to Predicted** all objects for the given project with the filters.  Return **NULL upon success.**

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.project_filters import ProjectFilters
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    project_filters = ecotaxa_py_client.ProjectFilters() # ProjectFilters | 

    try:
        # Reset Object Set To Predicted
        api_response = api_instance.reset_object_set_to_predicted(project_id, project_filters)
        print("The response of ObjectsApi->reset_object_set_to_predicted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->reset_object_set_to_predicted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **project_filters** | [**ProjectFilters**](ProjectFilters.md)|  | 

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

# **revert_object_set_to_history**
> ObjectSetRevertToHistoryRsp revert_object_set_to_history(project_id, dry_run, project_filters, target=target)

Revert Object Set To History

**Revert all objects for the given project**, with the filters, to the target.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.object_set_revert_to_history_rsp import ObjectSetRevertToHistoryRsp
from ecotaxa_py_client.models.project_filters import ProjectFilters
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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    project_id = 1 # int | Internal, numeric id of the project.
    dry_run = false # bool | If set, then no real write but consequences of the revert will be replied.
    project_filters = ecotaxa_py_client.ProjectFilters() # ProjectFilters | 
    target = 465 # int | Use null/None for reverting using the last annotation from anyone, or a user id for the last annotation from this user. (optional)

    try:
        # Revert Object Set To History
        api_response = api_instance.revert_object_set_to_history(project_id, dry_run, project_filters, target=target)
        print("The response of ObjectsApi->revert_object_set_to_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->revert_object_set_to_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Internal, numeric id of the project. | 
 **dry_run** | **bool**| If set, then no real write but consequences of the revert will be replied. | 
 **project_filters** | [**ProjectFilters**](ProjectFilters.md)|  | 
 **target** | **int**| Use null/None for reverting using the last annotation from anyone, or a user id for the last annotation from this user. | [optional] 

### Return type

[**ObjectSetRevertToHistoryRsp**](ObjectSetRevertToHistoryRsp.md)

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

# **update_object_set**
> int update_object_set(bulk_update_req)

Update Object Set

Do the required **update for each objects in the set.**  **Returns the number of updated entities.**  🔒 Current user needs *Manage* right on all projects of specified objects.

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
    api_instance = ecotaxa_py_client.ObjectsApi(api_client)
    bulk_update_req = ecotaxa_py_client.BulkUpdateReq() # BulkUpdateReq | 

    try:
        # Update Object Set
        api_response = api_instance.update_object_set(bulk_update_req)
        print("The response of ObjectsApi->update_object_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->update_object_set: %s\n" % e)
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


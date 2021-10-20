# ecotaxa_cli_py.ObjectsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classify_auto_object_set_object_set_classify_auto_post**](ObjectsApi.md#classify_auto_object_set_object_set_classify_auto_post) | **POST** /object_set/classify_auto | Classify Auto Object Set
[**classify_object_set_object_set_classify_post**](ObjectsApi.md#classify_object_set_object_set_classify_post) | **POST** /object_set/classify | Classify Object Set
[**erase_object_set_object_set_delete**](ObjectsApi.md#erase_object_set_object_set_delete) | **DELETE** /object_set/ | Erase Object Set
[**export_object_set_object_set_export_post**](ObjectsApi.md#export_object_set_object_set_export_post) | **POST** /object_set/export | Export Object Set
[**get_object_set_object_set_project_id_query_post**](ObjectsApi.md#get_object_set_object_set_project_id_query_post) | **POST** /object_set/{project_id}/query | Get Object Set
[**get_object_set_summary_object_set_project_id_summary_post**](ObjectsApi.md#get_object_set_summary_object_set_project_id_summary_post) | **POST** /object_set/{project_id}/summary | Get Object Set Summary
[**query_object_set_parents_object_set_parents_post**](ObjectsApi.md#query_object_set_parents_object_set_parents_post) | **POST** /object_set/parents | Query Object Set Parents
[**reclassify_object_set_object_set_project_id_reclassify_post**](ObjectsApi.md#reclassify_object_set_object_set_project_id_reclassify_post) | **POST** /object_set/{project_id}/reclassify | Reclassify Object Set
[**reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post**](ObjectsApi.md#reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post) | **POST** /object_set/{project_id}/reset_to_predicted | Reset Object Set To Predicted
[**revert_object_set_to_history_object_set_project_id_revert_to_history_post**](ObjectsApi.md#revert_object_set_to_history_object_set_project_id_revert_to_history_post) | **POST** /object_set/{project_id}/revert_to_history | Revert Object Set To History
[**update_object_set_object_set_update_post**](ObjectsApi.md#update_object_set_object_set_update_post) | **POST** /object_set/update | Update Object Set


# **classify_auto_object_set_object_set_classify_auto_post**
> object classify_auto_object_set_object_set_classify_auto_post(classify_auto_req)

Classify Auto Object Set

Set automatic classification of a set of objects.  - `params`: None, all is in the Request body.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    classify_auto_req = ecotaxa_cli_py.ClassifyAutoReq() # ClassifyAutoReq | 

    try:
        # Classify Auto Object Set
        api_response = api_instance.classify_auto_object_set_object_set_classify_auto_post(classify_auto_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->classify_auto_object_set_object_set_classify_auto_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classify_auto_req** | [**ClassifyAutoReq**](ClassifyAutoReq.md)|  | 

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

# **classify_object_set_object_set_classify_post**
> object classify_object_set_object_set_classify_post(classify_req)

Classify Object Set

Change classification and/or qualification for a set of objects. Current user needs at least Annotate right on all projects of specified objects.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    classify_req = ecotaxa_cli_py.ClassifyReq() # ClassifyReq | 

    try:
        # Classify Object Set
        api_response = api_instance.classify_object_set_object_set_classify_post(classify_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->classify_object_set_object_set_classify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classify_req** | [**ClassifyReq**](ClassifyReq.md)|  | 

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

# **erase_object_set_object_set_delete**
> object erase_object_set_object_set_delete(request_body)

Erase Object Set

Delete the objects with given object ids. Current user needs Manage right on all projects of specified objects.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    request_body = [56] # list[int] | 

    try:
        # Erase Object Set
        api_response = api_instance.erase_object_set_object_set_delete(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->erase_object_set_object_set_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)|  | 

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

# **export_object_set_object_set_export_post**
> ExportRsp export_object_set_object_set_export_post(body_export_object_set_object_set_export_post)

Export Object Set

Start an export job for the given object set and options.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    body_export_object_set_object_set_export_post = ecotaxa_cli_py.BodyExportObjectSetObjectSetExportPost() # BodyExportObjectSetObjectSetExportPost | 

    try:
        # Export Object Set
        api_response = api_instance.export_object_set_object_set_export_post(body_export_object_set_object_set_export_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->export_object_set_object_set_export_post: %s\n" % e)
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

# **get_object_set_object_set_project_id_query_post**
> ObjectSetQueryRsp get_object_set_object_set_project_id_query_post(project_id, project_filters, fields=fields, order_field=order_field, window_start=window_start, window_size=window_size)

Get Object Set

Return object ids for the given project with the filters.  Optionally:      - fields will specify the needed object (and ancilliary entities) fields     - order_field will order the result using given field, If prefixed with \"-\" then it will be reversed.     - window_start & window_size allows to return only a slice of the result.  Fields follow the naming convention: `prefix.field`.     Prefix is either 'obj' for main object, 'fre' for free fields, 'img' for the visible image.     Use a comma to separate fields.     - Column obj.imgcount contains the total count of images for the object.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    project_id = 56 # int | 
project_filters = ecotaxa_cli_py.ProjectFilters() # ProjectFilters | 
fields = 'fields_example' # str |  (optional)
order_field = 'order_field_example' # str |  (optional)
window_start = 56 # int |  (optional)
window_size = 56 # int |  (optional)

    try:
        # Get Object Set
        api_response = api_instance.get_object_set_object_set_project_id_query_post(project_id, project_filters, fields=fields, order_field=order_field, window_start=window_start, window_size=window_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->get_object_set_object_set_project_id_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_filters** | [**ProjectFilters**](ProjectFilters.md)|  | 
 **fields** | **str**|  | [optional] 
 **order_field** | **str**|  | [optional] 
 **window_start** | **int**|  | [optional] 
 **window_size** | **int**|  | [optional] 

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

# **get_object_set_summary_object_set_project_id_summary_post**
> ObjectSetSummaryRsp get_object_set_summary_object_set_project_id_summary_post(project_id, only_total, project_filters)

Get Object Set Summary

For the given project, with given filters, return the classification summary, i.e.:     - Total number of objects Also if 'only_total' is not set:     - Number of Validated ones     - Number of Dubious ones     - Number of Predicted ones

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    project_id = 56 # int | 
only_total = True # bool | 
project_filters = ecotaxa_cli_py.ProjectFilters() # ProjectFilters | 

    try:
        # Get Object Set Summary
        api_response = api_instance.get_object_set_summary_object_set_project_id_summary_post(project_id, only_total, project_filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->get_object_set_summary_object_set_project_id_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **only_total** | **bool**|  | 
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

# **query_object_set_parents_object_set_parents_post**
> ObjectSetQueryRsp query_object_set_parents_object_set_parents_post(request_body)

Query Object Set Parents

Return object ids, with parent ones and projects for the objects in given list.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    request_body = [56] # list[int] | 

    try:
        # Query Object Set Parents
        api_response = api_instance.query_object_set_parents_object_set_parents_post(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->query_object_set_parents_object_set_parents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)|  | 

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

# **reclassify_object_set_object_set_project_id_reclassify_post**
> object reclassify_object_set_object_set_project_id_reclassify_post(project_id, forced_id, reason, project_filters)

Reclassify Object Set

Regardless of present classification or state, set the new classification for this object set. If the filter designates \"all with given classification\", add a TaxonomyChangeLog entry. :returns the number of affected objects.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    project_id = 56 # int | 
forced_id = 56 # int | 
reason = 'reason_example' # str | 
project_filters = ecotaxa_cli_py.ProjectFilters() # ProjectFilters | 

    try:
        # Reclassify Object Set
        api_response = api_instance.reclassify_object_set_object_set_project_id_reclassify_post(project_id, forced_id, reason, project_filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->reclassify_object_set_object_set_project_id_reclassify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **forced_id** | **int**|  | 
 **reason** | **str**|  | 
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

# **reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post**
> object reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post(project_id, project_filters)

Reset Object Set To Predicted

Reset to Predicted all objects for the given project with the filters.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    project_id = 56 # int | 
project_filters = ecotaxa_cli_py.ProjectFilters() # ProjectFilters | 

    try:
        # Reset Object Set To Predicted
        api_response = api_instance.reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post(project_id, project_filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
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

# **revert_object_set_to_history_object_set_project_id_revert_to_history_post**
> ObjectSetRevertToHistoryRsp revert_object_set_to_history_object_set_project_id_revert_to_history_post(project_id, dry_run, project_filters, target=target)

Revert Object Set To History

Revert all objects for the given project, with the filters, to the target. - param `filters`: The set of filters to apply to get the target objects. - param `dry_run`: If set, then no real write but consequences of the revert will be replied. - param `target`: Use null/None for reverting using the last annotation from anyone, or a user id     for the last annotation from this user.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    project_id = 56 # int | 
dry_run = True # bool | 
project_filters = ecotaxa_cli_py.ProjectFilters() # ProjectFilters | 
target = 56 # int |  (optional)

    try:
        # Revert Object Set To History
        api_response = api_instance.revert_object_set_to_history_object_set_project_id_revert_to_history_post(project_id, dry_run, project_filters, target=target)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->revert_object_set_to_history_object_set_project_id_revert_to_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **dry_run** | **bool**|  | 
 **project_filters** | [**ProjectFilters**](ProjectFilters.md)|  | 
 **target** | **int**|  | [optional] 

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

# **update_object_set_object_set_update_post**
> object update_object_set_object_set_update_post(bulk_update_req)

Update Object Set

Update all the objects with given IDs and values Current user needs Manage right on all projects of specified objects.

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
    api_instance = ecotaxa_cli_py.ObjectsApi(api_client)
    bulk_update_req = ecotaxa_cli_py.BulkUpdateReq() # BulkUpdateReq | 

    try:
        # Update Object Set
        api_response = api_instance.update_object_set_object_set_update_post(bulk_update_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->update_object_set_object_set_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_update_req** | [**BulkUpdateReq**](BulkUpdateReq.md)|  | 

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


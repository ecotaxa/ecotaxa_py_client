# ecotaxa_py_client.JobsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**erase_job_jobs_job_id_delete**](JobsApi.md#erase_job_jobs_job_id_delete) | **DELETE** /jobs/{job_id} | Erase Job
[**get_job_file_jobs_job_id_file_get**](JobsApi.md#get_job_file_jobs_job_id_file_get) | **GET** /jobs/{job_id}/file | Get Job File
[**get_job_jobs_job_id_get**](JobsApi.md#get_job_jobs_job_id_get) | **GET** /jobs/{job_id}/ | Get Job
[**get_job_log_file_jobs_job_id_log_get**](JobsApi.md#get_job_log_file_jobs_job_id_log_get) | **GET** /jobs/{job_id}/log | Get Job Log File
[**list_jobs_jobs_get**](JobsApi.md#list_jobs_jobs_get) | **GET** /jobs/ | List Jobs
[**reply_job_question_jobs_job_id_answer_post**](JobsApi.md#reply_job_question_jobs_job_id_answer_post) | **POST** /jobs/{job_id}/answer | Reply Job Question
[**restart_job_jobs_job_id_restart_get**](JobsApi.md#restart_job_jobs_job_id_restart_get) | **GET** /jobs/{job_id}/restart | Restart Job


# **erase_job_jobs_job_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type erase_job_jobs_job_id_delete(job_id)

Erase Job

**Delete the job** from DB, with associated storage.  Return **NULL upon success.**  If the job is running then kill it.  🔒 The job must be accessible to current user.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import jobs_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
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

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    # example passing only required values which don't have defaults set
    try:
        # Erase Job
        api_response = api_instance.erase_job_jobs_job_id_delete(job_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->erase_job_jobs_job_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. |

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

# **get_job_file_jobs_job_id_file_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_job_file_jobs_job_id_file_get(job_id)

Get Job File

**Return the file produced by given job.**  🔒 The job must be accessible to current user.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import jobs_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
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

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    # example passing only required values which don't have defaults set
    try:
        # Get Job File
        api_response = api_instance.get_job_file_jobs_job_id_file_get(job_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->get_job_file_jobs_job_id_file_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerOrCookieAuth](../README.md#BearerOrCookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip, text/tab-separated-values


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return the produced file. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_jobs_job_id_get**
> JobModel get_job_jobs_job_id_get(job_id)

Get Job

Returns **information about the job** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import jobs_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.job_model import JobModel
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

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    # example passing only required values which don't have defaults set
    try:
        # Get Job
        api_response = api_instance.get_job_jobs_job_id_get(job_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->get_job_jobs_job_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. |

### Return type

[**JobModel**](JobModel.md)

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

# **get_job_log_file_jobs_job_id_log_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_job_log_file_jobs_job_id_log_get(job_id)

Get Job Log File

**Return the log file produced by given job.**  🔒 The job must be accessible to current user.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import jobs_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
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

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    # example passing only required values which don't have defaults set
    try:
        # Get Job Log File
        api_response = api_instance.get_job_log_file_jobs_job_id_log_get(job_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->get_job_log_file_jobs_job_id_log_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. |

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

# **list_jobs_jobs_get**
> [JobModel] list_jobs_jobs_get(for_admin)

List Jobs

**Return the jobs** for current user, or all of them if admin is asked for.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import jobs_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.job_model import JobModel
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

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    for_admin = False # bool | If FALSE return the jobs for current user, else return all of them.

    # example passing only required values which don't have defaults set
    try:
        # List Jobs
        api_response = api_instance.list_jobs_jobs_get(for_admin)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->list_jobs_jobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_admin** | **bool**| If FALSE return the jobs for current user, else return all of them. |

### Return type

[**[JobModel]**](JobModel.md)

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

# **reply_job_question_jobs_job_id_answer_post**
> bool, date, datetime, dict, float, int, list, str, none_type reply_job_question_jobs_job_id_answer_post(job_id)

Reply Job Question

**Send answers to last question.** The job resumes after it receives the reply.  Return **NULL upon success.**  *Note: It's only about data storage here.*   If the data is technically NOK e.g. not a JS object, standard 422 error should be thrown.  If the data is incorrect from consistency point of view, the job will return in Asking state.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import jobs_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
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

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reply Job Question
        api_response = api_instance.reply_job_question_jobs_job_id_answer_post(job_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->reply_job_question_jobs_job_id_answer_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reply Job Question
        api_response = api_instance.reply_job_question_jobs_job_id_answer_post(job_id, body=body)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->reply_job_question_jobs_job_id_answer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **restart_job_jobs_job_id_restart_get**
> bool, date, datetime, dict, float, int, list, str, none_type restart_job_jobs_job_id_restart_get(job_id)

Restart Job

**Restart the job related to the given id.**  Return **NULL upon success.**  🔒 The job must be in a restartable state, and be accessible to current user.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import time
import ecotaxa_py_client
from ecotaxa_py_client.api import jobs_api
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
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

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    # example passing only required values which don't have defaults set
    try:
        # Restart Job
        api_response = api_instance.restart_job_jobs_job_id_restart_get(job_id)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling JobsApi->restart_job_jobs_job_id_restart_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. |

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


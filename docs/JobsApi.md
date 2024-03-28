# ecotaxa_py_client.JobsApi

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**erase_job**](JobsApi.md#erase_job) | **DELETE** /jobs/{job_id} | Erase Job
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{job_id}/ | Get Job
[**get_job_file**](JobsApi.md#get_job_file) | **GET** /jobs/{job_id}/file | Get Job File
[**get_job_log_file**](JobsApi.md#get_job_log_file) | **GET** /jobs/{job_id}/log | Get Job Log File
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /jobs/ | List Jobs
[**reply_job_question**](JobsApi.md#reply_job_question) | **POST** /jobs/{job_id}/answer | Reply Job Question
[**restart_job**](JobsApi.md#restart_job) | **GET** /jobs/{job_id}/restart | Restart Job


# **erase_job**
> object erase_job(job_id)

Erase Job

**Delete the job** from DB, with associated storage.  Return **NULL upon success.**  If the job is running then kill it.  🔒 The job must be accessible to current user.

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
    api_instance = ecotaxa_py_client.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    try:
        # Erase Job
        api_response = api_instance.erase_job(job_id)
        print("The response of JobsApi->erase_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->erase_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. | 

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

# **get_job**
> JobModel get_job(job_id)

Get Job

Returns **information about the job** corresponding to the given id.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.job_model import JobModel
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
    api_instance = ecotaxa_py_client.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    try:
        # Get Job
        api_response = api_instance.get_job(job_id)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
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

# **get_job_file**
> object get_job_file(job_id, range=range)

Get Job File

**Return the file produced by given job.**  🔒 The job must be accessible to current user.

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
    api_instance = ecotaxa_py_client.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.
    range = 'range_example' # str |  (optional)

    try:
        # Get Job File
        api_response = api_instance.get_job_file(job_id, range=range)
        print("The response of JobsApi->get_job_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. | 
 **range** | **str**|  | [optional] 

### Return type

**object**

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

# **get_job_log_file**
> object get_job_log_file(job_id)

Get Job Log File

**Return the log file produced by given job.**  🔒 The job must be accessible to current user.

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
    api_instance = ecotaxa_py_client.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    try:
        # Get Job Log File
        api_response = api_instance.get_job_log_file(job_id)
        print("The response of JobsApi->get_job_log_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_log_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. | 

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

# **list_jobs**
> List[JobModel] list_jobs(for_admin)

List Jobs

**Return the jobs** for current user, or all of them if admin is asked for.

### Example

* OAuth Authentication (BearerOrCookieAuth):

```python
import ecotaxa_py_client
from ecotaxa_py_client.models.job_model import JobModel
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
    api_instance = ecotaxa_py_client.JobsApi(api_client)
    for_admin = false # bool | If FALSE return the jobs for current user, else return all of them.

    try:
        # List Jobs
        api_response = api_instance.list_jobs(for_admin)
        print("The response of JobsApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_admin** | **bool**| If FALSE return the jobs for current user, else return all of them. | 

### Return type

[**List[JobModel]**](JobModel.md)

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

# **reply_job_question**
> object reply_job_question(job_id, body=body)

Reply Job Question

**Send answers to last question.** The job resumes after it receives the reply.  Return **NULL upon success.**  *Note: It's only about data storage here.*   If the data is technically NOK e.g. not a JS object, standard 422 error should be thrown.  If the data is incorrect from consistency point of view, the job will return in Asking state.

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
    api_instance = ecotaxa_py_client.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.
    body = None # object |  (optional)

    try:
        # Reply Job Question
        api_response = api_instance.reply_job_question(job_id, body=body)
        print("The response of JobsApi->reply_job_question:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->reply_job_question: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. | 
 **body** | **object**|  | [optional] 

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

# **restart_job**
> object restart_job(job_id)

Restart Job

**Restart the job related to the given id.**  Return **NULL upon success.**  🔒 The job must be in a restartable state, and be accessible to current user.

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
    api_instance = ecotaxa_py_client.JobsApi(api_client)
    job_id = 47445 # int | Internal, the unique numeric id of this job.

    try:
        # Restart Job
        api_response = api_instance.restart_job(job_id)
        print("The response of JobsApi->restart_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->restart_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Internal, the unique numeric id of this job. | 

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


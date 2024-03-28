# JobModel

All information about the Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | **object** | Creation parameters. | [optional] 
**result** | **object** | Final result of the run. | [optional] 
**errors** | **List[str]** | The errors seen during last step. | [optional] [default to []]
**question** | **object** | The data provoking job move to Asking state. | [optional] 
**reply** | **object** | The data provided as a reply to the question. | [optional] 
**inside** | **object** | Internal state of the job. | [optional] 
**id** | **int** | Job unique identifier. | 
**owner_id** | **int** | The user who created and thus owns the job.  | 
**type** | **str** | The job type, e.g. import, export...  | 
**state** | **str** | What the job is doing. Could be &#39;P&#39; for Pending (Waiting for an execution thread), &#39;R&#39; for Running (Being executed inside a thread), &#39;A&#39; for Asking (Needing user information before resuming), &#39;E&#39; for Error (Stopped with error), &#39;F&#39; for Finished (Done). | [optional] 
**step** | **int** | Where in the workflow the job is.  | [optional] 
**progress_pct** | **int** | The progress percentage for UI.  | [optional] 
**progress_msg** | **str** | The message for UI, short version.  | [optional] 
**creation_date** | **datetime** | The date of creation of the Job, as text formatted according to the ISO 8601 standard. | 
**updated_on** | **datetime** | Last time that anything changed in present line.  | 

## Example

```python
from ecotaxa_py_client.models.job_model import JobModel

# TODO update the JSON string below
json = "{}"
# create an instance of JobModel from a JSON string
job_model_instance = JobModel.from_json(json)
# print the JSON string representation of the object
print(JobModel.to_json())

# convert the object into a dict
job_model_dict = job_model_instance.to_dict()
# create an instance of JobModel from a dict
job_model_form_dict = job_model.from_dict(job_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



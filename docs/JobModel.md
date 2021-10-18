# JobModel

All information about the Job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Job unique identifier. | 
**owner_id** | **int** | The user who created and thus owns the job.  | 
**type** | **str** | The job type, e.g. import, export...  | 
**creation_date** | **datetime** | The date of creation of the Job, as text formatted according to the ISO 8601 standard. | 
**updated_on** | **datetime** | Last time that anything changed in present line.  | 
**params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Creation parameters. | [optional]  if omitted the server will use the default value of {}
**result** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Final result of the run. | [optional]  if omitted the server will use the default value of {}
**errors** | **[str]** | The errors seen during last step. | [optional]  if omitted the server will use the default value of []
**question** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The data provoking job move to Asking state. | [optional]  if omitted the server will use the default value of {}
**reply** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The data provided as a reply to the question. | [optional]  if omitted the server will use the default value of {}
**inside** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Internal state of the job. | [optional]  if omitted the server will use the default value of {}
**state** | **str** | What the job is doing. Could be &#39;P&#39; for Pending (Waiting for an execution thread), &#39;R&#39; for Running (Being executed inside a thread), &#39;A&#39; for Asking (Needing user information before resuming), &#39;E&#39; for Error (Stopped with error), &#39;F&#39; for Finished (Done). | [optional] 
**step** | **int** | Where in the workflow the job is.  | [optional] 
**progress_pct** | **int** | The progress percentage for UI.  | [optional] 
**progress_msg** | **str** | The message for UI, short version.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



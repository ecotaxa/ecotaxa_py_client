# ProjectUserStatsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projid** | **int** | The project id. | [optional] 
**annotators** | [**List[MinimalUserBO]**](MinimalUserBO.md) | The users who ever decided on classification or state of objects. | [optional] 
**activities** | [**List[UserActivity]**](UserActivity.md) | More details on annotators&#39; activities. | [optional] 

## Example

```python
from ecotaxa_py_client.models.project_user_stats_model import ProjectUserStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUserStatsModel from a JSON string
project_user_stats_model_instance = ProjectUserStatsModel.from_json(json)
# print the JSON string representation of the object
print(ProjectUserStatsModel.to_json())

# convert the object into a dict
project_user_stats_model_dict = project_user_stats_model_instance.to_dict()
# create an instance of ProjectUserStatsModel from a dict
project_user_stats_model_form_dict = project_user_stats_model.from_dict(project_user_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



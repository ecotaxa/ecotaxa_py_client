# ProjectSetColumnStatsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proj_ids** | **List[int]** | Projects IDs from the call. | [optional] 
**total** | **int** | All rows regardless of emptiness. | [optional] 
**columns** | **List[str]** | Column names from the call. | [optional] 
**counts** | **List[int]** | Counts of non-empty values, one per column. | [optional] 
**variances** | **List[float]** | Variances of values, one per column. | [optional] 

## Example

```python
from ecotaxa_py_client.models.project_set_column_stats_model import ProjectSetColumnStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSetColumnStatsModel from a JSON string
project_set_column_stats_model_instance = ProjectSetColumnStatsModel.from_json(json)
# print the JSON string representation of the object
print(ProjectSetColumnStatsModel.to_json())

# convert the object into a dict
project_set_column_stats_model_dict = project_set_column_stats_model_instance.to_dict()
# create an instance of ProjectSetColumnStatsModel from a dict
project_set_column_stats_model_form_dict = project_set_column_stats_model.from_dict(project_set_column_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



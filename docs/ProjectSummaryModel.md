# ProjectSummaryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projid** | **int** | Project unique identifier. | 
**title** | **str** | Project&#39;s title. | 

## Example

```python
from ecotaxa_py_client.models.project_summary_model import ProjectSummaryModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSummaryModel from a JSON string
project_summary_model_instance = ProjectSummaryModel.from_json(json)
# print the JSON string representation of the object
print(ProjectSummaryModel.to_json())

# convert the object into a dict
project_summary_model_dict = project_summary_model_instance.to_dict()
# create an instance of ProjectSummaryModel from a dict
project_summary_model_form_dict = project_summary_model.from_dict(project_summary_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ProjectTaxoStatsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projid** | **int** | The project id. | 
**used_taxa** | **List[int]** | The taxa/category ids used inside the project. An id of -1 means some unclassified objects. | [optional] [default to []]
**nb_unclassified** | **int** | The number of unclassified objects inside the project. | 
**nb_validated** | **int** | The number of validated objects inside the project. | 
**nb_dubious** | **int** | The number of dubious objects inside the project. | 
**nb_predicted** | **int** | The number of predicted objects inside the project. | 

## Example

```python
from ecotaxa_py_client.models.project_taxo_stats_model import ProjectTaxoStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTaxoStatsModel from a JSON string
project_taxo_stats_model_instance = ProjectTaxoStatsModel.from_json(json)
# print the JSON string representation of the object
print(ProjectTaxoStatsModel.to_json())

# convert the object into a dict
project_taxo_stats_model_dict = project_taxo_stats_model_instance.to_dict()
# create an instance of ProjectTaxoStatsModel from a dict
project_taxo_stats_model_form_dict = project_taxo_stats_model.from_dict(project_taxo_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



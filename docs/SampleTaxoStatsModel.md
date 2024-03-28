# SampleTaxoStatsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_id** | **int** | The sample id. | [optional] 
**used_taxa** | **List[int]** | The taxa/category ids used inside the sample. -1 for unclassified objects. | [optional] 
**nb_unclassified** | **int** | The number of unclassified objects inside the sample. | [optional] 
**nb_validated** | **int** | The number of validated objects inside the sample. | [optional] 
**nb_dubious** | **int** | The number of dubious objects inside the sample. | [optional] 
**nb_predicted** | **int** | The number of predicted objects inside the sample. | [optional] 

## Example

```python
from ecotaxa_py_client.models.sample_taxo_stats_model import SampleTaxoStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of SampleTaxoStatsModel from a JSON string
sample_taxo_stats_model_instance = SampleTaxoStatsModel.from_json(json)
# print the JSON string representation of the object
print(SampleTaxoStatsModel.to_json())

# convert the object into a dict
sample_taxo_stats_model_dict = sample_taxo_stats_model_instance.to_dict()
# create an instance of SampleTaxoStatsModel from a dict
sample_taxo_stats_model_form_dict = sample_taxo_stats_model.from_dict(sample_taxo_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



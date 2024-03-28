# TaxonUsageModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projid** | **int** | Project unique identifier. | 
**title** | **str** | Project&#39;s title. | 
**nb_validated** | **int** | How many validated objects in this category in this project. | 

## Example

```python
from ecotaxa_py_client.models.taxon_usage_model import TaxonUsageModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonUsageModel from a JSON string
taxon_usage_model_instance = TaxonUsageModel.from_json(json)
# print the JSON string representation of the object
print(TaxonUsageModel.to_json())

# convert the object into a dict
taxon_usage_model_dict = taxon_usage_model_instance.to_dict()
# create an instance of TaxonUsageModel from a dict
taxon_usage_model_form_dict = taxon_usage_model.from_dict(taxon_usage_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



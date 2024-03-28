# SampleModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sampleid** | **int** | The sample Id. | 
**projid** | **int** | The project Id. | 
**orig_id** | **str** | Original sample ID from initial TSV load. | 
**latitude** | **float** | The latitude. | [optional] 
**longitude** | **float** | The longitude. | [optional] 
**dataportal_descriptor** | **str** |  | [optional] 
**free_columns** | **object** | Free columns from sample mapping in project. | [optional] 

## Example

```python
from ecotaxa_py_client.models.sample_model import SampleModel

# TODO update the JSON string below
json = "{}"
# create an instance of SampleModel from a JSON string
sample_model_instance = SampleModel.from_json(json)
# print the JSON string representation of the object
print(SampleModel.to_json())

# convert the object into a dict
sample_model_dict = sample_model_instance.to_dict()
# create an instance of SampleModel from a dict
sample_model_form_dict = sample_model.from_dict(sample_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



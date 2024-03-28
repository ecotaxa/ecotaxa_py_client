# AcquisitionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisid** | **int** | The acquisition Id. | 
**acq_sample_id** | **int** | The acquisition sample Id. | 
**orig_id** | **str** | Original acquisition ID from initial TSV load. | 
**instrument** | **str** | Instrument used. | [optional] 
**free_columns** | **object** | Free columns from acquisition mapping in project. | [optional] 

## Example

```python
from ecotaxa_py_client.models.acquisition_model import AcquisitionModel

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionModel from a JSON string
acquisition_model_instance = AcquisitionModel.from_json(json)
# print the JSON string representation of the object
print(AcquisitionModel.to_json())

# convert the object into a dict
acquisition_model_dict = acquisition_model_instance.to_dict()
# create an instance of AcquisitionModel from a dict
acquisition_model_form_dict = acquisition_model.from_dict(acquisition_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



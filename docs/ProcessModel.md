# ProcessModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processid** | **int** | The process Id. | 
**orig_id** | **str** | Original process ID from initial TSV load. | 
**free_columns** | **object** |  | [optional] 

## Example

```python
from ecotaxa_py_client.models.process_model import ProcessModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessModel from a JSON string
process_model_instance = ProcessModel.from_json(json)
# print the JSON string representation of the object
print(ProcessModel.to_json())

# convert the object into a dict
process_model_dict = process_model_instance.to_dict()
# create an instance of ProcessModel from a dict
process_model_form_dict = process_model.from_dict(process_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



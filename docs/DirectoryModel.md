# DirectoryModel

A path + list of entries inside. The path is relative to an implied root.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | A /-separated path from root to this directory. | 
**entries** | [**List[DirectoryEntryModel]**](DirectoryEntryModel.md) | Entries, i.e. subdirectories or contained files.All entries are readable, i.e. can be used as input or navigated into. | 

## Example

```python
from ecotaxa_py_client.models.directory_model import DirectoryModel

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryModel from a JSON string
directory_model_instance = DirectoryModel.from_json(json)
# print the JSON string representation of the object
print(DirectoryModel.to_json())

# convert the object into a dict
directory_model_dict = directory_model_instance.to_dict()
# create an instance of DirectoryModel from a dict
directory_model_form_dict = directory_model.from_dict(directory_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



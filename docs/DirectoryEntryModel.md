# DirectoryEntryModel

Something inside a directory, i.e. a sub-directory or a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | atomic entry name. | 
**type** | **str** | entry type, &#39;D&#39; for directory, &#39;F&#39; for file. | 
**size** | **int** | Entry size, for zips. | 
**mtime** | **str** | Modification time, in ISO format. | 

## Example

```python
from ecotaxa_py_client.models.directory_entry_model import DirectoryEntryModel

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryEntryModel from a JSON string
directory_entry_model_instance = DirectoryEntryModel.from_json(json)
# print the JSON string representation of the object
print(DirectoryEntryModel.to_json())

# convert the object into a dict
directory_entry_model_dict = directory_entry_model_instance.to_dict()
# create an instance of DirectoryEntryModel from a dict
directory_entry_model_form_dict = directory_entry_model.from_dict(directory_entry_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



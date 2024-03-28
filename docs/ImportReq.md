# ImportReq

Import request, from UI choices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_path** | **str** | Source path on server, to zip or plain directory.     The path can be returned by a file upload (absolute),     otherwise it&#39;s relative to shared file area root. | 
**taxo_mappings** | **Dict[str, str]** | Optional taxonomy mapping, the key specifies the taxonomy ID found in file and the value specifies the final taxonomy ID to write. | [optional] 
**skip_loaded_files** | **bool** | If true skip loaded files, else don&#39;t. | [optional] [default to False]
**skip_existing_objects** | **bool** | If true skip existing objects, else don&#39;t. | [optional] [default to False]
**update_mode** | **str** | Update data (&#39;Yes&#39;), including classification (&#39;Cla&#39;). | [optional] [default to '']

## Example

```python
from ecotaxa_py_client.models.import_req import ImportReq

# TODO update the JSON string below
json = "{}"
# create an instance of ImportReq from a JSON string
import_req_instance = ImportReq.from_json(json)
# print the JSON string representation of the object
print(ImportReq.to_json())

# convert the object into a dict
import_req_dict = import_req_instance.to_dict()
# create an instance of ImportReq from a dict
import_req_form_dict = import_req.from_dict(import_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



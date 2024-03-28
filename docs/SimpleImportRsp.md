# SimpleImportRsp

Simple Import, response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The job which was created for the run. 0 if called with dry_run option. | 
**errors** | **List[str]** | Validation errors, dry_run or not. | 

## Example

```python
from ecotaxa_py_client.models.simple_import_rsp import SimpleImportRsp

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleImportRsp from a JSON string
simple_import_rsp_instance = SimpleImportRsp.from_json(json)
# print the JSON string representation of the object
print(SimpleImportRsp.to_json())

# convert the object into a dict
simple_import_rsp_dict = simple_import_rsp_instance.to_dict()
# create an instance of SimpleImportRsp from a dict
simple_import_rsp_form_dict = simple_import_rsp.from_dict(simple_import_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



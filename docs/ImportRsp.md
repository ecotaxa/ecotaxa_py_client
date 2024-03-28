# ImportRsp

Import response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The job which was created for the run. | 
**errors** | **List[str]** | Errors from analysis. | [optional] [default to []]

## Example

```python
from ecotaxa_py_client.models.import_rsp import ImportRsp

# TODO update the JSON string below
json = "{}"
# create an instance of ImportRsp from a JSON string
import_rsp_instance = ImportRsp.from_json(json)
# print the JSON string representation of the object
print(ImportRsp.to_json())

# convert the object into a dict
import_rsp_dict = import_rsp_instance.to_dict()
# create an instance of ImportRsp from a dict
import_rsp_form_dict = import_rsp.from_dict(import_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



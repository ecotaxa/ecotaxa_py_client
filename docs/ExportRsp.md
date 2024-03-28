# ExportRsp

Export response, for all export jobs, either on Project or Collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | Showstopper problems found preventing building the archive. | [optional] [default to []]
**warnings** | **List[str]** | Problems found while building the archive, which do not prevent producing it. | [optional] [default to []]
**job_id** | **int** | The created job, 0 if there were problems. | [optional] [default to 0]

## Example

```python
from ecotaxa_py_client.models.export_rsp import ExportRsp

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRsp from a JSON string
export_rsp_instance = ExportRsp.from_json(json)
# print the JSON string representation of the object
print(ExportRsp.to_json())

# convert the object into a dict
export_rsp_dict = export_rsp_instance.to_dict()
# create an instance of ExportRsp from a dict
export_rsp_form_dict = export_rsp.from_dict(export_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



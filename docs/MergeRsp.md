# MergeRsp

Merge response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | The errors found during processing. | [optional] [default to []]

## Example

```python
from ecotaxa_py_client.models.merge_rsp import MergeRsp

# TODO update the JSON string below
json = "{}"
# create an instance of MergeRsp from a JSON string
merge_rsp_instance = MergeRsp.from_json(json)
# print the JSON string representation of the object
print(MergeRsp.to_json())

# convert the object into a dict
merge_rsp_dict = merge_rsp_instance.to_dict()
# create an instance of MergeRsp from a dict
merge_rsp_form_dict = merge_rsp.from_dict(merge_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



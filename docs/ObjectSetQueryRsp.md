# ObjectSetQueryRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[int]** | Matching object IDs. | [optional] [default to []]
**acquisition_ids** | **List[int]** | Parent (acquisition) IDs. | [optional] [default to []]
**sample_ids** | **List[int]** | Parent (sample) IDs. | [optional] [default to []]
**project_ids** | **List[int]** | Project Ids. | [optional] [default to []]
**details** | **List[List[object]]** | Requested fields, in request order. | [optional] [default to []]
**total_ids** | **int** | Total rows returned by the query, even if it was window-ed. | [optional] [default to 0]

## Example

```python
from ecotaxa_py_client.models.object_set_query_rsp import ObjectSetQueryRsp

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSetQueryRsp from a JSON string
object_set_query_rsp_instance = ObjectSetQueryRsp.from_json(json)
# print the JSON string representation of the object
print(ObjectSetQueryRsp.to_json())

# convert the object into a dict
object_set_query_rsp_dict = object_set_query_rsp_instance.to_dict()
# create an instance of ObjectSetQueryRsp from a dict
object_set_query_rsp_form_dict = object_set_query_rsp.from_dict(object_set_query_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



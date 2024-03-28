# ObjectSetRevertToHistoryRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_entries** | [**List[HistoricalLastClassif]**](HistoricalLastClassif.md) | Object + last classification | [optional] [default to []]
**classif_info** | **object** | Classification names (self+parent) for involved IDs. | [optional] 

## Example

```python
from ecotaxa_py_client.models.object_set_revert_to_history_rsp import ObjectSetRevertToHistoryRsp

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSetRevertToHistoryRsp from a JSON string
object_set_revert_to_history_rsp_instance = ObjectSetRevertToHistoryRsp.from_json(json)
# print the JSON string representation of the object
print(ObjectSetRevertToHistoryRsp.to_json())

# convert the object into a dict
object_set_revert_to_history_rsp_dict = object_set_revert_to_history_rsp_instance.to_dict()
# create an instance of ObjectSetRevertToHistoryRsp from a dict
object_set_revert_to_history_rsp_form_dict = object_set_revert_to_history_rsp.from_dict(object_set_revert_to_history_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



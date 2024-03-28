# BulkUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_ids** | **List[int]** | The IDs of the target entities. | 
**updates** | [**List[ColUpdate]**](ColUpdate.md) | The list of updates, to do on all impacted entities.        {            ucol : A column name, pseudo-columns AKA free ones, are OK.            uval : The new value to set, always as a string        } | 

## Example

```python
from ecotaxa_py_client.models.bulk_update_req import BulkUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateReq from a JSON string
bulk_update_req_instance = BulkUpdateReq.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateReq.to_json())

# convert the object into a dict
bulk_update_req_dict = bulk_update_req_instance.to_dict()
# create an instance of BulkUpdateReq from a dict
bulk_update_req_form_dict = bulk_update_req.from_dict(bulk_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



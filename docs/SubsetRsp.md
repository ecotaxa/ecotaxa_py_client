# SubsetRsp

Subset response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | The job created for this operation. | 

## Example

```python
from ecotaxa_py_client.models.subset_rsp import SubsetRsp

# TODO update the JSON string below
json = "{}"
# create an instance of SubsetRsp from a JSON string
subset_rsp_instance = SubsetRsp.from_json(json)
# print the JSON string representation of the object
print(SubsetRsp.to_json())

# convert the object into a dict
subset_rsp_dict = subset_rsp_instance.to_dict()
# create an instance of SubsetRsp from a dict
subset_rsp_form_dict = subset_rsp.from_dict(subset_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



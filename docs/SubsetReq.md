# SubsetReq

Subset request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ProjectFiltersDict**](ProjectFiltersDict.md) | The filters to apply to project. | [optional] 
**dest_prj_id** | **int** | The destination project ID. | 
**group_type** | [**GroupDefinitions**](GroupDefinitions.md) | Define the groups in which to apply limits. C for categories, S for samples, A for acquisitions. | 
**limit_type** | [**LimitMethods**](LimitMethods.md) | The type of limit_value: P for %, V for constant, both per group. | 
**limit_value** | **float** | Limit value, e.g. 20% or 5 per copepoda or 5% per sample. | 

## Example

```python
from ecotaxa_py_client.models.subset_req import SubsetReq

# TODO update the JSON string below
json = "{}"
# create an instance of SubsetReq from a JSON string
subset_req_instance = SubsetReq.from_json(json)
# print the JSON string representation of the object
print(SubsetReq.to_json())

# convert the object into a dict
subset_req_dict = subset_req_instance.to_dict()
# create an instance of SubsetReq from a dict
subset_req_form_dict = subset_req.from_dict(subset_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



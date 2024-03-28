# ClassifyAutoReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_ids** | **List[int]** | The IDs of the target objects. | 
**classifications** | **List[int]** | The wanted new classifications, i.e. taxon ID, one for each object. | 
**scores** | **List[float]** | The classification score is generally between 0 and 1. It indicates the probability that the taxon prediction of this object is correct. | 
**keep_log** | **bool** | Set if former automatic classification history is needed. | 

## Example

```python
from ecotaxa_py_client.models.classify_auto_req import ClassifyAutoReq

# TODO update the JSON string below
json = "{}"
# create an instance of ClassifyAutoReq from a JSON string
classify_auto_req_instance = ClassifyAutoReq.from_json(json)
# print the JSON string representation of the object
print(ClassifyAutoReq.to_json())

# convert the object into a dict
classify_auto_req_dict = classify_auto_req_instance.to_dict()
# create an instance of ClassifyAutoReq from a dict
classify_auto_req_form_dict = classify_auto_req.from_dict(classify_auto_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ClassifyReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_ids** | **List[int]** | The IDs of the target objects. | 
**classifications** | **List[int]** | The wanted new classifications, i.e. taxon ID, one for each object. Use -1 to keep present one. | 
**wanted_qualification** | **str** | The wanted qualifications for all objects. &#39;V&#39; or &#39;P&#39;. | 

## Example

```python
from ecotaxa_py_client.models.classify_req import ClassifyReq

# TODO update the JSON string below
json = "{}"
# create an instance of ClassifyReq from a JSON string
classify_req_instance = ClassifyReq.from_json(json)
# print the JSON string representation of the object
print(ClassifyReq.to_json())

# convert the object into a dict
classify_req_dict = classify_req_instance.to_dict()
# create an instance of ClassifyReq from a dict
classify_req_form_dict = classify_req.from_dict(classify_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



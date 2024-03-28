# ObjectSetSummaryRsp

Classification summary from object set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_objects** | **int** | Total number of objects in the set. | [optional] 
**validated_objects** | **int** | Number of validated objects in the set. | [optional] 
**dubious_objects** | **int** | Number of dubious objects in the set. | [optional] 
**predicted_objects** | **int** | Number of predicted objects in the set. | [optional] 

## Example

```python
from ecotaxa_py_client.models.object_set_summary_rsp import ObjectSetSummaryRsp

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSetSummaryRsp from a JSON string
object_set_summary_rsp_instance = ObjectSetSummaryRsp.from_json(json)
# print the JSON string representation of the object
print(ObjectSetSummaryRsp.to_json())

# convert the object into a dict
object_set_summary_rsp_dict = object_set_summary_rsp_instance.to_dict()
# create an instance of ObjectSetSummaryRsp from a dict
object_set_summary_rsp_form_dict = object_set_summary_rsp.from_dict(object_set_summary_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



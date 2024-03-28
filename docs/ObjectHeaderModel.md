# ObjectHeaderModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objid** | **int** | The object Id. | 
**acquisid** | **int** | The parent acquisition Id. | 
**classif_id** | **int** | The classification Id. | [optional] 
**objtime** | **str** |  | [optional] 
**latitude** | **float** | The latitude. | [optional] 
**longitude** | **float** | The longitude. | [optional] 
**depth_min** | **float** | The min depth. | [optional] 
**depth_max** | **float** | The min depth. | [optional] 
**objdate** | **date** |  | [optional] 
**classif_qual** | **str** | The classification qualification. Could be **P** for predicted, **V** for validated or **D** for Dubious. | [optional] 
**sunpos** | **str** | Sun position, from date, time and coords. | [optional] 
**classif_when** | **datetime** | The classification date. | [optional] 
**classif_who** | **int** | The user who manualy classify this object. | [optional] 
**classif_auto_id** | **int** | Set if the object was ever predicted, remain forever with these value. Reflect the &#39;last state&#39; only if classif_qual is &#39;P&#39;.  | [optional] 
**classif_auto_when** | **datetime** | Set if the object was ever predicted, remain forever with these value. Reflect the &#39;last state&#39; only if classif_qual is &#39;P&#39;. The classification date. | [optional] 
**classif_auto_score** | **float** | Set if the object was ever predicted, remain forever with these value. Reflect the &#39;last state&#39; only if classif_qual is &#39;P&#39;. The classification auto score is generally between 0 and 1. This is a confidence score, in the fact that, the taxon prediction for this object is correct. | [optional] 
**orig_id** | **str** | Original object ID from initial TSV load. | 
**object_link** | **str** | Object link. | [optional] 
**complement_info** | **str** |  | [optional] 

## Example

```python
from ecotaxa_py_client.models.object_header_model import ObjectHeaderModel

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectHeaderModel from a JSON string
object_header_model_instance = ObjectHeaderModel.from_json(json)
# print the JSON string representation of the object
print(ObjectHeaderModel.to_json())

# convert the object into a dict
object_header_model_dict = object_header_model_instance.to_dict()
# create an instance of ObjectHeaderModel from a dict
object_header_model_form_dict = object_header_model.from_dict(object_header_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



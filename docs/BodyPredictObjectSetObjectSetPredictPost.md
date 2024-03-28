# BodyPredictObjectSetObjectSetPredictPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ProjectFilters**](ProjectFilters.md) |  | 
**request** | [**PredictionReq**](PredictionReq.md) |  | 

## Example

```python
from ecotaxa_py_client.models.body_predict_object_set_object_set_predict_post import BodyPredictObjectSetObjectSetPredictPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyPredictObjectSetObjectSetPredictPost from a JSON string
body_predict_object_set_object_set_predict_post_instance = BodyPredictObjectSetObjectSetPredictPost.from_json(json)
# print the JSON string representation of the object
print(BodyPredictObjectSetObjectSetPredictPost.to_json())

# convert the object into a dict
body_predict_object_set_object_set_predict_post_dict = body_predict_object_set_object_set_predict_post_instance.to_dict()
# create an instance of BodyPredictObjectSetObjectSetPredictPost from a dict
body_predict_object_set_object_set_predict_post_form_dict = body_predict_object_set_object_set_predict_post.from_dict(body_predict_object_set_object_set_predict_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



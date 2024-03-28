# PredictionReq

How to predict, in details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The destination project, of which objects will be predicted. | 
**source_project_ids** | **List[int]** | The source projects, objects in them will serve as reference. | 
**learning_limit** | **int** | When set (to a positive value), there will be this number  of objects, _per category_, in the learning set. | [optional] 
**features** | **List[str]** | The object features AKA free column, to use in the algorithm. Features must be common to all projects, source ones and destination one. | 
**categories** | **List[int]** | In source projects, only objects validated with these categories will be considered. | 
**use_scn** | **bool** | Use extra features, generated using the image, for improving the prediction. | [optional] [default to False]
**pre_mapping** | **Dict[str, int]** | Categories in keys become value one before launching the ML algorithm. Any unknown value is ignored. | 

## Example

```python
from ecotaxa_py_client.models.prediction_req import PredictionReq

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionReq from a JSON string
prediction_req_instance = PredictionReq.from_json(json)
# print the JSON string representation of the object
print(PredictionReq.to_json())

# convert the object into a dict
prediction_req_dict = prediction_req_instance.to_dict()
# create an instance of PredictionReq from a dict
prediction_req_form_dict = prediction_req.from_dict(prediction_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



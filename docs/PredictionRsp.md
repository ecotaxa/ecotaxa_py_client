# PredictionRsp

Prediction response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | Showstopper problems found while preparing the prediction. | [optional] [default to []]
**warnings** | **List[str]** | Problems found while preparing the prediction. | [optional] [default to []]
**job_id** | **int** | The created job, 0 if there were problems. | [optional] [default to 0]

## Example

```python
from ecotaxa_py_client.models.prediction_rsp import PredictionRsp

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionRsp from a JSON string
prediction_rsp_instance = PredictionRsp.from_json(json)
# print the JSON string representation of the object
print(PredictionRsp.to_json())

# convert the object into a dict
prediction_rsp_dict = prediction_rsp_instance.to_dict()
# create an instance of PredictionRsp from a dict
prediction_rsp_form_dict = prediction_rsp.from_dict(prediction_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



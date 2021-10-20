# ObjectSetSummaryRsp

Tuned model for faster serialization out. TODO: A bit useless in the context as FastAPI does _not_ use ser/deser from the model.       Instead, it produces what needs to be sent over the wire and calls a JSON encoder onto it.       So 1) It calls def jsonable_encoder (in FastAPI encoders.py)          2) It calls an encoder (presently ORJSONEncoder in main.py)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_objects** | **int** |  | [optional] 
**validated_objects** | **int** |  | [optional] 
**dubious_objects** | **int** |  | [optional] 
**predicted_objects** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



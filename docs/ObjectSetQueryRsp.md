# ObjectSetQueryRsp

Tuned model for faster serialization out. TODO: A bit useless in the context as FastAPI does _not_ use ser/deser from the model.       Instead, it produces what needs to be sent over the wire and calls a JSON encoder onto it.       So 1) It calls def jsonable_encoder (in FastAPI encoders.py)          2) It calls an encoder (presently ORJSONEncoder in main.py)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **[int]** |  | [optional]  if omitted the server will use the default value of []
**acquisition_ids** | **[int]** |  | [optional]  if omitted the server will use the default value of []
**sample_ids** | **[int]** |  | [optional]  if omitted the server will use the default value of []
**project_ids** | **[int]** |  | [optional]  if omitted the server will use the default value of []
**details** | **[[bool, date, datetime, dict, float, int, list, str, none_type]]** |  | [optional]  if omitted the server will use the default value of []
**total_ids** | **int** |  | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



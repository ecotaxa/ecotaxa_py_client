# JobModel

All from DB table

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**owner_id** | **int** |  | 
**type** | **str** |  | 
**creation_date** | **datetime** |  | 
**updated_on** | **datetime** |  | 
**params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**result** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**errors** | **[str]** |  | [optional]  if omitted the server will use the default value of []
**question** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**reply** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**inside** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**state** | **str** |  | [optional] 
**step** | **int** |  | [optional] 
**progress_pct** | **int** |  | [optional] 
**progress_msg** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



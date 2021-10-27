# CreateProjectReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The project title, as text. | 
**clone_of_id** | **int** | Internal, numeric id of a project to clone as a new one. By default it does not clone anything. | [optional] 
**visible** | **bool** | When TRUE, the project is created visible by all users. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



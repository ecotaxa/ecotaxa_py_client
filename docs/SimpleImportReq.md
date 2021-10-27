# SimpleImportReq

Simple Import request. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_path** | **str** | Source path on server, to zip or plain directory. | 
**values** | **{str: (str,)}** | :imgdate, imgtime, latitude, longitude, depthmin, depthmax, taxolb, userlb, status | 
**possible_values** | **[str]** |  | [optional]  if omitted the server will use the default value of ["imgdate","imgtime","latitude","longitude","depthmin","depthmax","taxolb","userlb","status"]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



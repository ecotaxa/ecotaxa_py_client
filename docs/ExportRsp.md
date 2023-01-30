# ExportRsp

Export response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **[str]** | Showstopper problems found preventing building the archive. | [optional]  if omitted the server will use the default value of []
**warnings** | **[str]** | Problems found while building the archive, which do not prevent producing it. | [optional]  if omitted the server will use the default value of []
**job_id** | **int** | The created job, 0 if there were problems. | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



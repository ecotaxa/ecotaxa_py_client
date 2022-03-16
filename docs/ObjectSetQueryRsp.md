# ObjectSetQueryRsp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **[int]** | Matching object IDs. | [optional]  if omitted the server will use the default value of []
**acquisition_ids** | **[int]** | Parent (acquisition) IDs. | [optional]  if omitted the server will use the default value of []
**sample_ids** | **[int]** | Parent (sample) IDs. | [optional]  if omitted the server will use the default value of []
**project_ids** | **[int]** | Project Ids. | [optional]  if omitted the server will use the default value of []
**details** | **[[bool, date, datetime, dict, float, int, list, str, none_type]]** | Requested fields, in request order. | [optional]  if omitted the server will use the default value of []
**total_ids** | **int** | Total rows returned by the query, even if it was window-ed. | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



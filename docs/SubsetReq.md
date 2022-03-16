# SubsetReq

Subset request. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_prj_id** | **int** | The destination project ID. | 
**group_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | Define the groups in which to apply limits. C for categories, S for samples, A for acquisitions. | 
**limit_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The type of limit_value: P for %, V for constant, both per group. | 
**limit_value** | **float** | Limit value, e.g. 20% or 5 per copepoda or 5% per sample. | 
**filters** | **bool, date, datetime, dict, float, int, list, str, none_type** | The filters to apply to project. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SubsetReq

Subset request. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **dict(str, str)** | The filters to apply to project | [optional] 
**dest_prj_id** | **int** | The destination project ID. | 
**group_type** | [**GroupDefinitions**](GroupDefinitions.md) | Define the groups in which to apply limits. C for categories, S for samples, A for acquisitions. | 
**limit_type** | [**LimitMethods**](LimitMethods.md) | The type of limit_value: P for %, V for constant, both per group. | 
**limit_value** | **float** | Limit value, e.g. 20% or 5 per copepoda or 5% per sample. | 
**do_images** | **bool** | If set, also clone images. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



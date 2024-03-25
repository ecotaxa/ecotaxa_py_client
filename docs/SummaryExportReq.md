# SummaryExportReq

Summary export request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project to export. | 
**quantity** | **bool, date, datetime, dict, float, int, list, str, none_type** | The quantity to compute. Abundance is always possible. | [optional] 
**summarise_by** | **bool, date, datetime, dict, float, int, list, str, none_type** | Computations aggregation level. | [optional] 
**taxo_mapping** | **{str: (int,)}** | Mapping from present taxon (key) to output replacement one (value). Use a 0 replacement to _discard_ the present taxon. | [optional]  if omitted the server will use the default value of {}
**formulae** | **{str: (str,)}** | Transitory: How to get values from DB free columns. Python syntax, prefixes are &#39;sam&#39;, &#39;ssm&#39; and &#39;obj&#39;.Variables used in computations are &#39;total_water_volume&#39;, &#39;subsample_coef&#39; and &#39;individual_volume&#39; | [optional]  if omitted the server will use the default value of {}
**out_to_ftp** | **bool** | Copy result file to FTP area. Original file is still available. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



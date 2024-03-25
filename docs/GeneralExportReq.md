# GeneralExportReq

General purpose export request, produce a zip in a job with many options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project to export. | 
**split_by** | **bool, date, datetime, dict, float, int, list, str, none_type** | If not none, separate (in ZIP sub-directories) output per given field. | [optional] 
**with_images** | **bool, date, datetime, dict, float, int, list, str, none_type** | Add in ZIP first (i.e. visible) image, all images, or no image.⚠️ &#39;all&#39; means maybe several lines per object in TSVs. | [optional] 
**with_internal_ids** | **bool** | Export internal database IDs. | [optional]  if omitted the server will use the default value of False
**with_types_row** | **bool** | Add an EcoTaxa-compatible second line with types. | [optional]  if omitted the server will use the default value of False
**only_annotations** | **bool** | Only save objects&#39; last annotation data. | [optional]  if omitted the server will use the default value of False
**out_to_ftp** | **bool** | Copy result file to FTP area. Original file is still available. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



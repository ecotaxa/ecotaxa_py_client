# ImportReq

Import request, from UI choices.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_path** | **str** | Source path on server, to zip or plain directory.     The path can be returned by a file upload (absolute),     otherwise it&#39;s relative to shared file area root. | 
**taxo_mappings** | **{str: (str,)}** | Optional taxonomy mapping, the key specifies the taxonomy ID found in file and the value specifies the final taxonomy ID to write. | [optional]  if omitted the server will use the default value of {}
**skip_loaded_files** | **bool** | If true skip loaded files, else don&#39;t. | [optional]  if omitted the server will use the default value of False
**skip_existing_objects** | **bool** | If true skip existing objects, else don&#39;t. | [optional]  if omitted the server will use the default value of False
**update_mode** | **str** | Update data (&#39;Yes&#39;), including classification (&#39;Cla&#39;). | [optional]  if omitted the server will use the default value of ""
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



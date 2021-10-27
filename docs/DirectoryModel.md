# DirectoryModel

A path + list of entries inside. The path is relative to an implied root.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | A /-separated path from root to this directory. | 
**entries** | [**[DirectoryEntryModel]**](DirectoryEntryModel.md) | Entries, i.e. subdirectories or contained files.All entries are readable, i.e. can be used as input or navigated into. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



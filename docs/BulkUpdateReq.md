# BulkUpdateReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_ids** | **[int]** | The IDs of the target entities. | 
**updates** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | The list of updates, to do on all impacted entities.        {            ucol : A column name, pseudo-columns AKA free ones, are OK.            uval : The new value to set, always as a string        } | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



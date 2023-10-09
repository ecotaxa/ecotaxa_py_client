# CollectionModel

Basic and computed information about the Collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **[int]** | The list of composing project IDs. | 
**id** | **int** | The collection Id. | 
**external_id** | **str** | The external Id. | 
**external_id_system** | **str** | The external Id system. | 
**title** | **str** | The collection title. | 
**provider_user** | **bool, date, datetime, dict, float, int, list, str, none_type** | Is the person who         is responsible for the content of this metadata record. Writer of the title and abstract. | [optional] 
**contact_user** | **bool, date, datetime, dict, float, int, list, str, none_type** | Is the person who         should be contacted in cases of questions regarding the content of the dataset or any data restrictions.         This is also the person who is most likely to stay involved in the dataset the longest. | [optional] 
**creator_users** | [**[MinUserModel]**](MinUserModel.md) | All people who         are responsible for the creation of the collection. Data creators should receive credit         for their work and should therefore be included in the citation. | [optional]  if omitted the server will use the default value of []
**creator_organisations** | **[str]** | All         organisations who are responsible for the creation of the collection. Data creators should         receive credit for their work and should therefore be included in the citation. | [optional]  if omitted the server will use the default value of []
**associate_users** | [**[MinUserModel]**](MinUserModel.md) | Other person(s)         associated with the collection. | [optional]  if omitted the server will use the default value of []
**associate_organisations** | **[str]** | Other         organisation(s) associated with the collection. | [optional]  if omitted the server will use the default value of []
**short_title** | **str** | The collection short title. | [optional] 
**citation** | **str** | The collection citation. | [optional] 
**license** | **str** | The collection license. | [optional] 
**abstract** | **str** | The collection abstract. | [optional] 
**description** | **str** | The collection description. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



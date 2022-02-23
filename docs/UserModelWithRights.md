# UserModelWithRights


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique numeric id of this user. | 
**email** | **str** | User&#39;s email address, as text, used during registration. | 
**name** | **str** | User&#39;s full name, as text. | 
**password** | **str** | Encrypted (or not) password. | [optional] 
**organisation** | **str** | User&#39;s organisation name, as text. | [optional] 
**active** | **bool** | Whether the user is still active. | [optional] 
**country** | **str** | The country name, as text (but chosen in a consistent list). | [optional] 
**usercreationdate** | **datetime** | The date of creation of the user, as text formatted according to the ISO 8601 standard. | [optional] 
**usercreationreason** | **str** | Paragraph describing the usage of EcoTaxa made by the user. | [optional] 
**can_do** | **[int]** | List of User&#39;s allowed actions : 1 create a project, 2 administrate the app, 3 administrate users, 4 create taxon. | [optional]  if omitted the server will use the default value of []
**last_used_projects** | [**[ProjectSummaryModel]**](ProjectSummaryModel.md) | List of User&#39;s last used projects. | [optional]  if omitted the server will use the default value of []
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



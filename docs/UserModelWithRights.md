# UserModelWithRights


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique user identifier | 
**email** | **str** | User&#39;s email used during registration | 
**name** | **str** | User&#39;s full name | 
**organisation** | **str** | User&#39;s organisation | [optional] 
**active** | **bool** | User&#39;s Account status | [optional] 
**country** | **str** | User&#39;s country | [optional] 
**usercreationdate** | **datetime** | User account creation date | [optional] 
**usercreationreason** | **str** | The reason of creation of this user account | [optional] 
**can_do** | **[int]** | List of User&#39;s allowed actions : 1 create a project, 2 administrate the app, 3 administrate users, 4 create taxon | [optional]  if omitted the server will use the default value of []
**last_used_projects** | [**[ProjectSummaryModel]**](ProjectSummaryModel.md) | List of User&#39;s last used projects | [optional]  if omitted the server will use the default value of []
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



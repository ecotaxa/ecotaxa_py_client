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
**can_do** | **list[int]** | List of User&#39;s allowed actions : 1 create a project, 2 administrate the app, 3 administrate users, 4 create taxon | [optional] [default to []]
**last_used_projects** | [**list[ProjectSummaryModel]**](ProjectSummaryModel.md) | List of User&#39;s last used projects | [optional] [default to []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



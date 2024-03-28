# UserModelWithRights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique numeric id of this user. | 
**email** | **str** | User&#39;s email address, as text, used during registration. | 
**password** | **str** | Encrypted (or not) password. | [optional] 
**name** | **str** | User&#39;s full name, as text. | 
**organisation** | **str** | User&#39;s organisation name, as text. | [optional] 
**status** | **int** | Status of the user : 1 for active, 0 for inactive ,2 for pending, -1 for blocked | [optional] 
**status_date** | **datetime** | Timestamp status modification date | [optional] 
**status_admin_comment** | **str** | Optional Users admininistrator comment about the account status. | [optional] 
**country** | **str** | The country name, as text (but chosen in a consistent list). | [optional] 
**orcid** | **str** | The orcid id https://support.orcid.org. | [optional] 
**usercreationdate** | **datetime** | The date of creation of the user, as text formatted according to the ISO 8601 standard. | [optional] 
**usercreationreason** | **str** | Paragraph describing the usage of EcoTaxa made by the user. | [optional] 
**mail_status** | **bool** | True for verified, False for waiting for verification, None for no action. | [optional] 
**mail_status_date** | **datetime** | Timestamp mail status modification date | [optional] 
**can_do** | **List[int]** | List of User&#39;s allowed actions : 1 create a project, 2 administrate the app, 3 administrate users, 4 create taxon. | [optional] [default to []]
**last_used_projects** | [**List[ProjectSummaryModel]**](ProjectSummaryModel.md) | List of User&#39;s last used projects. | [optional] [default to []]

## Example

```python
from ecotaxa_py_client.models.user_model_with_rights import UserModelWithRights

# TODO update the JSON string below
json = "{}"
# create an instance of UserModelWithRights from a JSON string
user_model_with_rights_instance = UserModelWithRights.from_json(json)
# print the JSON string representation of the object
print(UserModelWithRights.to_json())

# convert the object into a dict
user_model_with_rights_dict = user_model_with_rights_instance.to_dict()
# create an instance of UserModelWithRights from a dict
user_model_with_rights_form_dict = user_model_with_rights.from_dict(user_model_with_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



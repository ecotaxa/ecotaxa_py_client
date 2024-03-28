# UserActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**nb_actions** | **int** |  | [optional] 
**last_annot** | **str** |  | [optional] 

## Example

```python
from ecotaxa_py_client.models.user_activity import UserActivity

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivity from a JSON string
user_activity_instance = UserActivity.from_json(json)
# print the JSON string representation of the object
print(UserActivity.to_json())

# convert the object into a dict
user_activity_dict = user_activity_instance.to_dict()
# create an instance of UserActivity from a dict
user_activity_form_dict = user_activity.from_dict(user_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



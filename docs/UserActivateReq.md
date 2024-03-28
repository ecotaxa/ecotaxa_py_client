# UserActivateReq

Request to modify status of a user by a Users Administrator or confirm email_status, or resend emails (when token is expired) to confirm email or modify pending profile by a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | token when the user is not an admin and must confirm the email.  | [optional] 
**reason** | **str** | status,optional users administrator comment related to the status.  | [optional] 
**password** | **str** | Existing user can modify own email and must confirm it with token and password when email confirmation is on.  | [optional] 

## Example

```python
from ecotaxa_py_client.models.user_activate_req import UserActivateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivateReq from a JSON string
user_activate_req_instance = UserActivateReq.from_json(json)
# print the JSON string representation of the object
print(UserActivateReq.to_json())

# convert the object into a dict
user_activate_req_dict = user_activate_req_instance.to_dict()
# create an instance of UserActivateReq from a dict
user_activate_req_form_dict = user_activate_req.from_dict(user_activate_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



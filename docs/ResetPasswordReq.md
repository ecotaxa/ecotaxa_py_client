# ResetPasswordReq

Minimal user information need to reset the password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] [default to -1]
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from ecotaxa_py_client.models.reset_password_req import ResetPasswordReq

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPasswordReq from a JSON string
reset_password_req_instance = ResetPasswordReq.from_json(json)
# print the JSON string representation of the object
print(ResetPasswordReq.to_json())

# convert the object into a dict
reset_password_req_dict = reset_password_req_instance.to_dict()
# create an instance of ResetPasswordReq from a dict
reset_password_req_form_dict = reset_password_req.from_dict(reset_password_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



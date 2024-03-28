# LoginReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | User password. | 
**username** | **str** | User email used during registration. | 

## Example

```python
from ecotaxa_py_client.models.login_req import LoginReq

# TODO update the JSON string below
json = "{}"
# create an instance of LoginReq from a JSON string
login_req_instance = LoginReq.from_json(json)
# print the JSON string representation of the object
print(LoginReq.to_json())

# convert the object into a dict
login_req_dict = login_req_instance.to_dict()
# create an instance of LoginReq from a dict
login_req_form_dict = login_req.from_dict(login_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MinUserModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique numeric id of this user. | 
**email** | **str** | User&#39;s email address, as text, used during registration. | 
**name** | **str** | User&#39;s full name, as text. | 

## Example

```python
from ecotaxa_py_client.models.min_user_model import MinUserModel

# TODO update the JSON string below
json = "{}"
# create an instance of MinUserModel from a JSON string
min_user_model_instance = MinUserModel.from_json(json)
# print the JSON string representation of the object
print(MinUserModel.to_json())

# convert the object into a dict
min_user_model_dict = min_user_model_instance.to_dict()
# create an instance of MinUserModel from a dict
min_user_model_form_dict = min_user_model.from_dict(min_user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



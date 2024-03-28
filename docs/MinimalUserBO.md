# MinimalUserBO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from ecotaxa_py_client.models.minimal_user_bo import MinimalUserBO

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalUserBO from a JSON string
minimal_user_bo_instance = MinimalUserBO.from_json(json)
# print the JSON string representation of the object
print(MinimalUserBO.to_json())

# convert the object into a dict
minimal_user_bo_dict = minimal_user_bo_instance.to_dict()
# create an instance of MinimalUserBO from a dict
minimal_user_bo_form_dict = minimal_user_bo.from_dict(minimal_user_bo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



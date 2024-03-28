# CreateProjectReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_of_id** | **int** | Internal, numeric id of a project to clone as a new one. By default it does not clone anything. | [optional] 
**title** | **str** | The project title, as text. | 
**instrument** | **str** | The project instrument. | [optional] [default to '?']
**visible** | **bool** | When TRUE, the project is created visible by all users. | [optional] [default to True]

## Example

```python
from ecotaxa_py_client.models.create_project_req import CreateProjectReq

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectReq from a JSON string
create_project_req_instance = CreateProjectReq.from_json(json)
# print the JSON string representation of the object
print(CreateProjectReq.to_json())

# convert the object into a dict
create_project_req_dict = create_project_req_instance.to_dict()
# create an instance of CreateProjectReq from a dict
create_project_req_form_dict = create_project_req.from_dict(create_project_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



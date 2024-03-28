# CreateCollectionReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The collection title. | 
**project_ids** | **List[int]** | The list of composing project IDs. | 

## Example

```python
from ecotaxa_py_client.models.create_collection_req import CreateCollectionReq

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionReq from a JSON string
create_collection_req_instance = CreateCollectionReq.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionReq.to_json())

# convert the object into a dict
create_collection_req_dict = create_collection_req_instance.to_dict()
# create an instance of CreateCollectionReq from a dict
create_collection_req_form_dict = create_collection_req.from_dict(create_collection_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



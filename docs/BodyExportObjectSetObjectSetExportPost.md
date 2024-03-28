# BodyExportObjectSetObjectSetExportPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ProjectFilters**](ProjectFilters.md) |  | 
**request** | [**ExportReq**](ExportReq.md) |  | 

## Example

```python
from ecotaxa_py_client.models.body_export_object_set_object_set_export_post import BodyExportObjectSetObjectSetExportPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyExportObjectSetObjectSetExportPost from a JSON string
body_export_object_set_object_set_export_post_instance = BodyExportObjectSetObjectSetExportPost.from_json(json)
# print the JSON string representation of the object
print(BodyExportObjectSetObjectSetExportPost.to_json())

# convert the object into a dict
body_export_object_set_object_set_export_post_dict = body_export_object_set_object_set_export_post_instance.to_dict()
# create an instance of BodyExportObjectSetObjectSetExportPost from a dict
body_export_object_set_object_set_export_post_form_dict = body_export_object_set_object_set_export_post.from_dict(body_export_object_set_object_set_export_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



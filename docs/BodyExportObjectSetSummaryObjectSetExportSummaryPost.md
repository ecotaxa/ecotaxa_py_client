# BodyExportObjectSetSummaryObjectSetExportSummaryPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ProjectFilters**](ProjectFilters.md) |  | 
**request** | [**SummaryExportReq**](SummaryExportReq.md) |  | 

## Example

```python
from ecotaxa_py_client.models.body_export_object_set_summary_object_set_export_summary_post import BodyExportObjectSetSummaryObjectSetExportSummaryPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyExportObjectSetSummaryObjectSetExportSummaryPost from a JSON string
body_export_object_set_summary_object_set_export_summary_post_instance = BodyExportObjectSetSummaryObjectSetExportSummaryPost.from_json(json)
# print the JSON string representation of the object
print(BodyExportObjectSetSummaryObjectSetExportSummaryPost.to_json())

# convert the object into a dict
body_export_object_set_summary_object_set_export_summary_post_dict = body_export_object_set_summary_object_set_export_summary_post_instance.to_dict()
# create an instance of BodyExportObjectSetSummaryObjectSetExportSummaryPost from a dict
body_export_object_set_summary_object_set_export_summary_post_form_dict = body_export_object_set_summary_object_set_export_summary_post.from_dict(body_export_object_set_summary_object_set_export_summary_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



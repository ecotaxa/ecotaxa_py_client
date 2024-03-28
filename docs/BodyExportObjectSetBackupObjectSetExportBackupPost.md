# BodyExportObjectSetBackupObjectSetExportBackupPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ProjectFilters**](ProjectFilters.md) |  | 
**request** | [**BackupExportReq**](BackupExportReq.md) |  | 

## Example

```python
from ecotaxa_py_client.models.body_export_object_set_backup_object_set_export_backup_post import BodyExportObjectSetBackupObjectSetExportBackupPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyExportObjectSetBackupObjectSetExportBackupPost from a JSON string
body_export_object_set_backup_object_set_export_backup_post_instance = BodyExportObjectSetBackupObjectSetExportBackupPost.from_json(json)
# print the JSON string representation of the object
print(BodyExportObjectSetBackupObjectSetExportBackupPost.to_json())

# convert the object into a dict
body_export_object_set_backup_object_set_export_backup_post_dict = body_export_object_set_backup_object_set_export_backup_post_instance.to_dict()
# create an instance of BodyExportObjectSetBackupObjectSetExportBackupPost from a dict
body_export_object_set_backup_object_set_export_backup_post_form_dict = body_export_object_set_backup_object_set_export_backup_post.from_dict(body_export_object_set_backup_object_set_export_backup_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



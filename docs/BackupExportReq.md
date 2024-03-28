# BackupExportReq

Backup export request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project to export. | 
**out_to_ftp** | **bool** | Copy result file to FTP area. Original file is still available. | [optional] [default to False]

## Example

```python
from ecotaxa_py_client.models.backup_export_req import BackupExportReq

# TODO update the JSON string below
json = "{}"
# create an instance of BackupExportReq from a JSON string
backup_export_req_instance = BackupExportReq.from_json(json)
# print the JSON string representation of the object
print(BackupExportReq.to_json())

# convert the object into a dict
backup_export_req_dict = backup_export_req_instance.to_dict()
# create an instance of BackupExportReq from a dict
backup_export_req_form_dict = backup_export_req.from_dict(backup_export_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SimpleImportReq

Simple Import request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_path** | **str** | Source path on server, to zip or plain directory. | 
**values** | **Dict[str, str]** | :imgdate, imgtime, latitude, longitude, depthmin, depthmax, taxolb, userlb, status | 
**possible_values** | **List[str]** |  | [optional] [default to ["imgdate","imgtime","latitude","longitude","depthmin","depthmax","taxolb","userlb","status"]]

## Example

```python
from ecotaxa_py_client.models.simple_import_req import SimpleImportReq

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleImportReq from a JSON string
simple_import_req_instance = SimpleImportReq.from_json(json)
# print the JSON string representation of the object
print(SimpleImportReq.to_json())

# convert the object into a dict
simple_import_req_dict = simple_import_req_instance.to_dict()
# create an instance of SimpleImportReq from a dict
simple_import_req_form_dict = simple_import_req.from_dict(simple_import_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



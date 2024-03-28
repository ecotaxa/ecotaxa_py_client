# HistoricalLastClassif


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objid** | **int** | The object Id. | [optional] 
**classif_id** | **int** | The classification Id. | [optional] 
**histo_classif_date** | **datetime** | The classification date. | [optional] 
**histo_classif_type** | **str** | The type of classification. Could be **A** for Automatic or **M** for Manual. | [optional] 
**histo_classif_id** | **int** | The classification Id. | [optional] 
**histo_classif_qual** | **str** | The classification qualification. Could be **P** for predicted, **V** for validated or **D** for Dubious. | [optional] 
**histo_classif_who** | **int** | The user who manualy classify this object. | [optional] 

## Example

```python
from ecotaxa_py_client.models.historical_last_classif import HistoricalLastClassif

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalLastClassif from a JSON string
historical_last_classif_instance = HistoricalLastClassif.from_json(json)
# print the JSON string representation of the object
print(HistoricalLastClassif.to_json())

# convert the object into a dict
historical_last_classif_dict = historical_last_classif_instance.to_dict()
# create an instance of HistoricalLastClassif from a dict
historical_last_classif_form_dict = historical_last_classif.from_dict(historical_last_classif_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



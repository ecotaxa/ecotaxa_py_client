# SummaryExportReq

Summary export request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project to export. | 
**quantity** | [**SummaryExportQuantitiesOptionsEnum**](SummaryExportQuantitiesOptionsEnum.md) | The quantity to compute. Abundance is always possible. | [optional] 
**summarise_by** | [**SummaryExportSumOptionsEnum**](SummaryExportSumOptionsEnum.md) | Computations aggregation level. | [optional] 
**taxo_mapping** | **Dict[str, int]** | Mapping from present taxon (key) to output replacement one (value). Use a 0 replacement to _discard_ the present taxon. | [optional] 
**formulae** | **Dict[str, str]** | Transitory: How to get values from DB free columns. Python syntax, prefixes are &#39;sam&#39;, &#39;ssm&#39; and &#39;obj&#39;.Variables used in computations are &#39;total_water_volume&#39;, &#39;subsample_coef&#39; and &#39;individual_volume&#39; | [optional] 
**out_to_ftp** | **bool** | Copy result file to FTP area. Original file is still available. | [optional] [default to False]

## Example

```python
from ecotaxa_py_client.models.summary_export_req import SummaryExportReq

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryExportReq from a JSON string
summary_export_req_instance = SummaryExportReq.from_json(json)
# print the JSON string representation of the object
print(SummaryExportReq.to_json())

# convert the object into a dict
summary_export_req_dict = summary_export_req_instance.to_dict()
# create an instance of SummaryExportReq from a dict
summary_export_req_form_dict = summary_export_req.from_dict(summary_export_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ExportReq

Export request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project to export. | 
**exp_type** | [**ExportTypeEnum**](ExportTypeEnum.md) | The export type. | 
**use_latin1** | **bool** | Export using latin 1 character set, AKA iso-8859-1. Default is utf-8. | [optional] [default to False]
**tsv_entities** | **str** | For &#39;TSV&#39; type, the entities to export, one letter for each of O(bject), P(rocess), A(cquisition), S(ample), C(omments). | [optional] [default to '']
**only_annotations** | **bool** | For &#39;BAK&#39; type, only save objects&#39; last annotation data in backup. | [optional] [default to False]
**split_by** | **str** | For &#39;TSV&#39; type, inside archives, split in one directory per... &#39;sample&#39;, &#39;acquisition&#39;, &#39;taxon&#39; or &#39;&#39; (no split). | [optional] [default to '']
**coma_as_separator** | **bool** | For &#39;TSV&#39; type, use a , instead of . for decimal separator. | [optional] [default to False]
**format_dates_times** | **bool** | For &#39;TSV&#39; type, format dates and times using - and : respectively. | [optional] [default to True]
**with_images** | **bool** | For &#39;BAK&#39; and &#39;DOI&#39; types, export images as well. | [optional] [default to False]
**with_internal_ids** | **bool** | For &#39;TSV&#39; type, export internal DB IDs. | [optional] [default to False]
**with_types_row** | **bool** | Add an EcoTaxa-compatible second line with types. | [optional] [default to False]
**only_first_image** | **bool** | For &#39;DOI&#39; type, export only first (displayed) image. | [optional] [default to False]
**sum_subtotal** | [**SummaryExportGroupingEnum**](SummaryExportGroupingEnum.md) | For &#39;SUM&#39;, &#39;ABO&#39;, &#39;CNC&#39; and &#39;BIV&#39; types, if computations should be combined. Per A(cquisition) or S(ample) or &lt;Empty&gt;(just taxa). | [optional] 
**pre_mapping** | **Dict[str, int]** | For &#39;ABO&#39;, &#39;CNC&#39; and &#39;BIV&#39; types types, mapping from present taxon (key) to output replacement one (value). Use a null replacement to _discard_ the present taxon. | [optional] 
**formulae** | **Dict[str, str]** | Transitory: For &#39;CNC&#39; and &#39;BIV&#39; type, how to get values from DB free columns. Python syntax, prefixes are &#39;sam&#39;, &#39;ssm&#39; and &#39;obj&#39;.Variables used in computations are &#39;total_water_volume&#39;, &#39;subsample_coef&#39; and &#39;individual_volume&#39; | [optional] 
**out_to_ftp** | **bool** | Copy result file to FTP area. Original file is still available. | [optional] [default to False]

## Example

```python
from ecotaxa_py_client.models.export_req import ExportReq

# TODO update the JSON string below
json = "{}"
# create an instance of ExportReq from a JSON string
export_req_instance = ExportReq.from_json(json)
# print the JSON string representation of the object
print(ExportReq.to_json())

# convert the object into a dict
export_req_dict = export_req_instance.to_dict()
# create an instance of ExportReq from a dict
export_req_form_dict = export_req.from_dict(export_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



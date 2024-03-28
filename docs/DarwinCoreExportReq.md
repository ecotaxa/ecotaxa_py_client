# DarwinCoreExportReq

Darwin Core format export request, only allowed format for a Collection. @see https://dwc.tdwg.org/

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **int** | The collection to export, by its internal Id. | 
**dry_run** | **bool** | If set, then only a diagnostic of doability will be done. | [optional] [default to False]
**include_predicted** | **bool** | If set, then predicted objects, as well as validated ones, will be exported. A validation status will allow to distinguish between the two possible statuses. | [optional] [default to False]
**with_absent** | **bool** | If set, then *absent* records will be generated, in the relevant samples, for categories present in other samples. | [optional] [default to False]
**with_computations** | [**List[SciExportTypeEnum]**](SciExportTypeEnum.md) | Compute organisms abundances (ABO), concentrations (CNC) or biovolumes (BIV). Several possible. | [optional] [default to []]
**computations_pre_mapping** | **Dict[str, int]** | Mapping from present taxon (key) to output replacement one (value), during computations. Use a 0 replacement to _discard_ the objects with present taxon. Note: These are EcoTaxa categories, WoRMS mapping happens after, whatever. | [optional] 
**formulae** | **Dict[str, str]** | Transitory: How to get values from DB free columns. Python syntax, prefixes are &#39;sam&#39;, &#39;ssm&#39; and &#39;obj&#39;. Variables used in computations are &#39;total_water_volume&#39;, &#39;subsample_coef&#39; and &#39;individual_volume&#39; | [optional] 
**extra_xml** | **List[str]** | XML blocks which will be output, reformatted, inside the &lt;dataset&gt; tag of produced EML. Formal schema is in dataset section of: https://eml.ecoinformatics.org/schema/eml_xsd  | [optional] [default to []]

## Example

```python
from ecotaxa_py_client.models.darwin_core_export_req import DarwinCoreExportReq

# TODO update the JSON string below
json = "{}"
# create an instance of DarwinCoreExportReq from a JSON string
darwin_core_export_req_instance = DarwinCoreExportReq.from_json(json)
# print the JSON string representation of the object
print(DarwinCoreExportReq.to_json())

# convert the object into a dict
darwin_core_export_req_dict = darwin_core_export_req_instance.to_dict()
# create an instance of DarwinCoreExportReq from a dict
darwin_core_export_req_form_dict = darwin_core_export_req.from_dict(darwin_core_export_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



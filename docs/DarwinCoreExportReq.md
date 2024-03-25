# DarwinCoreExportReq

Darwin Core format export request, only allowed format for a Collection. @see https://dwc.tdwg.org/

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **int** | The collection to export, by its internal Id. | 
**dry_run** | **bool** | If set, then only a diagnostic of doability will be done. | [optional]  if omitted the server will use the default value of False
**include_predicted** | **bool** | If set, then predicted objects, as well as validated ones, will be exported. A validation status will allow to distinguish between the two possible statuses. | [optional]  if omitted the server will use the default value of False
**with_absent** | **bool** | If set, then *absent* records will be generated, in the relevant samples, for categories present in other samples. | [optional]  if omitted the server will use the default value of False
**with_computations** | [**[SciExportTypeEnum]**](SciExportTypeEnum.md) | Compute organisms abundances (ABO), concentrations (CNC) or biovolumes (BIV). Several possible. | [optional]  if omitted the server will use the default value of []
**computations_pre_mapping** | **{str: (int,)}** | Mapping from present taxon (key) to output replacement one (value), during computations. Use a 0 replacement to _discard_ the objects with present taxon. Note: These are EcoTaxa categories, WoRMS mapping happens after, whatever. | [optional]  if omitted the server will use the default value of {}
**formulae** | **{str: (str,)}** | Transitory: How to get values from DB free columns. Python syntax, prefixes are &#39;sam&#39;, &#39;ssm&#39; and &#39;obj&#39;. Variables used in computations are &#39;total_water_volume&#39;, &#39;subsample_coef&#39; and &#39;individual_volume&#39; | [optional]  if omitted the server will use the default value of {}
**extra_xml** | **[str]** | XML blocks which will be output, reformatted, inside the &lt;dataset&gt; tag of produced EML. Formal schema is in dataset section of: https://eml.ecoinformatics.org/schema/eml_xsd  | [optional]  if omitted the server will use the default value of []

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



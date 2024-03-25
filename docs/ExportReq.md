# ExportReq

Export request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project to export. | 
**exp_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The export type. | 
**use_latin1** | **bool** | Export using latin 1 character set, AKA iso-8859-1. Default is utf-8. | [optional]  if omitted the server will use the default value of False
**tsv_entities** | **str** | For &#39;TSV&#39; type, the entities to export, one letter for each of O(bject), P(rocess), A(cquisition), S(ample), C(omments). | [optional]  if omitted the server will use the default value of ""
**only_annotations** | **bool** | For &#39;BAK&#39; type, only save objects&#39; last annotation data in backup. | [optional]  if omitted the server will use the default value of False
**split_by** | **str** | For &#39;TSV&#39; type, inside archives, split in one directory per... &#39;sample&#39;, &#39;acquisition&#39;, &#39;taxon&#39; or &#39;&#39; (no split). | [optional]  if omitted the server will use the default value of ""
**coma_as_separator** | **bool** | For &#39;TSV&#39; type, use a , instead of . for decimal separator. | [optional]  if omitted the server will use the default value of False
**format_dates_times** | **bool** | For &#39;TSV&#39; type, format dates and times using - and : respectively. | [optional]  if omitted the server will use the default value of True
**with_images** | **bool** | For &#39;BAK&#39; and &#39;DOI&#39; types, export images as well. | [optional]  if omitted the server will use the default value of False
**with_internal_ids** | **bool** | For &#39;TSV&#39; type, export internal DB IDs. | [optional]  if omitted the server will use the default value of False
**with_types_row** | **bool** | Add an EcoTaxa-compatible second line with types. | [optional]  if omitted the server will use the default value of False
**only_first_image** | **bool** | For &#39;DOI&#39; type, export only first (displayed) image. | [optional]  if omitted the server will use the default value of False
**sum_subtotal** | **bool, date, datetime, dict, float, int, list, str, none_type** | For &#39;SUM&#39;, &#39;ABO&#39;, &#39;CNC&#39; and &#39;BIV&#39; types, if computations should be combined. Per A(cquisition) or S(ample) or &lt;Empty&gt;(just taxa). | [optional] 
**pre_mapping** | **{str: (int,)}** | For &#39;ABO&#39;, &#39;CNC&#39; and &#39;BIV&#39; types types, mapping from present taxon (key) to output replacement one (value). Use a null replacement to _discard_ the present taxon. | [optional]  if omitted the server will use the default value of {}
**formulae** | **{str: (str,)}** | Transitory: For &#39;CNC&#39; and &#39;BIV&#39; type, how to get values from DB free columns. Python syntax, prefixes are &#39;sam&#39;, &#39;ssm&#39; and &#39;obj&#39;.Variables used in computations are &#39;total_water_volume&#39;, &#39;subsample_coef&#39; and &#39;individual_volume&#39; | [optional]  if omitted the server will use the default value of {}
**out_to_ftp** | **bool** | Copy result file to FTP area. Original file is still available. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



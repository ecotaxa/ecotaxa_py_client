# ExportReq

Export request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The project to export. | 
**exp_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The export type. | 
**tsv_entities** | **str** | For &#39;TSV&#39; type, the entities to export, one letter for each of O(bject), P(rocess), A(cquisition), S(ample), classification H(istory), C(omments). | 
**split_by** | **str** | For &#39;TSV&#39; type, inside archives, split in one directory per... &#39;sample&#39;, &#39;taxo&#39; or &#39;&#39; (no split). | 
**coma_as_separator** | **bool** | For &#39;TSV&#39; type, use a , instead of . for decimal separator. | 
**format_dates_times** | **bool** | For &#39;TSV&#39; type, format dates and times using - and : respectively. | 
**with_images** | **bool** | For &#39;BAK&#39; and &#39;DOI&#39; types, export images as well. | 
**with_internal_ids** | **bool** | For &#39;BAK&#39; and &#39;DOI&#39; types, export internal DB IDs. | 
**only_first_image** | **bool** | For &#39;DOI&#39; type, export only first (displayed) image. | 
**sum_subtotal** | **bool, date, datetime, dict, float, int, list, str, none_type** | For &#39;SUM&#39;, &#39;ABO&#39;, &#39;CNC&#39; and &#39;BIV&#39; types, if computations should be combined. Per A(cquisition) or S(ample) or &lt;Empty&gt;(just taxa). | 
**out_to_ftp** | **bool** | Copy result file to FTP area. Original file is still available. | 
**use_latin1** | **bool** | Export using latin 1 character set, AKA iso-8859-1. Default is utf-8. | [optional]  if omitted the server will use the default value of False
**pre_mapping** | **{str: (int,)}** | For &#39;ABO&#39;, &#39;CNC&#39; and &#39;BIV&#39; types types, mapping from present taxon (key) to output replacement one (value). Use a null replacement to _discard_ the present taxon. | [optional]  if omitted the server will use the default value of {}
**formulae** | **{str: (str,)}** | Transitory: For &#39;CNC&#39; and &#39;BIV&#39; type, how to get values from DB free columns. Python syntax, prefixes are &#39;sam&#39;, &#39;ssm&#39; and &#39;obj&#39;.Variables used in computations are &#39;total_water_volume&#39;, &#39;subsample_coef&#39; and &#39;individual_volume&#39; | [optional]  if omitted the server will use the default value of {}
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



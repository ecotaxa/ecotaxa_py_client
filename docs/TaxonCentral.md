# TaxonCentral


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique numeric id of the taxon. | 
**name** | **str** | The name of the taxon. | 
**taxotype** | **str** | The taxon type, &#39;M&#39; for Morpho or &#39;P&#39; for Phylo. | 
**taxostatus** | **str** | The taxon status, N for Not approved, A for Approved or D for Deprecated. | 
**parent_id** | **int** | The unique numeric id of the taxon parent. | [optional] 
**id_source** | **str** | The source ID. | [optional] 
**display_name** | **str** | The display name of the taxon. It is suffixed in EcoTaxoServer with (Deprecated) when taxostatus is &#39;D&#39; | [optional] 
**lastupdate_datetime** | **datetime** | Taxon last update. Date, with format YYYY-MM-DD hh:mm:ss. | [optional] 
**id_instance** | **int** | The instance Id. | [optional] 
**rename_to** | **int** | The advised replacement Name if the taxon is deprecated. | [optional] 
**source_url** | **str** | The source url. | [optional] 
**source_desc** | **str** | The source description. | [optional] 
**creator_email** | **str** | Email of the creator of the taxon. | [optional] 
**creation_datetime** | **datetime** | Taxon creation date. Date, with format YYYY-MM-DD hh:mm:ss. | [optional] 
**nbrobj** | **int** | Number of objects in this category exactly. | [optional] 
**nbrobjcum** | **int** | Number of objects in this category and descendant ones. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



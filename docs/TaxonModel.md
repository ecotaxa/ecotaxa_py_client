# TaxonModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The taxon/category IDs. | 
**name** | **str** | The taxon/category verbatim name. | 
**type** | **str** | The taxon/category type, &#39;M&#39; for Morpho or &#39;P&#39; for Phylo. | 
**nb_objects** | **int** | How many objects are classified in this category. | 
**nb_children_objects** | **int** | How many objects are classified in this category children (not itself). | 
**display_name** | **str** | The taxon/category display name. | 
**lineage** | **[str]** | The taxon/category name of ancestors, including self, in first. | 
**id_lineage** | **[int]** | The taxon/category IDs of ancestors, including self, in first. | 
**children** | **[int]** | The taxon/category IDs of children. | 
**renm_id** | **int** | The advised replacement ID if the taxon/category is deprecated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



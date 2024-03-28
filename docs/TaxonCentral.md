# TaxonCentral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique numeric id of the taxon. | 
**parent_id** | **int** | The unique numeric id of the taxon parent. | [optional] 
**name** | **str** | The name of the taxon. | 
**id_source** | **str** | The source ID. | [optional] 
**taxotype** | **str** | The taxon type, &#39;M&#39; for Morpho or &#39;P&#39; for Phylo. | 
**display_name** | **str** | The display name of the taxon. It is suffixed in EcoTaxoServer with (Deprecated) when taxostatus is &#39;D&#39; | [optional] 
**lastupdate_datetime** | **datetime** | Taxon last update. Date, with format YYYY-MM-DD hh:mm:ss. | [optional] 
**id_instance** | **int** | The instance Id. | [optional] 
**taxostatus** | **str** | The taxon status, N for Not approved, A for Approved or D for Deprecated. | 
**rename_to** | **int** | The advised replacement Name if the taxon is deprecated. | [optional] 
**source_url** | **str** | The source url. | [optional] 
**source_desc** | **str** | The source description. | [optional] 
**creator_email** | **str** | Email of the creator of the taxon. | [optional] 
**creation_datetime** | **datetime** | Taxon creation date. Date, with format YYYY-MM-DD hh:mm:ss. | [optional] 
**nbrobj** | **int** | Number of objects in this category exactly. | [optional] 
**nbrobjcum** | **int** | Number of objects in this category and descendant ones. | [optional] 

## Example

```python
from ecotaxa_py_client.models.taxon_central import TaxonCentral

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonCentral from a JSON string
taxon_central_instance = TaxonCentral.from_json(json)
# print the JSON string representation of the object
print(TaxonCentral.to_json())

# convert the object into a dict
taxon_central_dict = taxon_central_instance.to_dict()
# create an instance of TaxonCentral from a dict
taxon_central_form_dict = taxon_central.from_dict(taxon_central_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



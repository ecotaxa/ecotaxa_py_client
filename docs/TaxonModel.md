# TaxonModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The taxon/category IDs. | 
**renm_id** | **int** | The advised replacement ID if the taxon/category is deprecated. | [optional] 
**name** | **str** | The taxon/category verbatim name. | 
**type** | **str** | The taxon/category type, &#39;M&#39; for Morpho or &#39;P&#39; for Phylo. | 
**nb_objects** | **int** | How many objects are classified in this category. | 
**nb_children_objects** | **int** | How many objects are classified in this category children (not itself). | 
**display_name** | **str** | The taxon/category display name. | 
**lineage** | **List[str]** | The taxon/category name of ancestors, including self, in first. | 
**id_lineage** | **List[int]** | The taxon/category IDs of ancestors, including self, in first. | 
**children** | **List[int]** | The taxon/category IDs of children. | 

## Example

```python
from ecotaxa_py_client.models.taxon_model import TaxonModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonModel from a JSON string
taxon_model_instance = TaxonModel.from_json(json)
# print the JSON string representation of the object
print(TaxonModel.to_json())

# convert the object into a dict
taxon_model_dict = taxon_model_instance.to_dict()
# create an instance of TaxonModel from a dict
taxon_model_form_dict = taxon_model.from_dict(taxon_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



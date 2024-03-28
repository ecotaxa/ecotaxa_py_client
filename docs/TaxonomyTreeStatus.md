# TaxonomyTreeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_refresh** | **str** | Taxonomy tree last refresh/sync from taxonomy server. Date, with format YYYY-MM-DDThh:mm:ss. | [optional] 

## Example

```python
from ecotaxa_py_client.models.taxonomy_tree_status import TaxonomyTreeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyTreeStatus from a JSON string
taxonomy_tree_status_instance = TaxonomyTreeStatus.from_json(json)
# print the JSON string representation of the object
print(TaxonomyTreeStatus.to_json())

# convert the object into a dict
taxonomy_tree_status_dict = taxonomy_tree_status_instance.to_dict()
# create an instance of TaxonomyTreeStatus from a dict
taxonomy_tree_status_form_dict = taxonomy_tree_status.from_dict(taxonomy_tree_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



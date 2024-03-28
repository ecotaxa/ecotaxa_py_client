# TaxonomyRecast

In various contexts, a taxo recast (from taxon -> to taxon) setting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_to** | **Dict[str, int]** | Mapping from seen taxon (key) to output replacement one (value). Use a null replacement to _discard_ the present taxon. Note: keys are strings. | 
**doc** | **Dict[str, str]** | To keep memory of the reasons for the above mapping. Note: keys are strings. | [optional] 

## Example

```python
from ecotaxa_py_client.models.taxonomy_recast import TaxonomyRecast

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyRecast from a JSON string
taxonomy_recast_instance = TaxonomyRecast.from_json(json)
# print the JSON string representation of the object
print(TaxonomyRecast.to_json())

# convert the object into a dict
taxonomy_recast_dict = taxonomy_recast_instance.to_dict()
# create an instance of TaxonomyRecast from a dict
taxonomy_recast_form_dict = taxonomy_recast.from_dict(taxonomy_recast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TaxaSearchRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The taxon/category IDs. | 
**renm_id** | **int** | The advised replacement ID if the taxon/category is deprecated. | [optional] 
**text** | **str** | The taxon name, display one. | 
**pr** | **int** | 1 if the taxon is in project list, 0 otherwise. | 

## Example

```python
from ecotaxa_py_client.models.taxa_search_rsp import TaxaSearchRsp

# TODO update the JSON string below
json = "{}"
# create an instance of TaxaSearchRsp from a JSON string
taxa_search_rsp_instance = TaxaSearchRsp.from_json(json)
# print the JSON string representation of the object
print(TaxaSearchRsp.to_json())

# convert the object into a dict
taxa_search_rsp_dict = taxa_search_rsp_instance.to_dict()
# create an instance of TaxaSearchRsp from a dict
taxa_search_rsp_form_dict = taxa_search_rsp.from_dict(taxa_search_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



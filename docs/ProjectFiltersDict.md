# ProjectFiltersDict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxo** | **str** |  | [optional] 
**taxochild** | **str** |  | [optional] 
**statusfilter** | **str** |  | [optional] 
**map_n** | **str** |  | [optional] 
**map_w** | **str** |  | [optional] 
**map_e** | **str** |  | [optional] 
**map_s** | **str** |  | [optional] 
**depthmin** | **str** |  | [optional] 
**depthmax** | **str** |  | [optional] 
**samples** | **str** |  | [optional] 
**instrum** | **str** |  | [optional] 
**daytime** | **str** |  | [optional] 
**month** | **str** |  | [optional] 
**fromdate** | **str** |  | [optional] 
**todate** | **str** |  | [optional] 
**fromtime** | **str** |  | [optional] 
**totime** | **str** |  | [optional] 
**inverttime** | **str** |  | [optional] 
**validfromdate** | **str** |  | [optional] 
**validtodate** | **str** |  | [optional] 
**freenum** | **str** |  | [optional] 
**freenumst** | **str** |  | [optional] 
**freenumend** | **str** |  | [optional] 
**freetxt** | **str** |  | [optional] 
**freetxtval** | **str** |  | [optional] 
**filt_annot** | **str** |  | [optional] 
**filt_last_annot** | **str** |  | [optional] 

## Example

```python
from ecotaxa_py_client.models.project_filters_dict import ProjectFiltersDict

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectFiltersDict from a JSON string
project_filters_dict_instance = ProjectFiltersDict.from_json(json)
# print the JSON string representation of the object
print(ProjectFiltersDict.to_json())

# convert the object into a dict
project_filters_dict_dict = project_filters_dict_instance.to_dict()
# create an instance of ProjectFiltersDict from a dict
project_filters_dict_form_dict = project_filters_dict.from_dict(project_filters_dict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



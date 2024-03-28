# ProjectFilters

How to reduce project data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxo** | **str** | Coma-separated list of numeric taxonomy/category ids. Only include objects classified with one of them. | [optional] 
**taxochild** | **str** | If &#39;Y&#39; and taxo is set, also include children of each member of &#39;taxo&#39; list in taxonomy tree. | [optional] 
**statusfilter** | **str** | Include objects with given status:             &#39;NV&#39;: Not validated              &#39;PV&#39;: Predicted or Validated              &#39;PVD&#39;: Predicted or Validated or Dubious             &#39;NVM&#39;: Validated, but not by me              &#39;VM&#39;: Validated by me              &#39;U&#39;: Not classified             other: direct equality comparison with DB value           | [optional] 
**map_n** | **str** | If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle. | [optional] 
**map_w** | **str** | If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle. | [optional] 
**map_e** | **str** | If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle. | [optional] 
**map_s** | **str** | If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle. | [optional] 
**depthmin** | **str** | Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range. | [optional] 
**depthmax** | **str** | Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range. | [optional] 
**samples** | **str** | Coma-separated list of sample IDs, include only objects for these samples. | [optional] 
**instrum** | **str** | Instrument name, include objects for which sampling was done using this instrument. | [optional] 
**daytime** | **str** | Coma-separated list of sun position values: D for Day, U for Dusk, N for Night, A for Dawn (Aube in French). | [optional] 
**month** | **str** | Coma-separated list of month numbers, 1&#x3D;Jan and so on. | [optional] 
**fromdate** | **str** | Format is &#39;YYYY-MM-DD&#39;, include objects collected after this date. | [optional] 
**todate** | **str** | Format is &#39;YYYY-MM-DD&#39;, include objects collected before this date. | [optional] 
**fromtime** | **str** | Format is &#39;HH24:MM:SS&#39;, include objects collected after this time of day. | [optional] 
**totime** | **str** | Format is &#39;HH24:MM:SS&#39;, include objects collected before this time of day. | [optional] 
**inverttime** | **str** | If &#39;1&#39;, include objects outside fromtime and totime range. | [optional] 
**validfromdate** | **str** | Format is &#39;YYYY-MM-DD HH24:MI&#39;, include objects validated/set to dubious after this date+time. | [optional] 
**validtodate** | **str** | Format is &#39;YYYY-MM-DD HH24:MI&#39;, include objects validated/set to dubious before this date+time. | [optional] 
**freenum** | **str** | Numerical DB column number in Object as basis for the 2 following criteria (freenumst, freenumend). | [optional] 
**freenumst** | **str** | Start of included range for the column defined by freenum, in which objects are included. | [optional] 
**freenumend** | **str** | End of included range for the column defined by freenum, in which objects are included. | [optional] 
**freetxt** | **str** |  Textual DB column number as basis for following criteria (freetxtval)             If starts with &#39;s&#39; then it&#39;s a text column in Sample             If starts with &#39;a&#39; then it&#39;s a text column in Acquisition              If starts with &#39;p&#39; then it&#39;s a text column in Process              If starts with &#39;o&#39; then it&#39;s a text column in Object .          | [optional] 
**freetxtval** | **str** | Text to match in the column defined by freetxt, for an object to be include. | [optional] 
**filt_annot** | **str** | Coma-separated list of annotators, i.e. persons who validated the classification at any point in time. | [optional] 
**filt_last_annot** | **str** | Coma-separated list of annotators, i.e. persons who validated the classification in last. | [optional] 

## Example

```python
from ecotaxa_py_client.models.project_filters import ProjectFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectFilters from a JSON string
project_filters_instance = ProjectFilters.from_json(json)
# print the JSON string representation of the object
print(ProjectFilters.to_json())

# convert the object into a dict
project_filters_dict = project_filters_instance.to_dict()
# create an instance of ProjectFilters from a dict
project_filters_form_dict = project_filters.from_dict(project_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



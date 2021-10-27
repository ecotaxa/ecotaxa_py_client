# PredictionReq

How to predict, in details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The destination project, of which objects will be predicted. | 
**source_project_ids** | **[int]** | The source projects, objects in them will serve as reference. | 
**features** | **[str]** | The object features AKA free column, to use in the algorithm. Features must be common to all projects, source ones and destination one. | 
**categories** | **[int]** | In source projects, only objects validated with these categories will be considered. | 
**pre_mapping** | **{str: (int,)}** | Categories in keys become value one before launching the ML algorithm. Any unknown value is ignored. | 
**learning_limit** | **int** | When set (to a positive value), there will be this number  of objects, _per category_, in the learning set. | [optional] 
**use_scn** | **bool** | Use extra features, generated using the image, for improving the prediction. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



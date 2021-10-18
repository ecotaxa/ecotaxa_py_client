# ObjectModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objid** | **int** | The object Id. | 
**acquisid** | **int** | The parent acquisition Id. | 
**orig_id** | **str** | Original object ID from initial TSV load. | 
**sample_id** | **int** | Sample (i.e. parent of parent acquisition) ID. | 
**project_id** | **int** | Project (i.e. parent of sample) ID. | 
**objdate** | **date** |  | [optional] 
**objtime** | **str** |  | [optional] 
**latitude** | **float** | The latitude. | [optional] 
**longitude** | **float** | The longitude. | [optional] 
**depth_min** | **float** | The min depth. | [optional] 
**depth_max** | **float** | The min depth. | [optional] 
**sunpos** | **str** | Sun position, from date, time and coords. | [optional] 
**classif_id** | **int** | The classification Id. | [optional] 
**classif_qual** | **str** | The classification qualification. Could be **P** for predicted, **V** for validated or **D** for Dubious. | [optional] 
**classif_who** | **int** | The user who manualy classify this object. | [optional] 
**classif_when** | **datetime** | The classification date. | [optional] 
**classif_auto_id** | **int** | Set if the object was ever predicted, remain forever with these value. Reflect the &#39;last state&#39; only if classif_qual is &#39;P&#39;.  | [optional] 
**classif_auto_score** | **float** | Set if the object was ever predicted, remain forever with these value. Reflect the &#39;last state&#39; only if classif_qual is &#39;P&#39;. The classification auto score is generally between 0 and 1. This is a confidence score, in the fact that, the taxon prediction for this object is correct. | [optional] 
**classif_auto_when** | **datetime** | Set if the object was ever predicted, remain forever with these value. Reflect the &#39;last state&#39; only if classif_qual is &#39;P&#39;. The classification date. | [optional] 
**classif_crossvalidation_id** | **int** | Always NULL in prod. | [optional] 
**complement_info** | **str** |  | [optional] 
**similarity** | **float** | Always NULL in prod. | [optional] 
**random_value** | **int** |  | [optional] 
**object_link** | **str** | Object link. | [optional] 
**images** | [**[ImageModel]**](ImageModel.md) | Images for this object. | [optional]  if omitted the server will use the default value of []
**free_columns** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Free columns from object mapping in project. | [optional]  if omitted the server will use the default value of {}
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# HistoricalClassification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objid** | **int** | The object Id. | [optional] 
**classif_id** | **int** | The classification Id. | [optional] 
**classif_date** | **datetime** | The classification date. | [optional] 
**classif_who** | **int** | The user who manualy classify this object. | [optional] 
**classif_type** | **str** | The type of classification. Could be **A** for Automatic or **M** for Manual. | [optional] 
**classif_qual** | **str** | The classification qualification. Could be **P** for predicted, **V** for validated or **D** for Dubious. | [optional] 
**classif_score** | **float** | The classification score is generally between 0 and 1. This is a confidence score, in the fact that, the taxon prediction for this object is correct. | [optional] 
**user_name** | **str** | The name of the user who classified this object. | [optional] 
**taxon_name** | **str** | The taxon name of the object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



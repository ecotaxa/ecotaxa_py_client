# ProjectModel

Basic and computed information about the Project.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license** | **str** |  | 
**projid** | **int** | The project Id. | 
**title** | **str** | The project title. | 
**obj_free_cols** | **{str: (str,)}** | Object free columns. | [optional]  if omitted the server will use the default value of {}
**sample_free_cols** | **{str: (str,)}** | Sample free columns. | [optional]  if omitted the server will use the default value of {}
**acquisition_free_cols** | **{str: (str,)}** | Acquisition free columns. | [optional]  if omitted the server will use the default value of {}
**process_free_cols** | **{str: (str,)}** | Process free columns. | [optional]  if omitted the server will use the default value of {}
**init_classif_list** | **[int]** | Favorite taxa used in classification. | [optional]  if omitted the server will use the default value of []
**managers** | [**[UserModel]**](UserModel.md) | Managers of this project. | [optional]  if omitted the server will use the default value of []
**annotators** | [**[UserModel]**](UserModel.md) | Annotators of this project, if not manager. | [optional]  if omitted the server will use the default value of []
**viewers** | [**[UserModel]**](UserModel.md) | Viewers of this project, if not manager nor annotator. | [optional]  if omitted the server will use the default value of []
**instrument** | **str** | This project&#39;s instrument. Transitory: if several of them, then coma-separated. | [optional] 
**contact** | **dict** | The contact person is a manager who serves as the contact person for other users and EcoTaxa&#39;s managers. | [optional] 
**highest_right** | **str** | The highest right for requester on this project. One of &#39;Manage&#39;, &#39;Annotate&#39;, &#39;View&#39;. | [optional]  if omitted the server will use the default value of ""
**visible** | **bool** | The project visibility. | [optional] 
**status** | **str** | The project status. | [optional] 
**objcount** | **float** | The number of objects. | [optional] 
**pctvalidated** | **float** | Percentage of validated images. | [optional] 
**pctclassified** | **float** | Percentage of classified images. | [optional] 
**classifsettings** | **str** |  | [optional] 
**classiffieldlist** | **str** |  | [optional] 
**popoverfieldlist** | **str** |  | [optional] 
**comments** | **str** | The project comments. | [optional] 
**description** | **str** | The project description, i.e. main traits. | [optional] 
**rf_models_used** | **str** |  | [optional] 
**cnn_network_id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



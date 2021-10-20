# ProjectModel

Project + computed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_free_cols** | **dict(str, str)** | Object free columns | [optional] 
**sample_free_cols** | **dict(str, str)** | Sample free columns | [optional] 
**acquisition_free_cols** | **dict(str, str)** | Acquisition free columns | [optional] 
**process_free_cols** | **dict(str, str)** | Process free columns | [optional] 
**init_classif_list** | **list[int]** | Favorite taxa used in classification | [optional] [default to []]
**managers** | [**list[UserModel]**](UserModel.md) | Managers of this project | [optional] [default to []]
**annotators** | [**list[UserModel]**](UserModel.md) | Annotators of this project, if not manager | [optional] [default to []]
**viewers** | [**list[UserModel]**](UserModel.md) | Viewers of this project, if not manager nor annotator | [optional] [default to []]
**instrument** | **str** | This project&#39;s instrument. Transitory: if several of them, then coma-separated | [optional] 
**contact** | [**UserModel**](UserModel.md) | The contact person is a manager who serves as the contact person for other users and EcoTaxa&#39;s managers. | [optional] 
**highest_right** | **str** | The highest right for requester on this project. One of &#39;Manage&#39;, &#39;Annotate&#39;, &#39;View&#39;. | [optional] [default to '']
**license** | **str** |  | 
**projid** | **int** | The project Id | 
**title** | **str** | The project title | 
**visible** | **bool** | The project visibility | [optional] 
**status** | **str** | The project status | [optional] 
**objcount** | **float** | The number of objects | [optional] 
**pctvalidated** | **float** | Percentage of validated images. | [optional] 
**pctclassified** | **float** | Percentage of classified images. | [optional] 
**classifsettings** | **str** |  | [optional] 
**classiffieldlist** | **str** |  | [optional] 
**popoverfieldlist** | **str** |  | [optional] 
**comments** | **str** | The project comments | [optional] 
**projtype** | **str** | The type of the project | [optional] 
**rf_models_used** | **str** |  | [optional] 
**cnn_network_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



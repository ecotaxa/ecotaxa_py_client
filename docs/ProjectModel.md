# ProjectModel

Basic and computed information about the Project.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projid** | **int** | The project Id. | 
**title** | **str** | The project title. | 
**obj_free_cols** | **{str: (str,)}** | Object free columns. | [optional]  if omitted the server will use the default value of {}
**sample_free_cols** | **{str: (str,)}** | Sample free columns. | [optional]  if omitted the server will use the default value of {}
**acquisition_free_cols** | **{str: (str,)}** | Acquisition free columns. | [optional]  if omitted the server will use the default value of {}
**process_free_cols** | **{str: (str,)}** | Process free columns. | [optional]  if omitted the server will use the default value of {}
**bodc_variables** | **{str: (str,)}** | BODC quantities from columns. Only the 3 keys listed in example are valid. | [optional]  if omitted the server will use the default value of {}
**init_classif_list** | **[int]** | Favorite taxa used in classification. | [optional]  if omitted the server will use the default value of []
**managers** | [**[MinUserModel]**](MinUserModel.md) | Managers of this project. | [optional]  if omitted the server will use the default value of []
**annotators** | [**[MinUserModel]**](MinUserModel.md) | Annotators of this project, if not manager. | [optional]  if omitted the server will use the default value of []
**viewers** | [**[MinUserModel]**](MinUserModel.md) | Viewers of this project, if not manager nor annotator. | [optional]  if omitted the server will use the default value of []
**instrument** | **str** | This project&#39;s instrument code. | [optional] 
**instrument_url** | **str** | This project&#39;s instrument BODC definition. | [optional] 
**contact** | **bool, date, datetime, dict, float, int, list, str, none_type** | The contact person is a manager who serves as the contact person for other users and EcoTaxa&#39;s managers. | [optional] 
**highest_right** | **str** | The highest right for requester on this project. One of &#39;Manage&#39;, &#39;Annotate&#39;, &#39;View&#39;. | [optional]  if omitted the server will use the default value of ""
**license** | **bool, date, datetime, dict, float, int, list, str, none_type** | Data licence. | [optional] 
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



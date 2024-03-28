# ProjectModel

Basic and computed information about the Project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_free_cols** | **Dict[str, str]** | Object free columns. | [optional] 
**sample_free_cols** | **Dict[str, str]** | Sample free columns. | [optional] 
**acquisition_free_cols** | **Dict[str, str]** | Acquisition free columns. | [optional] 
**process_free_cols** | **Dict[str, str]** | Process free columns. | [optional] 
**bodc_variables** | **Dict[str, str]** | BODC quantities from columns. Only the 3 keys listed in example are valid. | [optional] 
**init_classif_list** | **List[int]** | Favorite taxa used in classification. | [optional] [default to []]
**managers** | [**List[MinUserModel]**](MinUserModel.md) | Managers of this project. | [optional] [default to []]
**annotators** | [**List[MinUserModel]**](MinUserModel.md) | Annotators of this project, if not manager. | [optional] [default to []]
**viewers** | [**List[MinUserModel]**](MinUserModel.md) | Viewers of this project, if not manager nor annotator. | [optional] [default to []]
**instrument** | **str** | This project&#39;s instrument code. | [optional] 
**instrument_url** | **str** | This project&#39;s instrument BODC definition. | [optional] 
**contact** | [**MinUserModel**](MinUserModel.md) | The contact person is a manager who serves as the contact person for other users and EcoTaxa&#39;s managers. | [optional] 
**highest_right** | **str** | The highest right for requester on this project. One of &#39;Manage&#39;, &#39;Annotate&#39;, &#39;View&#39;. | [optional] [default to '']
**license** | [**LicenseEnum**](LicenseEnum.md) | Data licence. | [optional] 
**projid** | **int** | The project Id. | 
**title** | **str** | The project title. | 
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

## Example

```python
from ecotaxa_py_client.models.project_model import ProjectModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectModel from a JSON string
project_model_instance = ProjectModel.from_json(json)
# print the JSON string representation of the object
print(ProjectModel.to_json())

# convert the object into a dict
project_model_dict = project_model_instance.to_dict()
# create an instance of ProjectModel from a dict
project_model_form_dict = project_model.from_dict(project_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



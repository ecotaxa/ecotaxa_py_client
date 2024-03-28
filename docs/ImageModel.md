# ImageModel

Computed inside ObjectBO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imgid** | **int** | The id of the image. | [optional] 
**objid** | **int** | The id of the object related to the image. | 
**imgrank** | **int** | The rank of the image. | 
**width** | **int** | The width of the image. | 
**height** | **int** | The height of the image. | 
**orig_file_name** | **str** | The file name of the original image. | 
**thumb_width** | **int** | Generate thumbnail if image is too large. This generated thumbnail width. | [optional] 
**thumb_height** | **int** | Generate thumbnail if image is too large. The thumb height of the image. | [optional] 
**file_name** | **str** | The file name. | 
**thumb_file_name** | **str** | If image was too large at import time, the generated thumbnail file name. | [optional] 

## Example

```python
from ecotaxa_py_client.models.image_model import ImageModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImageModel from a JSON string
image_model_instance = ImageModel.from_json(json)
# print the JSON string representation of the object
print(ImageModel.to_json())

# convert the object into a dict
image_model_dict = image_model_instance.to_dict()
# create an instance of ImageModel from a dict
image_model_form_dict = image_model.from_dict(image_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



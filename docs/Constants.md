# Constants

Values which can be considered identical over the lifetime of the back-end.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_texts** | **Dict[str, str]** | The supported licenses and help text/links. | [optional] 
**app_manager** | **List[str]** | The application manager identity (name, mail), from config file. | [optional] [default to ["",""]]
**countries** | **List[str]** | List of known countries names. | [optional] [default to []]
**user_status** | **Dict[str, int]** | Application User status values | [optional] 
**password_regexp** | **str** | 8 char. minimum, at least one uppercase, one lowercase, one number and one special char in &#39;#?!@%^&amp;*-+&#39;  | [optional] [default to '^(?:(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#?%^&*-+])).{8,20}$']
**email_verification** | **bool** | Require verification before activation. | [optional] [default to True]
**account_validation** | **bool** | Require validation by a Users Administrator before activation. | [optional] [default to False]
**short_token_age** | **int** | Email confirmation, password reset token lifespan. | [optional] [default to 1]
**profile_token_age** | **int** | Profile modification token lifespan. | [optional] [default to 24]
**recaptchaid** | **bool** | use Google ReCaptcha | [optional] [default to False]

## Example

```python
from ecotaxa_py_client.models.constants import Constants

# TODO update the JSON string below
json = "{}"
# create an instance of Constants from a JSON string
constants_instance = Constants.from_json(json)
# print the JSON string representation of the object
print(Constants.to_json())

# convert the object into a dict
constants_dict = constants_instance.to_dict()
# create an instance of Constants from a dict
constants_form_dict = constants.from_dict(constants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Constants

Values which can be considered identical over the lifetime of the back-end. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_texts** | **{str: (str,)}** | The supported licenses and help text/links. | [optional]  if omitted the server will use the default value of {"CC0 1.0":"<a href=\"https://creativecommons.org/publicdomain/zero/1.0/\" rel=\"nofollow\"><strong>CC-0</strong></a>: all registered EcoTaxa users are free to download, redistribute, modify, and build upon the data, with no conditions. Other databases can index the data. The data falls into the worldwide public domain. This is the license preferred by <a href=\"https://obis.org/manual/policy/\" rel=\"nofollow\">OBIS</a> and <a href=\"https://www.gbif.org/terms\" rel=\"nofollow\">GBIF</a>.","CC BY 4.0":"<a href=\"https://creativecommons.org/licenses/by/4.0/\" rel=\"nofollow\"><strong>CC-BY</strong></a>: all registered EcoTaxa users are free to download, redistribute, modify, and build upon the data, as long as they cite the dataset and its authors. Other databases can index the data.","CC BY-NC 4.0":"<a href=\"https://creativecommons.org/licenses/by-nc/4.0/\" rel=\"nofollow\"><strong>CC-BY-NC</strong></a>: all registered EcoTaxa users are free to download, redistribute, modify, and build upon the data, as long as they cite the dataset and its authors, and do not use it for commercial purpose (\"primarily intended for or directed toward commercial advantage or monetary compensation\"). Other databases can index the data.","Copyright":"<strong>Copyright</strong>: only contributors to this project have rights on this data. This prevents its distribution in any kind of database.","":"Not chosen"}
**app_manager** | **[str]** | The application manager identity (name, mail), from config file. | [optional]  if omitted the server will use the default value of ["",""]
**countries** | **[str]** | List of known countries names. | [optional]  if omitted the server will use the default value of []
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ExportRsp

Export response. TODO: Should inherit the other way round.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **list[str]** | Showstopper problems found while building the archive. | [optional] [default to []]
**warnings** | **list[str]** | Problems found while building the archive, which do not prevent producing it. | [optional] [default to []]
**job_id** | **int** | The created job, 0 if there were problems. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



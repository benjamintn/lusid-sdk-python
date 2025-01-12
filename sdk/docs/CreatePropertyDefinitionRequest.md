# CreatePropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property will be created in. | 
**scope** | **str** | The scope that the property will be created in. | 
**code** | **str** | The code that the property will be created with. Together with the domain and  scope this uniquely identifies the property. | 
**value_required** | **bool** | Whether or not a value is always required for this property. Defaults to false if not specified. | [optional] 
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**life_time** | **str** | Controls how the property&#39;s values can change over time. Defaults to \&quot;Perpetual\&quot; if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



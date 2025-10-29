# Key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | API key unique identifier | [optional] 
**issuer_id** | **str** | In ID of the entity that issued the token. | [optional] 
**type** | **int** | API key type. Keys of different type are processed differently. | [optional] 
**subject** | **str** | User&#x27;s email or service identifier of API key subject. | [optional] 
**issued_at** | **datetime** | Time when the key is generated. | [optional] 
**expires_at** | **datetime** | Time when the Key expires. If this field is missing, that means that Key is valid indefinitely. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


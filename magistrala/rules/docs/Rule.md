# Rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique rule identifier | [optional] 
**name** | **str** | Rule name | 
**domain** | **str** | Domain ID this rule belongs to | 
**metadata** | **dict(str, str)** | Custom metadata | [optional] 
**input_channel** | **str** | Input channel for receiving messages | 
**input_topic** | **str** | Input topic for receiving messages | 
**logic** | [**RuleLogic**](RuleLogic.md) |  | 
**output_channel** | **str** | Output channel for processed messages | [optional] 
**output_topic** | **str** | Output topic for processed messages | [optional] 
**schedule** | [**RuleSchedule**](RuleSchedule.md) |  | [optional] 
**status** | **str** | Rule status | 
**created_at** | **datetime** | Creation timestamp | [optional] 
**created_by** | **str** | User who created the rule | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**updated_by** | **str** | User who last updated the rule | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


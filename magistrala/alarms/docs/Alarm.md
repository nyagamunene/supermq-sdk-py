# Alarm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique alarm identifier | [optional] 
**rule_id** | **str** | Rule ID that triggered this alarm | [optional] 
**domain_id** | **str** | Domain ID this alarm belongs to | [optional] 
**channel_id** | **str** | Channel ID where the alarm was triggered | [optional] 
**client_id** | **str** | Client ID that triggered the alarm | [optional] 
**subtopic** | **str** | Subtopic associated with the alarm | [optional] 
**status** | **str** | Alarm status | [optional] 
**measurement** | **str** | Measurement that triggered the alarm | [optional] 
**value** | **str** | Value that triggered the alarm | [optional] 
**unit** | **str** | Unit of measurement | [optional] 
**threshold** | **str** | Threshold value that was exceeded | [optional] 
**cause** | **str** | Cause or description of the alarm | [optional] 
**severity** | **int** | Severity level (0-100) | [optional] 
**assignee_id** | **str** | ID of the user assigned to this alarm | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**updated_by** | **str** | User who last updated the alarm | [optional] 
**assigned_at** | **datetime** | When the alarm was assigned | [optional] 
**assigned_by** | **str** | User who assigned the alarm | [optional] 
**acknowledged_at** | **datetime** | When the alarm was acknowledged | [optional] 
**acknowledged_by** | **str** | User who acknowledged the alarm | [optional] 
**resolved_at** | **datetime** | When the alarm was resolved | [optional] 
**resolved_by** | **str** | User who resolved the alarm | [optional] 
**metadata** | **dict(str, object)** | Custom metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


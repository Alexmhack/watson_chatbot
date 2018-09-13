import watson_developer_cloud

service = watson_developer_cloud.AssistantV1(
	username='',
	password='',
	version=''
)

workspace_id = ""

# Start conversation with an empty message
response = service.message(
	workspace_id=workspace_id,
	input={
		'text': ''
	}
)

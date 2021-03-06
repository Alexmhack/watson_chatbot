import os
import watson_developer_cloud

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

service = watson_developer_cloud.AssistantV1(
	username=os.getenv("WATSON_USERNAME"),
	password=os.getenv("WATSON_PASSWORD"),
	version=os.getenv("WATSON_VERSION")
)

workspace_id = os.getenv("WATSON_WORKSPACEID")

user_message = ''
context = {}

while True:
	response = service.message(
		workspace_id=workspace_id,
		input={
			'text': user_message
		},
		context=context
	).get_result()

	if response['intents']:
		print(f"Detected intent: {response['intents'][0]['intent']}")

	if response['output']['text']:
		print(response['output']['text'][0])

	try:
		if response['output']['generic'][1]['title']:
			print(response['output']['generic'][1]['title'])
			for opt in response['output']['generic'][1]['options']:
				print(opt['value']['input']['text'])
	except Exception as e:
		print(e)

	# update the stored context with the latest received from dialog
	context = response['context']

	user_message = input(">> ")

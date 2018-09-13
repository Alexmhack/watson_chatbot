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

# initialize with empty value to start conversation
user_message = ''

while True:

	response = service.message(
		workspace_id=workspace_id,
		input={
			'text': user_message
		}
	).get_result()

	if response['intents']:
		print(f"Detected intent: {response['intents'][0]['intent']}")

	if response['output']['text']:
		print(response['output']['text'][0])

	user_message = input(">> ")

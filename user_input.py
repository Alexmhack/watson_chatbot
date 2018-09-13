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

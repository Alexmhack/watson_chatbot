import os
import watson_developer_cloud

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# service = watson_developer_cloud.AssistantV1(
# 	username=os.getenv("USERNAME"),
# 	password=os.getenv("PASSWORD"),
# 	version=os.getenv("VERSION")
# )

# workspace_id = os.getenv("WORKSPACEID")

# # Start conversation with an empty message
# response = service.message(
# 	workspace_id=workspace_id,
# 	input={
# 		'text': ''
# 	}
# )

print(os.getenv("WATSON_VERSION"))
print(os.getenv("WATSON_USERNAME"))
print(os.getenv("WATSON_WORKSPACEID"))
print(os.getenv("WATSON_PASSWORD"))

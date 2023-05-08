from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = "xoxb-5226118994370-5223233262437-zBbT72nYYi46yJgLzaKodb9J"
client = WebClient(token=slack_token)
channel_id = "C057BPPD00Y"

try:
    result = client.chat_postMessage(
        channel=channel_id,
        text = "test: Hello world"
    )

except SlackApiError as e:
    print(f"Error posting message:{e}")
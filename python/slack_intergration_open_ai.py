# import openai_secret_manager
import openai
import json
import requests

# Use the openai_secret_manager to get your API key
# secrets = openai_secret_manager.get_secrets("openai")
# api_key = secrets["api_key"]

# Set the API key
openai.api_key = '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'

# Define the Slack bot's token
SLACK_BOT_TOKEN = "xoxb-3688285432405-4706348161459-QmdWTY6NQWkkIKNgXu9pLXr7"

# Define the Slack bot's endpoint
SLACK_BOT_ENDPOINT = f"https://slack.com/api/chat.postMessage?token={SLACK_BOT_TOKEN}&channel=%s&text=%s"

# Define the Slack event listener
SLACK_EVENT_ENDPOINT = "https://slack.com/api/events.listen"

def handle_question(event_data):
    # Extract the user's question from the event data
    question = event_data["text"]

    # Use the GPT-3 model to generate an answer to the question
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=3000
    )

    # Extract the answer from the response
    answer = response["choices"][0]["text"]

    # Send the answer back to the user via Slack
    channel = event_data["channel"]
    requests.get(SLACK_BOT_ENDPOINT % (channel, answer))

# Listen for events from Slack
while True:
    print("START Listen for events from Slack")
    response = requests.post(SLACK_EVENT_ENDPOINT, json={"token": SLACK_BOT_TOKEN})
    event_data = json.loads(response.text)
    if "event" in event_data:
        event_type = event_data["event"]["type"]
        if event_type == "app_mention":
            handle_question(event_data["event"])

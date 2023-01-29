# # import openai_secret_manager
# import openai
# import json
# import requests

# # Use the openai_secret_manager to get your API key
# secrets = openai_secret_manager.get_secrets("openai")
# api_key = secrets["api_key"]

# # Set the API key
openai.api_key = 'sk-your-token-here  '

# # Define the Slack bot's token
SLACK_BOT_TOKEN = "xoxb-your-token-here  "


# # Define the Slack bot's endpoint
# SLACK_BOT_ENDPOINT = f"https://slack.com/api/chat.postMessage?token={SLACK_BOT_TOKEN}&channel=%s&text=%s"

# # Define the Slack event listener
# SLACK_EVENT_ENDPOINT = "https://slack.com/api/events.listen"

# def handle_question(event_data):
#     # Extract the user's question from the event data
#     question = event_data["text"]

#     # Use the GPT-3 model to generate an answer to the question
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=question,
#         max_tokens=3000
#     )

#     # Extract the answer from the response
#     answer = response["choices"][0]["text"]

#     # Send the answer back to the user via Slack
#     channel = event_data["channel"]
#     requests.get(SLACK_BOT_ENDPOINT % (channel, answer))

# # Listen for events from Slack
# while True:
#     print("START Listen for events from Slack")
#     response = requests.post(SLACK_EVENT_ENDPOINT, json={"token": SLACK_BOT_TOKEN})
#     event_data = json.loads(response.text)
#     if "event" in event_data:
#         event_type = event_data["event"]["type"]
#         if event_type == "app_mention":
#             handle_question(event_data["event"])

##############################
#tasks/api/views.py
##############################
# import openai_secret_manager
import logging

import openai
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)


# Define the Slack bot's endpoint
SLACK_BOT_ENDPOINT = "https://slack.com/api/chat.postMessage"

# Define the Slack event listener
SLACK_EVENT_ENDPOINT = "https://slack.com/api/events.listen"


def handle_question(event_data):
    # Extract the user's question from the event data
    question = event_data["text"]
    logger.info('2' * 100)
    logger.info(question)

    # Use the GPT-3 model to generate an answer to the question
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=50
    )

    # Extract the answer from the response
    answer = response["choices"][0]["text"]

    # Send the answer back to the user via Slack
    channel = event_data["channel"]

    # res = requests.post(SLACK_BOT_ENDPOINT % (channel, answer))
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+SLACK_BOT_TOKEN},
        data={"channel": channel, "text": answer}
    )
    logger.info('3' * 100)
    logger.info(response.status_code)
    logger.info(response.text)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def slack_action_test(request):
    event_data = request.data
    logger.info('1' * 100)
    logger.info(event_data)

    if "event" in event_data:
        event_type = event_data["event"]["type"]
        if event_type == "app_mention":
            handle_question(event_data["event"])
        return JsonResponse({"message": "ok"}, status=status.HTTP_200_OK)

    elif "challenge" in event_data:
        return JsonResponse({"challenge": event_data["challenge"]})

    else:
        return JsonResponse({})

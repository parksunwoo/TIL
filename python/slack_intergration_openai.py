import logging

import openai
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)

# # Set the API key
openai.api_key = 'sk-your-token-here  '

# # Define the Slack bot's token
SLACK_BOT_TOKEN = "xoxb-your-token-here  "
SLACK_BOT_TOKEN_DALLE = "xoxb-your-token-here  "

# Define the Slack bot's endpoint
SLACK_BOT_ENDPOINT = "https://slack.com/api/chat.postMessage"

# Define the Slack event listener
SLACK_EVENT_ENDPOINT = "https://slack.com/api/events.listen"

AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]


def mod_openai_url_to_s3_public_expire_url(openai_expire_url, file_name):
    logger.info('START get_public_url()')
    # Download the image
    response = requests.get(openai_expire_url)
    image = BytesIO(response.content)
    s3 = boto3.client("s3")

    # Connect to S3 and upload the image
    timestamp = timezone.now().strftime("%Y/%m/%d/%H/%M/%S")
    dir_path = os.path.join(f"dalle/{timestamp}", f"{file_name}.png")
    full_path = os.path.join("media", dir_path)
    s3.upload_fileobj(image, AWS_STORAGE_BUCKET_NAME, full_path)

    # Generate the public URL
    # url = f"{settings.MEDIA_URL}{dir_path}"

    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': AWS_STORAGE_BUCKET_NAME,
            'Key': full_path
        },
        ExpiresIn=60 * 60 * 24 * 3,  # 3 days
        HttpMethod='GET'
    )
    return url


def handle_question_chatgpt(event_data):
    # Extract the user's question from the event data
    question = event_data["text"]
    logger.info('START handle_question_chatgpt()')
    logger.info(question)

    # Use the GPT-3 model to generate an answer to the question
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1000
    )

    # Extract the answer from the response
    answer = response["choices"][0]["text"]
    answer = re.sub(r"\w?\?", ".아 뭐더라...", answer)

    # Send the answer back to the user via Slack
    channel = event_data["channel"]

    # res = requests.post(SLACK_BOT_ENDPOINT % (channel, answer))
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+SLACK_BOT_TOKEN},
        data={"channel": channel, "text": answer}
    )
    logger.info(response.status_code)
    logger.info(response.text)
    logger.info('END handle_question_chatgpt()')


def handle_image_dalle(event_data):
    # Extract the user's question from the event data
    question = event_data["text"]
    logger.info('START handle_question_dalle()')
    logger.info(question)

    response = openai.Image.create(
        prompt=question,
        n=1,
        size="512x512"
    )
    _image_url1 = response['data'][0]['url']

    words = question.split()[:2]
    short_text = '-'.join(words)
    lowercase_text = short_text.lower()

    image_url1 = mod_openai_url_to_s3_public_expire_url(_image_url1, lowercase_text)
    logger.info(image_url1)

    # Send the answer back to the user via Slack
    channel = event_data["channel"]

    headers = {
        "Authorization": "Bearer "+SLACK_BOT_TOKEN_DALLE,
        "Content-type": "application/json; charset=utf-8",
    }
    payload = {
        "channel": channel,
        "attachments": [{
            "image_url": image_url1,
            "text": question,
        }
        ]
    }
    # logger.info(payload)

    response = requests.post("https://slack.com/api/chat.postMessage",
        headers=headers,
        data=json.dumps(payload)
    )
    logger.info(response.status_code)
    logger.info(response.text)
    logger.info('END handle_image_dalle()')


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def slack_action_chatgpt(request):
    logger.info('START slack_action_chatgpt()')
    event_data = request.data
    logger.info(event_data)
    logger.info(request.headers)

    if "event" in event_data:
        event_type = event_data["event"]["type"]
        x_slack_retry_num = request.headers.get('X-Slack-Retry-Num')
        logger.info(event_type)
        logger.info(x_slack_retry_num)

        if event_type == "app_mention" and not request.headers.get('X-Slack-Retry-Num'):
            handle_question_chatgpt(event_data["event"])
        return JsonResponse({"message": "ok"}, status=status.HTTP_200_OK)

    elif "challenge" in event_data:
        return JsonResponse({"challenge": event_data["challenge"]})

    else:
        return JsonResponse({})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def slack_action_dalle(request):
    logger.info('START slack_action_dalle()')
    event_data = request.data
    logger.info(event_data)
    logger.info(request.headers)

    if "event" in event_data:
        event_type = event_data["event"]["type"]
        x_slack_retry_num = request.headers.get('X-Slack-Retry-Num')
        logger.info(event_type)
        logger.info(x_slack_retry_num)

        if event_type == "app_mention" and not request.headers.get('X-Slack-Retry-Num'):
            handle_image_dalle(event_data["event"])
        return JsonResponse({"message": "ok"}, status=status.HTTP_200_OK)

    elif "challenge" in event_data:
        return JsonResponse({"challenge": event_data["challenge"]})

    else:
        return JsonResponse({})
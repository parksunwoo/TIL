import requests
import json
import webbrowser

import openai
from pytrends.request import TrendReq
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from googletrans import Translator

with open('conf.json') as f:
    config = json.load(f)

# Insert your OpenAI API key here
openai.api_key = config['openai.api_key']
CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']
REDIRECT_URI = config['REDIRECT_URI']
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
BLOGNAME = config['BLOGNAME']

# TODO
# https://trends.google.com/trends/yis/2022/US/
def get_top_10_trending_keywords(pn):
    pytrends = TrendReq()

    # Get the top 10 trending keywords
    trending_searches_df = pytrends.trending_searches(pn=pn)
    top_10_trends = trending_searches_df.head(30).values.tolist()

    return top_10_trends

def generate_summarize_text(keywords, pn):
    if pn == 'south_korea':
        prompt = "Please answer the topic following the conditions below Topic:" + "\n".join(keywords) +" Length: around 600 words. Format: markdown. Answer me in Korean Includes title Includes subtitles and detail descriptions. Voice and style guide: Write at a 5th grade level. Use clear and simple language, even when explaining complex topics. Bias toward short sentences. Avoid jargon and acronyms. Contend Goal: Blog."
    else:
        prompt="Summarize the contents of the main articles searched for by "+ "\n".join(keywords) +" and summarize them in an 300 words",

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1200,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def get_access_token():
    # 인증 요청 URL
    auth_url = f"https://www.tistory.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code"

    # 브라우저에서 자동으로 auth_code를 가져와서 사용,
    # Create an instance of the Firefox driver
    driver = webdriver.Chrome()

    # Navigate to the URL
    driver.get(auth_url)

    # Find the button you want to click
    button = driver.find_element(By.CLASS_NAME, "txt_login")

    # Click the button
    button.click()

    # Find the username and password fields
    username_field = driver.find_element(By.ID, "loginKey--1")
    password_field = driver.find_element(By.ID, "password--2")

    # Enter the username and password
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    button = driver.find_element(By.CLASS_NAME, "submit")
    button.click()

    sleep(1)

    button = driver.find_element(By.CLASS_NAME, "confirm")
    button.click()

    # # Extract the specific query value
    current_url = driver.current_url
    parts = urlparse(current_url)

    auth_code = parts.query.split('&')[0].split('=')[1]
    # # Close the browser window
    driver.quit()

    # Access Token 발급을 요청할 URL
    token_url = f"https://www.tistory.com/oauth/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&redirect_uri={REDIRECT_URI}&code={auth_code}&grant_type=authorization_code"

    # Access Token 발급 요청
    response = requests.get(token_url)

    # 발급된 Access Token
    access_token = response.text.split("=")[1]
    return access_token

def wirte_tistroy_post(access_token, keywords, content):
    # Replace these values with your own Tistory API credentials
    blog_name = BLOGNAME

    # The title and content of the article you want to post
    title = keywords + " 주요기사 요약"

    post_url = "https://www.tistory.com/apis/post/write?"
    params = {
        'access_token': access_token,
        'blogName': blog_name,
        'title': title,
        'content': content,
        'visibility': 0,
        'category': 0,
        'output': "json"
    }
    response = requests.post(post_url, params=params)

    print('5'*100)
    if response.status_code == 200:
        response_json = response.json()
        post_id = response_json["tistory"]["postId"]
        print("Successfully posted new article with ID:", post_id)
        return response.status_code
    else:
        print("Failed to post new article. Response code:", response.status_code)
        return response.status_code

print('0'*100)
access_token = get_access_token()
top_10_trends_us = get_top_10_trending_keywords(pn='united_states')
print(top_10_trends_us)

top_10_trends_ko = get_top_10_trending_keywords(pn='south_korea')
print(top_10_trends_ko)

translator = Translator()

for keyword_list in top_10_trends_us:
    print('1'*100)
    keyword = keyword_list[0]
    # keyword = keyword_list
    print(keyword)

    print('2'*100)
    generated_summarize_text = generate_summarize_text(keyword, pn='united_states')
    print(generated_summarize_text)
    
    print('3'*100)
    translations = translator.translate(generated_summarize_text, src='en', dest='ko')
    print(translations.text + '\n\n' + '---' + '\n\n원문\n' + generated_summarize_text)
    content = translations.text + '\n\n' + '---' + '\n\n원문\n' + generated_summarize_text
    print(len(content))

    print('4'*100)
    status_code = wirte_tistroy_post(access_token, keyword, content)

for keyword_list in top_10_trends_ko:
    print('1'*100)
    keyword = keyword_list[0]
    # keyword = keyword_list
    print(keyword)

    print('2'*100)
    generated_summarize_text = generate_summarize_text(keyword, pn='south_korea')
    print(generated_summarize_text)
    
    print('3'*100)
    translations = translator.translate(keyword, src='en', dest='ko')    
    keyword = translations.text
    content = generated_summarize_text
    print(len(content))

    print('4'*100)
    status_code = wirte_tistroy_post(access_token, keyword, content)
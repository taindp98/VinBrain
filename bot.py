# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import shlex
import os
from datetime import datetime
import json
import subprocess
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import requests
from audio_card import create_audio_card
from botbuilder.schema import AudioCard,AttachmentLayoutTypes
from botbuilder.core import MessageFactory
from glob import glob

from requests_toolbelt.multipart.encoder import MultipartEncoder

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        ## custom
        process_url = 'http://e2ebot.azurewebsites.net/api/convers-manager'
        # process_url = 'http://0.0.0.0:6969/api/convers-manager'
        input_text = str(turn_context.activity.text)
        input_id = str(turn_context.activity.conversation.id)
        ## frame input 

        # print('>'*50)
        # print(turn_context.activity.conversation.id)
        # print('>'*50)

        dict_input = {}
        dict_input['message'] = input_text
        dict_input['state_tracker_id'] = input_id

        response_object = requests.post(url=process_url, json=dict_input)
        response_object_json = response_object.json()
        

        # print('='*50)
        # print(input_id)
        # print(response_object_json)

        response_message = response_object_json['message']

        # print('>'*50)
        # print(response_message)

        if type(response_message) is list:
            list_mess_response = [item.replace('\n', r'').replace(r'"',r'') for item in response_message]
            first_response_message = list_mess_response[0]
        # else:

            # first_response_message = response_message.replace('\n', r'').replace(r'"',r'')
        
            cwd = os.getcwd()
            # print(cwd)
            audio_path = os.path.join(cwd,'audio')
            now = datetime.now()
            date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
            # date_time

            save_audio = os.path.join(audio_path,str(date_time)+'.wav')

            audio_cURL = """
            curl --location --request POST 'https://api-int.draid.ai/tts-service/v1/tts' \
            --header 'Content-Type: multipart/form-data' \
            --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJpc3MiOiJodHRwczovL3ZiaW50LmIyY2xvZ2luLmNvbS84NTA4ZDM0NC05MzJjLTQ0NGEtYjdkOC1mNDMyMTM0ZTZiMDEvdjIuMC8iLCJleHAiOjE2MTg1Njc2MTUsIm5iZiI6MTYxODU2NDAxNSwiYXVkIjoiZTA1ZTk2MWUtODc3OC00NzNlLWJiMzctNjA2OWU0Mjc3MzA3Iiwib2lkIjoiZDVjNDllOGEtODQ5ZS00ZTg3LWFlNWQtZWViZWYwYmUxNGIxIiwic3ViIjoiZDVjNDllOGEtODQ5ZS00ZTg3LWFlNWQtZWViZWYwYmUxNGIxIiwibmFtZSI6Ik5ndXnhu4VuIETGsMahbmcgUGjDumMgVMOgaSIsImdpdmVuX25hbWUiOiJQaMO6YyBUw6BpIiwiZW1haWxzIjpbInYudGFpbmdAdmluYnJhaW4ubmV0Il0sInRmcCI6IkIyQ18xX3ZibWRhLXNpZ25pbi12Mi1pbnQiLCJub25jZSI6ImY3YmVmMGE0LTU0NDgtNGFhYS04NzJkLWRhNWRkODFjNjM3YSIsInNjcCI6InZibWRhLnJlYWQiLCJhenAiOiJlMDVlOTYxZS04Nzc4LTQ3M2UtYmIzNy02MDY5ZTQyNzczMDciLCJ2ZXIiOiIxLjAiLCJpYXQiOjE2MTg1NjQwMTV9.hmjZBm3Sq8IQLL6Mi1SL_UI3CLc8YbL4jZ0IZBXEc3FoJvHrQ6qWZwuZWRxfo2nKUgnacTs2Ziqa5ti-zNCd9Yc-y4OOOjBJJGZ2ieAo8PVZbwES0EcWCtLhjluq9mX_MFVwcTkfzM6gYtaH6g075VM4-k90AiNEi83Gsc1LHXOIiGErb4cKY9WQUsSjsm1JDObxMiJGtaIDIbiMq1y_hssUpSGvYS6GxK1kX1ncXqtznd_jq89YY6XBevE9Kv481EGEHF9aWSF_uAZYxPRMjJ-D9rtUDsXwK3tcCdHMgzvipxhhJiSc-0sEBHm15rVqPYRNZVf-qrSgg1msbZQemQ'\
            --form 'text=%s' \
            --form 'extension="WAV"' \
            --form 'gender="MALE"' \
            --form 'area="SOUTH"' \
            --form 'language="VI"' \
            --form 'pace="1.0"'\
            --output %s
            """%(first_response_message,save_audio)
            # print(os.system(audio_cURL))
            args = shlex.split(audio_cURL)
            process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            # print("save_audio",save_audio)
            # print("stdout",stdout)
            # print("stderr",stderr)
            # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
            reply = MessageFactory.list([])
            reply.attachment_layout = AttachmentLayoutTypes.carousel

            # audio_url_custom = 'https://1drv.ms/u/s!AvgPPwEWTreweCuzIqgIJ5yZx2Q?e=Vgz9Uj'
            list_audio = glob(os.path.join(audio_path,'*.wav'))
            audio_url_custom = sorted(list_audio,reverse=True)[0]

            print('audio_url_custom',audio_url_custom)
            reply.attachments.append(create_audio_card(audio_url_custom))

            # await turn_context.send_activity(first_response_message)
            await turn_context.send_activity(reply)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

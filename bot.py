# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import requests
import json
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import requests
from audio_card import create_audio_card
from botbuilder.schema import AudioCard,AttachmentLayoutTypes
from botbuilder.core import MessageFactory

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
            save_audio = os.path.join(audio_path,first_response_message[:5]+'.wav')

            ## parse cURL
            url = 'https://api-int.draid.ai/tts-service/v1/tts'
            headers = {
                'Content-Type': 'multipart/form-data',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJpc3MiOiJodHRwczovL3ZiaW50LmIyY2xvZ2luLmNvbS84NTA4ZDM0NC05MzJjLTQ0NGEtYjdkOC1mNDMyMTM0ZTZiMDEvdjIuMC8iLCJleHAiOjE2MTg0Nzg3MDEsIm5iZiI6MTYxODQ3NTEwMSwiYXVkIjoiZTA1ZTk2MWUtODc3OC00NzNlLWJiMzctNjA2OWU0Mjc3MzA3Iiwib2lkIjoiZDVjNDllOGEtODQ5ZS00ZTg3LWFlNWQtZWViZWYwYmUxNGIxIiwic3ViIjoiZDVjNDllOGEtODQ5ZS00ZTg3LWFlNWQtZWViZWYwYmUxNGIxIiwibmFtZSI6Ik5ndXnhu4VuIETGsMahbmcgUGjDumMgVMOgaSIsImdpdmVuX25hbWUiOiJQaMO6YyBUw6BpIiwiZW1haWxzIjpbInYudGFpbmdAdmluYnJhaW4ubmV0Il0sInRmcCI6IkIyQ18xX3ZibWRhLXNpZ25pbi12Mi1pbnQiLCJub25jZSI6IjBkZDM4ZDEwLWI1YjAtNDE5Ny1hODJmLTVkOGQyY2FhYzZkYSIsInNjcCI6InZibWRhLnJlYWQiLCJhenAiOiJlMDVlOTYxZS04Nzc4LTQ3M2UtYmIzNy02MDY5ZTQyNzczMDciLCJ2ZXIiOiIxLjAiLCJpYXQiOjE2MTg0NzUxMDF9.DaNkCtNwpBymdnKnX6lI1i_guU-KqIMEHCyEVaaj4Qgds771PArsOwDmgaV37g8TVb1BVRw1e2Z8d5OU2yAFiKZugqtWTgxXgHa6ODpVieACDacTJTG5YyPkhip8BCcUIyYQddEGpqH8wp8gZzKTGolKCeZ2x-qi6a5bI8TzJZgDnx1Y1EwXduGo3QF7-ebJrcEVAJOhWJHizSflmuqygdNJZI7vx_ySiWAGEpWiHodtu8_Eg-PVhhs4NpN9a1xwQJPjMPJ4x-o5gwSMP-HiLs_BKdiAqzmd7YKJAuB2XddrS19D8QJETeDeMlCjOCWjmYnwHaGrtN_UyKzJcPUo1A'
            }
            data = {
                "text": first_response_message,
                "extension": "WAV",
                "gender":"MALE",
                "area":"SOUTH",
                "language":"VI",
                "pace":"1.0",
                "output": save_audio
            }

            r = requests.post(url, data=json.dumps(data), headers=headers)
            print(r)
            # audio_cURL = """
            # curl --location --request POST 'https://api-int.draid.ai/tts-service/v1/tts' \
            # --header 'Content-Type: multipart/form-data' \
            # --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJpc3MiOiJodHRwczovL3ZiaW50LmIyY2xvZ2luLmNvbS84NTA4ZDM0NC05MzJjLTQ0NGEtYjdkOC1mNDMyMTM0ZTZiMDEvdjIuMC8iLCJleHAiOjE2MTg0Nzg3MDEsIm5iZiI6MTYxODQ3NTEwMSwiYXVkIjoiZTA1ZTk2MWUtODc3OC00NzNlLWJiMzctNjA2OWU0Mjc3MzA3Iiwib2lkIjoiZDVjNDllOGEtODQ5ZS00ZTg3LWFlNWQtZWViZWYwYmUxNGIxIiwic3ViIjoiZDVjNDllOGEtODQ5ZS00ZTg3LWFlNWQtZWViZWYwYmUxNGIxIiwibmFtZSI6Ik5ndXnhu4VuIETGsMahbmcgUGjDumMgVMOgaSIsImdpdmVuX25hbWUiOiJQaMO6YyBUw6BpIiwiZW1haWxzIjpbInYudGFpbmdAdmluYnJhaW4ubmV0Il0sInRmcCI6IkIyQ18xX3ZibWRhLXNpZ25pbi12Mi1pbnQiLCJub25jZSI6IjBkZDM4ZDEwLWI1YjAtNDE5Ny1hODJmLTVkOGQyY2FhYzZkYSIsInNjcCI6InZibWRhLnJlYWQiLCJhenAiOiJlMDVlOTYxZS04Nzc4LTQ3M2UtYmIzNy02MDY5ZTQyNzczMDciLCJ2ZXIiOiIxLjAiLCJpYXQiOjE2MTg0NzUxMDF9.DaNkCtNwpBymdnKnX6lI1i_guU-KqIMEHCyEVaaj4Qgds771PArsOwDmgaV37g8TVb1BVRw1e2Z8d5OU2yAFiKZugqtWTgxXgHa6ODpVieACDacTJTG5YyPkhip8BCcUIyYQddEGpqH8wp8gZzKTGolKCeZ2x-qi6a5bI8TzJZgDnx1Y1EwXduGo3QF7-ebJrcEVAJOhWJHizSflmuqygdNJZI7vx_ySiWAGEpWiHodtu8_Eg-PVhhs4NpN9a1xwQJPjMPJ4x-o5gwSMP-HiLs_BKdiAqzmd7YKJAuB2XddrS19D8QJETeDeMlCjOCWjmYnwHaGrtN_UyKzJcPUo1A' \
            # --form 'text=%s' \
            # --form 'extension="WAV"' \
            # --form 'gender="MALE"' \
            # --form 'area="SOUTH"' \
            # --form 'language="VI"' \
            # --form 'pace="1.0"'\
            # --output %s
            # """%(first_response_message,save_audio)

            # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
            reply = MessageFactory.list([])
            reply.attachment_layout = AttachmentLayoutTypes.carousel

            # audio_url_custom = 'https://1drv.ms/u/s!AvgPPwEWTreweCuzIqgIJ5yZx2Q?e=Vgz9Uj'
            audio_url_custom = './audio/test.wav'

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

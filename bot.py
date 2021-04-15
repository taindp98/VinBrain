# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import requests

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        ## custom
        process_url = 'http://e2ebot.azurewebsites.net/api/convers-manager'
        input_text = str(turn_context.activity.text)
        input_id = str(turn_context.activity.id)
        ## frame input 
        dict_input = {}
        dict_input['message'] = input_text
        dict_input['user_id'] = input_id

        response_object = requests.post(url=process_url, json=dict_input)
        response_object_json = response_object.json()
        

        # print('='*50)
        # print(response_object_json)

        response_message = response_object_json['message']
        if type(response_message) is list:
            list_mess_response = [item.replace('\n', r'').replace(r'"',r'') for item in response_message]
            first_response_message = list_mess_response[0]
        else:
            first_response_message = response_message.replace('\n', r'').replace(r'"',r'')
        
        
        audio_cURL = """
        curl --location --request POST 'https://api-int.draid.ai/tts-service/v1/tts' \
            --header 'Content-Type: multipart/form-data' \
            --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJpc3MiOiJodHRwczovL3ZiaW50LmIyY2xvZ2luLmNvbS84NTA4ZDM0NC05MzJjLTQ0NGEtYjdkOC1mNDMyMTM0ZTZiMDEvdjIuMC8iLCJleHAiOjE2MTg0NjIzOTEsIm5iZiI6MTYxODQ1ODc5MSwiYXVkIjoiZTA1ZTk2MWUtODc3OC00NzNlLWJiMzctNjA2OWU0Mjc3MzA3Iiwib2lkIjoiY2VlZDRhMTUtNTYyNS00OTE4LTkyNzEtNzRjOTlkOTA5ZmVjIiwic3ViIjoiY2VlZDRhMTUtNTYyNS00OTE4LTkyNzEtNzRjOTlkOTA5ZmVjIiwibmFtZSI6Ikjhu5MgSG_DoG5nIE5hbSIsImdpdmVuX25hbWUiOiJOYW0iLCJlbWFpbHMiOlsidi5uYW1ob0B2aW5icmFpbi5uZXQiXSwidGZwIjoiQjJDXzFfdmJtZGEtc2lnbmluLXYyLWludCIsIm5vbmNlIjoiNDQ2MmZmNzItZWIwMC00YjAwLWJlZjItYWZlYjEzN2FkYjliIiwic2NwIjoidmJtZGEucmVhZCIsImF6cCI6ImUwNWU5NjFlLTg3NzgtNDczZS1iYjM3LTYwNjllNDI3NzMwNyIsInZlciI6IjEuMCIsImlhdCI6MTYxODQ1ODc5MX0.oF1lTp4hnMB_nvclnFcwjOC0M7gjEHqaE6OGGX3f1cI89WQZOPVo2A-Ynz48flqbIshX3r0kWA1wq7jvHmheWNDjinQXMYoQ_sQRQi8MSO6-t6BmOmwAckfFme61gKaES-pMOqCXp4PymZhMNnziP03ktKyC9pKwCM0JqvuyEb_LkabSUTdDp35BPBcLcMBgPsCT1Qtsd0EKz6-OzOo29FU5bPzMP1BmQv2zZIFvvW1HL2KzooEVnigvtyJgKHhIlXr-W85UUZcIEaev47KWkHvqOk9xlJYLtNYuLwV4YJDx2W5MhmKv3u1j976njREOnMKba6-ZD4UNp7g36CKOzw' \
            --form 'text=%s' \
            --form 'extension="WAV"' \
            --form 'gender="MALE"' \
            --form 'area="SOUTH"' \
            --form 'language="VI"' \
            --form 'pace="1.0"'
        """%first_response_message

        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        await turn_context.send_activity(first_response_message)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

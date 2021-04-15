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

        print('='*50)
        print(response_object_json)

        response_message = response_object_json['message']
        if type(response_message) is list:
            list_mess_response = [item.replace('\n', r'').replace(r'"',r'') for item in response_message]
            first_response_message = list_mess_response[0]
        else:
            first_response_message = response_message.replace('\n', r'').replace(r'"',r'')
        

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

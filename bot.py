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
        input_data = str(turn_context.activity.text)
        response_object = requests.post(url=process_url, json=input_data)
        response_object_json = response_object.json()

        response_message = response_object_json['message']
        list_mess_response = [item.replace('\n', r'').replace(r'"',r'') for item in response_message]

        first_response_message = list_mess_response[0]

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

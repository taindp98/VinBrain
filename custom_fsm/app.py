import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


# API_TOKEN = 'Your Telegram API Token'
# WEBHOOK_URL = 'Your Webhook URL'

# app = Flask(__name__)
# bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2'
            ],
            'dest': 'user'
            # 'conditions': 'on_enter_state1'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

text = ['go to state1']
for t in text:
    machine.advance(t)
    # print(machine)
    # machine.go_back(t)

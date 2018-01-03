import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

import random

API_TOKEN = '490896274:AAGxeUtQf1Td-rqaeQKs-qLo1z0y3OICuwo'
WEBHOOK_URL = 'https://39c61131.ngrok.io/show-fsm'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'eat',
        'search',
        'fastfood',
		'fried',
		'nonfried',
		'food',
		'expensive',
		'cheap',
        'google'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'eat',
            'conditions': 'is_going_to_eat'
        },
        {
            'trigger': 'advance',
            'source': 'eat',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'search',
            'dest': 'google',
            'conditions': 'is_going_to_google'
        },
        {
            'trigger': 'advance',
            'source': 'eat',
            'dest': 'fastfood',
            'conditions': 'is_going_to_fastfood'
        },
		{
			'trigger': 'advance',
            'source': 'fastfood',
            'dest': 'fried',
            'conditions': 'is_going_to_fried'
		},
		{
			'trigger': 'advance',
            'source': 'fastfood',
            'dest': 'nonfried',
            'conditions': 'is_going_to_nonfried'
		},
		{
			'trigger': 'advance',
            'source': 'eat',
            'dest': 'food',
            'conditions': 'is_going_to_food'
		},
		{
			'trigger': 'advance',
            'source': 'food',
            'dest': 'expensive',
            'conditions': 'is_going_to_expensive'
		},
		{
			'trigger': 'advance',
            'source': 'food',
            'dest': 'cheap',
            'conditions': 'is_going_to_cheap'
		},
		{
            'trigger': 'go_back',
            'source': [
                'google',
				'fried',
				'nonfried',
				'expensive',
				'cheap'
				#'fastfood',
				#'food'
				],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()

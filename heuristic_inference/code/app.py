import pymongo
from flask_pymongo import PyMongo
from flask import Flask, request, jsonify
from flask_cors import CORS

import os
from process_action import update_agent_action
from utils import gen_user_action
from state_tracker import StateTracker

from pattern_response import AGENT_RESPONSE

app = Flask(__name__)
CORS(app)

# os.environ["MONGOLAB_URI"] = 'mongodb://localhost:27017'
os.environ["MONGOLAB_URI"] = 'mongodb://taindp:chatbot2020@thesis-shard-00-00.bdisf.mongodb.net:27017,thesis-shard-00-01.bdisf.mongodb.net:27017,thesis-shard-00-02.bdisf.mongodb.net:27017/hcmut?ssl=true&replicaSet=atlas-12fynb-shard-0&authSource=admin&retryWrites=true&w=majority'

client = pymongo.MongoClient(os.environ.get('MONGOLAB_URI'))
# database = client.vinbrain
database = client.hcmut
col_db = database.disease

tracker = StateTracker(col_db)

@app.route('/api/disease', methods=['POST'])
def post_api_disease():
    input_data = request.json

    if "message" not in input_data.keys():
        return msg(400, "Message cannot be None")
    else:
        message = input_data["message"]

    ## gen user's action
    tracker.reset_new_round()
    # print(tracker.tracker_user_action)
    # print('='*50)
    user_action = tracker.gen_user_action(message)
    print('='*50)
    print("USER'S ACTION: {}".format(user_action))
    print('='*50)
    # print("user_action",user_action)
    if user_action['intent'] == 'request':
        tracker.reset_tracker_user_action()

    # print("tracker",tracker.tracker_user_action)
    # print(user_action)
    # print('='*50)
    ## update user's action
    tracker.update_user_action(user_action)

    ## update agent's action
    agent_action,amount_record_match = tracker.update_agent_action()

    ## natural language generation
    if agent_action['intent'] == 'inform':
        current_informs = agent_action['inform_slots']['Symptom'][0]
        agent_message = AGENT_RESPONSE[agent_action['intent']].replace('*SUGGEST_SLOT*',current_informs)

    elif agent_action['intent'] == 'match_found':
        current_informs = agent_action['inform_slots']['Disease'][0]
        agent_message = AGENT_RESPONSE[agent_action['intent']].replace('*MATCH_FOUND_SLOT*',current_informs)
    else:
        agent_message = AGENT_RESPONSE[agent_action['intent']]

    if agent_action['intent'] == 'match_found' or agent_action['intent'] == 'done':
        tracker.reset_tracker_user_action()

    res_dict = {}
    res_dict["code"] = 200

    res_dict['agent_action'] = agent_action

    res_dict["message"] = agent_message
    
    return jsonify(res_dict)

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0',port=6969,debug=True)
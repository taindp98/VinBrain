import pymongo
from flask_pymongo import PyMongo
from flask import Flask, request, jsonify
from flask_cors import CORS

import os
from process_action import update_agent_action
# from mongoengine import connect

app = Flask(__name__)
CORS(app)

os.environ["MONGOLAB_URI"] = 'mongodb://localhost:27017'
client = pymongo.MongoClient(os.environ.get('MONGOLAB_URI'))
database = client.vinbrain
col_db = database.disease

@app.route('/api/convers-manager', methods=['POST'])
def post_api_cse_assistant():
    input_data = request.json

    if "message" not in input_data.keys():
        return msg(400, "Message cannot be None")
    else:
        message = input_data["message"]
    # print("-------------------------message")
    # print(message)
    # if "state_tracker_id" not in input_data.keys():
    #     state_tracker_id = get_new_id()
    # else:
    #     state_tracker_id = input_data["state_tracker_id"]
    # # print('StateTracker_Container',StateTracker_Container)
    # K.clear_session()
    # current_informs = 'null'
    # agent_message , agent_action = process_conversation_POST(state_tracker_id, message)

    

    agent_action,amount_record_match = update_agent_action(user_action,col_db)


    if agent_action['intent'] in ["match_found","inform"]:
        current_informs = StateTracker_Container[state_tracker_id][0].current_informs

    res_dict = {}
    res_dict["code"] = 200
    res_dict["message"] = agent_message
    res_dict["state_tracker_id"] = state_tracker_id

    res_dict['agent_action'] = agent_action
    res_dict['current_informs'] = current_informs

    print('======================')
    print('current_informs',current_informs)
    # print(res_dict)
    # return jsonify({"code": 200, "message": agent_message,"state_tracker_id":state_tracker_id,"agent_action":agent_action,"current_informs":current_informs})
    return jsonify(res_dict)

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0',port=6969,debug=True)



import re
import pymongo
from utils import convert_constraint,check_available,check_pattern,freq_sympt_appear

def update_agent_action(user_action,col,done=False):

    global agent_action
    """
    param:
        user's action

    return:
        agent's action
        dictionary to investigate db
    """
    ## convert constraint from user action
    constraints = user_action['inform_slots']
    query_string = convert_constraint(constraints)

    ## query from db
    query_result = col.find(query_string)
    list_record_query = []
    for item in query_result:
        list_record_query.append(item)

    ## investigate

    # dict_invest = {}
    # dict_invest[str(constraints)] = {}
    # dict_invest[str(constraints)]['amount_record_match'] = len(list_record_query)

    amount_record_match = len(list_record_query)

    if amount_record_match == 1:
        agent_action = {}
        agent_action['intent'] = 'match_found'
                
        _PLACE_HOLDER = list_record_query[0]['Disease']
        
        agent_action['inform_slots'] = {'Disease' : [_PLACE_HOLDER]}
        agent_action['request_slots'] = {}

        return agent_action,amount_record_match
    
    # elif amount_record_match == 
    # print('amount record match: {}'.format(len(list_record_query)))
    ## logic suggest

    list_statistic_sympt = []
    for record in list_record_query:
        for k,v in record.items():
            if k == 'Symptom':
                list_statistic_sympt += v
                
    ## logic correct sympt's name
    last_sympt_user_inform = user_action['inform_slots']['Symptom'][-1]

    list_sympt_user_inform = user_action['inform_slots']['Symptom']

    list_unique_sympt_query = list(set(list_statistic_sympt))

    list_correct_sympt_name = check_pattern(list_unique_sympt_query,last_sympt_user_inform)

    dict_sympt_correct_name_appear = freq_sympt_appear(list_statistic_sympt,list_correct_sympt_name)
    
    dict_all_sympt_appear = freq_sympt_appear(list_statistic_sympt,list_unique_sympt_query)
    
    list_sympt_suggest = []

    if last_sympt_user_inform not in list(dict_sympt_correct_name_appear.keys()):
        list_sympt_suggest = list(dict_sympt_correct_name_appear.keys())
    else:
        # print('='*50)
        # print('vote appear',dict_all_sympt_appear)
        list_sympt_query = list(dict_all_sympt_appear.keys())
        for item in list_sympt_query:
            if item not in list_sympt_user_inform and dict_all_sympt_appear[item] < amount_record_match:
                list_sympt_suggest.append(item)


    # list_sympt_user_inform = list(user_action['inform_slots'].values())[0]
    # print("list_sympt_user_inform",list_sympt_user_inform)
    # print("list_sympt_query",list_sympt_query)
    # list_sympt_suggest.append(check_available(list_sympt_query,list_sympt_user_inform))

    ## gen agent action
    """

        build chatbot script
        
        agent's intent available: inform, request, match_found, done
            + inform: when available list_sympt_suggest
            + request: when not available list_sympt_suggest

            temp not use

            + match_found: when find only 1 record
            + done: when not found record satisfy user's constraint  

    """
    agent_action = {}

    if list_sympt_suggest:
        agent_action['intent'] = 'inform'
                
        _PLACE_HOLDER = list_sympt_suggest.pop(0)
        
        agent_action['inform_slots'] = {'Symptom' : [_PLACE_HOLDER]}
        agent_action['request_slots'] = {}

    else:
        agent_action['intent'] = 'request'

        _UNK = 'unknown'

        agent_action['inform_slots'] = {}
        agent_action['request_slots'] = {'Symptom' : [_UNK]}

    ## process match_found
    # if match_found:
    #     agent_action['intent'] = 'match_found'
                
    #     _PLACE_HOLDER = list(list_record_query[0].keys())[1]
        
    #     agent_action['inform_slots'] = {'Disease' : [_PLACE_HOLDER]}
    #     agent_action['request_slots'] = {}
    
    if done:
        agent_action['intent'] = 'done'
                
        _PLACE_HOLDER = 'none_record_match'
        
        agent_action['inform_slots'] = {'Disease' : [_PLACE_HOLDER]}
        agent_action['request_slots'] = {}

    return agent_action,amount_record_match

# def update_user_action(user_action,agent_action):
def update_user_action(user_action,agent_action):

    """

    ONLY USE SIMULATE

    param:
        user's action new
        agent's action

        # HAPPY CASE
        <--assumpt that user willing response correct all action from agent-->

    return:
        user's action
    """

    ## check new sympt or confirm correct symptom's name 

    if agent_action['inform_slots']:
        current_slot = list(agent_action['inform_slots'].values())[0][0]
    
    if agent_action['request_slots']:
        current_slot = list(agent_action['request_slots'].values())[0][0]
    
    list_sympt_user_action = user_action['inform_slots']['Symptom']

    # list_check_pattern = check_pattern(list_sympt_user_action,current_slot)
    flag_pattern = False
    for item in list_sympt_user_action:
        regexp = re.compile(item)
        if regexp.search(current_slot):
            flag_pattern = True
            break


    # print('current_slot',current_slot)
    # print('list_sympt_user_action',list_sympt_user_action)

    if flag_pattern:
        user_action['inform_slots']['Symptom'] = [current_slot]
    else:
        user_action['inform_slots']['Symptom'].append(current_slot)

    return user_action
    



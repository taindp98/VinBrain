import re
import pymongo
from utils import convert_constraint,check_available,check_pattern,freq_sympt_appear

class StateTracker:

    def __init__(self,collection_db):

        self.tracker_user_action = {}

        self.tracker_user_action['inform_slots'] = {}
        self.tracker_user_action['inform_slots']['Symptom'] = []

        self.tracker_user_action['request_slots'] = {}
        self.tracker_user_action['request_slots']['Disease'] = None

        self.agent_action = {}
        self.amount_record_match = None
        self.db = collection_db
        self.current_informs = {}

        self.round_num = 0

        self.current_request_slots = []
    def update_agent_action(self,done=False):

        # global agent_action
        """
        param:
            user's action

        return:
            agent's action
            dictionary to investigate db
        """
        ## convert constraint from user action
        constraints = self.tracker_user_action['inform_slots']
        query_string = convert_constraint(constraints)

        ## query from db
        query_result = self.db.find(query_string)
        list_record_query = []
        for item in query_result:
            list_record_query.append(item)

        ## investigate

        # dict_invest = {}
        # dict_invest[str(constraints)] = {}
        # dict_invest[str(constraints)]['amount_record_match'] = len(list_record_query)

        self.amount_record_match = len(list_record_query)

        if self.amount_record_match == 1:
            # agent_action = {}
            self.agent_action['intent'] = 'match_found'
                    
            _PLACE_HOLDER = list_record_query[0]['Disease']
            
            self.agent_action['inform_slots'] = {'Disease' : [_PLACE_HOLDER]}
            self.agent_action['request_slots'] = {}

            return self.agent_action,self.amount_record_match


        list_statistic_sympt = []
        for record in list_record_query:
            for k,v in record.items():
                if k == 'Symptom':
                    list_statistic_sympt += v
                    
        ## logic correct sympt's name
        list_sympt_user_inform = self.tracker_user_action['inform_slots']['Symptom']

        last_sympt_user_inform = list_sympt_user_inform[-1]

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
                if item not in list_sympt_user_inform and dict_all_sympt_appear[item] < self.amount_record_match:
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
        # agent_action = {}

        if list_sympt_suggest:
            self.agent_action['intent'] = 'inform'
                    
            _PLACE_HOLDER = list_sympt_suggest.pop(0)
            
            self.agent_action['inform_slots'] = {'Symptom' : [_PLACE_HOLDER]}
            self.agent_action['request_slots'] = {}

        else:
            self.agent_action['intent'] = 'request'

            _UNK = 'unknown'

            self.agent_action['inform_slots'] = {}
            self.agent_action['request_slots'] = {'Symptom' : [_UNK]}

        ## process match_found
        # if match_found:
        #     agent_action['intent'] = 'match_found'
                    
        #     _PLACE_HOLDER = list(list_record_query[0].keys())[1]
            
        #     agent_action['inform_slots'] = {'Disease' : [_PLACE_HOLDER]}
        #     agent_action['request_slots'] = {}
        
        if done:
            self.agent_action['intent'] = 'done'
                    
            _PLACE_HOLDER = 'none_record_match'
            
            self.agent_action['inform_slots'] = {'Disease' : [_PLACE_HOLDER]}
            self.agent_action['request_slots'] = {}

        return self.agent_action, self.amount_record_match

    # def update_user_action(user_action,agent_action):
    def update_user_action(self,user_action):

        """

        param:
            agent's action new

        return:
        """
        # self.tracker_user_action['intent'] = user_action['intent']

        for key, values in user_action['inform_slots'].items():
            # print('check',self.tracker_user_action['inform_slots']['Symptom'])
            for v in values:
                if v not in self.tracker_user_action['inform_slots']['Symptom']:
                    self.tracker_user_action['inform_slots']['Symptom'].append(v)

        for key, value in user_action['request_slots'].items():
            if not self.tracker_user_action['request_slots']['Disease']:
                self.tracker_user_action['request_slots']['Disease'] = value
        
        # self.round_num += 1

    



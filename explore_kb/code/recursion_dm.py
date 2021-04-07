from process_action import *
import random

# global agent_action

# def dialogue_management(user_action,col_db,count,done):
def dialogue_management(target_symptom,col_db,count,done):
    """
    simulate user_action

    param:
        user's action
        col_db: collection of NoSQL database
    return:
        recursion to find the best way to successfull dialogue
    """
    global user_action
    global current_inform_slots
    # global idx_init_sympt
    if count == 0:

        user_action = {}
        # user_action['intent'] = 'request'
        # user_action['request_slots'] = {'Disease':'unk'}

        user_action['inform_slots'] = {}
        
        current_inform_slots = []
        # pop_inform_slot = target_symptom.pop(idx_init_sympt)
        # current_inform_slots.append(pop_inform_slot)
        # user_action['inform_slots']['Symptom'] = current_inform_slots
    if len(target_symptom) > 1:
        idx_init_sympt = random.randint(0,len(target_symptom)-1)

    user_action['intent'] = 'request'
    user_action['request_slots'] = {'Disease':'unk'}

    # user_action['inform_slots'] = {}
    
    
    pop_inform_slot = target_symptom.pop(idx_init_sympt)
    current_inform_slots.append(pop_inform_slot)
    user_action['inform_slots']['Symptom'] = current_inform_slots

    count += 1
    print('Current slot: {}'.format(count))
    print('User: {}'.format(user_action))
    agent_action,amount_record_match = update_agent_action(user_action,col_db,done)
    print('Agent: {}'.format(agent_action))
    print('Record found: {}'.format(amount_record_match))
    user_action = update_user_action(user_action,agent_action)
    print('='*50)

    # done = False

    if amount_record_match > 1:
        # dialogue_management(user_action,col_db,count,done)
        dialogue_management(target_symptom,col_db,count,done)

    # elif amount_record_match == 0:
    elif amount_record_match == 0:
        done = True
        # dialogue_management(user_action,col_db,count,done)
        dialogue_management(target_symptom,col_db,count,done)
        return True
    else:
        return True


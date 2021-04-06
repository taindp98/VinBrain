from process_action import *

# global agent_action

def dialogue_management(user_action,col_db,count,done):
    """
    param:
        user's action
        col_db: collection of NoSQL database
    return:
        recursion to find the best way to successfull dialogue
    """
    # global user_action
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
        dialogue_management(user_action,col_db,count,done)

    # elif amount_record_match == 0:
    elif amount_record_match == 0:
        done = True
        dialogue_management(user_action,col_db,count,done)
        return True
    else:
        return True


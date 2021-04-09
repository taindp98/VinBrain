## error model controller
import random

def gen_error_user_action(user_action,rand_noise=False):
    """
    param:
        user's action willing response correct slot for agent
    return:
        user's action response lack up char/string
    """

    last_sympt_user_inform = user_action['inform_slots']['Symptom'].pop(-1)
    if rand_noise:
        list_noise_sympt = last_sympt_user_inform.split('_')
        user_action['inform_slots']['Symptom'].append(random.choice(list_noise_sympt))
    else:
        noise_sympt = last_sympt_user_inform.split('_')[-1]
        user_action['inform_slots']['Symptom'].append(noise_sympt)

    return user_action

import re

def check_pattern(dis_list,inp):
    pred_list=[]
    patt = "^" + inp + "$"
    regexp = re.compile(inp)
    for item in dis_list:
        if regexp.search(item):
            pred_list.append(item)
    return pred_list

def check_available(list_sympt_query,list_user_inform):
    for item in list_sympt_query:
        
        for inform in list_user_inform:
            if len(item) < len(inform):
                regexp = re.compile(item)
                if not regexp.search(inform):
                    return item
            else:
                regexp = re.compile(inform)
                if not regexp.search(item):
                    return item

def freq_sympt_appear(list_statistic_sympt,list_unique_sympt_query):
    dict_count_sympt = {}

    for sympt in list_unique_sympt_query:
        dict_count_sympt[sympt] = list_statistic_sympt.count(sympt)

    dict_sort_sympt = dict(sorted(dict_count_sympt.items(), key=lambda item: item[1],reverse=True))
    return dict_sort_sympt

def flatten_lol(lol):
    sublist = []
    flat_list = [item for sublist in lol for item in sublist]
    return flat_list

def remove_multi_space(s):
    if s.startswith(' '):
        return s[1:]
    else:
        return s

def convert_constraint(constraints):
    """
    input dict các thực thể theo từng slot {entity_slot:[entity_mess]}
    return câu query mongodb
    form của câu query: { "$and": [{entity_slot:{"$all":[re.compile("entity_mess")]}},{},{}] }
    """

    list_and_out = []
    list_and_in = []
    regex_constraint_dict = {}

    for keys,values in constraints.items():
#         print(values)
        if not type(values) is list:
            values = []
        for value in values:
            list_and_in.append({
                    "$or" : [
                                {
                                    keys: {
                                        "$all": [re.compile(".*{0}.*".format(value))]
                                    }
                                }
                        ]
            })

    if list_and_in:
        list_and_out.append({"$and": list_and_in})
    if list_and_out:
        regex_constraint_dict = {"$and":list_and_out}

    return regex_constraint_dict

def gen_user_action(mess):
    user_action = {}

    extract_entity = mess.split(' ')

    for e in extract_entity:
        if '_' in e:
            inform_entity = e

    if mess.endswith('?'):
        user_action['intent'] = 'request'

        if inform_entity:
            user_action['inform_slots'] = {'Symptom':[inform_entity]}
        else:
            user_action['inform_slots'] = {}

        user_action['request_slots'] = {'Disease':'unk'}
    else:
        user_action['intent'] = 'inform'

        if inform_entity:
            user_action['inform_slots'] = {'Symptom':[inform_entity]}

        user_action['request_slots'] = {}

    return user_action
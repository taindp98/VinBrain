import itertools
from map_fsm import map_order_entity

dict_permute = {}
for key in list(map_order_entity.keys()):
    # list_permute_per_slot = []
    if key != 'all_slot':
        list_slot = map_order_entity[key]
        list_permute = list(itertools.permutations(list_slot))
        list_permute_fix = [[key] + list(item) for item in list_permute]

        dict_permute[key] = list_permute_fix

# print(dict_permute)

list_transition = []

for key in list(dict_permute.keys()):
    permute_per_slot = dict_permute[key]

    list_action_per_slot = []

    for permute_case in permute_per_slot:

        for idx, item in enumerate(permute_case):
            
            if idx < len(permute_case) - 1:
                dict_transition = {}
                dict_transition['trigger'] = 'into_' + str(permute_case[idx+1])
                dict_transition['source'] = item
                dict_transition['dest'] = permute_case[idx+1]

                if dict_transition not in list_transition:
                    list_transition.append(dict_transition)
    

print(list_transition)
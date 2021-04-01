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

dict_action_available = {}

for key in list(dict_permute.keys()):
    permute_per_slot = dict_permute[key]

    list_action_per_slot = []

    for sublist_permute in permute_per_slot:

        for idx, item in enumerate(sublist_permute):
            if idx < len(sublist_permute) - 1:
                action = str(item) + '_to_' + str(sublist_permute[idx+1])

                list_action_per_slot.append(action)
    
    dict_action_available[key] = list_action_per_slot

print(dict_action_available)
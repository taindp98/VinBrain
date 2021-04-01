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

print(dict_permute)
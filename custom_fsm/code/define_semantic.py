"""
	semantic of agent action as a dictionary:

	{
	"intent":<>,
	"inform_slots": <>,
	"request_slots": <>
	}

	type of "intent" field is string
	type of "inform_slots" field is list of string
	type of "request_slots" field is list of string
"""

## all possible intents of agent
"""
	"request": when agent want to ask user more information
	"inform": when agent want to confirm or suggest user about information
	"match_found": when agent find record satisfy all constraint from user
	"done": when agent want to end of conversation cause something
"""

LIST_AGENT_INTENT = ['request','inform','match_found','done']


## example agent's action with REQUEST semantic frame

agent_action['intent'] = 'request'
agent_action['inform_slots'] = []
agent_action['request_slots'] = ['entity_1','entity_2']

## example agent's action with INFORM semantic frame

agent_action['intent'] = 'inform'
agent_action['inform_slots'] = ['entity_1','entity_2']
agent_action['request_slots'] = []

## example agent's action with INFORM semantic frame

agent_action['intent'] = 'match_found'
agent_action['inform_slots'] = ['entity_1','entity_2']
agent_action['request_slots'] = []

## example agent's action with MATCH_FOUND semantic frame

agent_action['intent'] = 'match_found'
agent_action['inform_slots'] = ['entity_1','entity_2']
agent_action['request_slots'] = []

## example agent's action with DONE semantic frame

agent_action['intent'] = 'done'
agent_action['inform_slots'] = []
agent_action['request_slots'] = []
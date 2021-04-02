from transitions import Machine
import random
from map_fsm import map_order_entity
from gen_permute import list_transition

class CustomFSM(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...

    def __init__(self):

        # No anonymous superheroes on my watch! Every narcoleptic superhero gets
        # a name. Any name at all. SleepyMan. SlumberGirl. You get the idea.
        # self.name = name

        # What have we accomplished today?
        self.visited = {}
        self.preOrders = {}

        # Initialize states for FSM
        self.states = ['initial']
        # self.states = []

        self.currState = None

        # Assign Map Order Entity
        self.map_order_entity = map_order_entity

        # Iterating MapOrderEntity to Initializing States, Visited and preOrders
        for key, value in self.map_order_entity.items():
            # Add to States
            self.states.append(key)

            # Create a list of post order state (of current)
            postVisited = [key]

            #Iterating post-order state
            for postEntity in value:
                postVisited.append(postEntity)

                # If the first appearance of post-order state, generate its list of pre-order state
                if postEntity not in self.preOrders:
                    self.preOrders[postEntity] = []
                
                # Add current state as pre-order state
                self.preOrders[postEntity].append(key)

            self.visited[key] = postVisited

            # Generate list of pre-order state of current state
            if key not in self.preOrders:
                self.preOrders[key] = []

        # Initialize the state machine
        self.machine = Machine(model=self, states=self.states, transitions = list_transition ,initial='initial')
        
        # for state in self.states:
            # self.machine.add_transition(trigger='into_' + state, source='*', dest=state, after='switchIntocurrState')

        # print('='*50)
        # print('transition')
        # print(self.machine.add_transition)
        
    # def switchIntocurrState(self):
    #     currState = self.state
        
    #     print('currState',currState)
    #     # Check if this state havent met before
    #     if currState in self.visited[currState]:

    #         #remove state from its own Visited list as  allow termination at this
    #         self.visited[currState].remove(currState)
    #     # Remove this state from Visited lists where it present     
    #     for preOrder in self.preOrders[currState]:
    #         # Only removing when that PreOrder state is able to terminate (not have own state in VISITED list)
    #         if preOrder not in self.visited[preOrder]:
    #             self.visited[preOrder].remove(currState)
    #             self.preOrders[currState].remove(preOrder)
    #         # If that Pre-Order State's Visited List is null, terminate at that state
    #         if len(self.visited[preOrder]) == 0:
    #             print("Terminate!")





# allState = ['major_name','type_edu','subject_group','year','case','point','career','subject','tuition','major_code','criteria','object','register']

state1 = 'major_name'
testFSM = CustomFSM()

def recursive_find_best_way(state,count):
    attr = str(state)
    
    prev_state = state.copy()

    global map_state_per_key
    
    if count == 0:
        map_state_per_key = [state] + map_order_entity[state]

        print('map',map_state_per_key)

    if state in map_state_per_key:

        map_state_per_key.remove(state)

    if len(map_state_per_key) == 0:
        print('sucess')
        return True
    # print('current_state',testFSM.state)

    testFSM.state = prev_state

    func = getattr(testFSM,attr)
    func()

    next_state = testFSM.state
    
    print('next_state',next_state)
    count += 1

    if count == 5:
        return True
    recursive_find_best_way(next_state,count)
    

count = 0
recursive_find_best_way(state1,count)


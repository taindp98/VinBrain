Date: 31 Mar 2021

Categories: chatbot,nlp

# Task Dialogue Systems

## Characteristics
A task-oriented dialogue system is developed to perform a clearly defined task. Usually, the task involves finding information within a database and returning it to the user, performing an action, or retrieving information from its users.

## Technologies
Usually, the user’s input is processed by a natural language understanding (NLU) unit, which extracts the slots and their values from the utterance and identifies corresponding the dialogue act. This information is passed to the dialogue state tracker (DST), which infers the current state of the dialogue. Finally the output of the dialogue manager is passed to a natural language generation (NLG) component.

## Dialogue Management (DM)
The DM could be connected to some external Knowledge Base (KB) or Data Base (DB), such that it can produce more meaningful answers.

The Dialogue Manager consists the following two components:
	* The Dialogue State Tracker
	* Policy Learning (Reinforcement Learning Agent)

### Finite state machine
They are especially good when the number of things a user can say are limited. 

The FSM can change from one state to another in response to some external inputs; the change from one state to another is called a transition. A FSM is defined by a list of its states, its initial state, and the conditions for each transition.

External inputs are user inputs, typically arrive to the FSM in the form of parsed intent and slot values. External inputs are also called triggers or events in FSM parlance.

### Deep Q-Learning

### Evaluation
Two main aspects are evaluated, which have been shown to define the quality of the dialogue: 
	* Task-success
	* Dialogue efficiency

## Natural Language Generation
Natural language generation for dialogue systems
describes the task of converting a meaning representation (MR) into an utterance in a natural language. 

### Model
The goal of our model is to generate a text while
providing the ability of controlling various semantic and syntactic properties of this text. Model has two components:
	* The generator: the prediction of the next token is performed by sampling from the probability distribution
	* Multiple semantic control classifiers: classifier trained to detect which of its possible values is rendered in the text.

### Evaluation
Corpus-based metrics: BLEU-4 (Papineni et al., 2002), which computes the precision of the n-grams in the generated candidate with multiple reference utterances.

To assess the complexity of the generated utterances, employ the Lexical Complexity Analysers.


## Ref
https://medium.com/@BhashkarKunal/conversational-ai-chatbot-using-deep-learning-how-bi-directional-lstm-machine-reading-38dc5cf5a5a3

https://arxiv.org/pdf/1508.01745.pdf

http://www.macs.hw.ac.uk/InteractionLab/E2E/final_papers/E2E-ZHAW.pdf

https://solyarisoftware.medium.com/dialoghi-come-macchine-a-stati-41bb748fd5b0

https://medium.com/ai2-blog/alexafsm-a-finite-state-machine-python-library-for-building-complex-alexa-skills-61c3af5a299d

https://github.com/allenai/alexafsm

http://davekuhlman.org/fsm-transitions-python.html
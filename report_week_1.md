Date: 31 Mar 2021
Categories: chatbot,nlp

# Task Oriented Dialogue System
## Characteristics
A task-oriented dialogue system is developed to perform a clearly defined task. Usually, the task involves finding information within a database and returning it to the user, performing an action, or retrieving information from its users.

## Dialogue Structure
The dialogue structure for task-oriented systems is defined by two aspects: the content of the conversation and the strategy used within the conversation.

Content: The content of the conversation is derived from the domain ontology. The domain
ontology is usually defined as a list of slot-value pairs.

Strategy: While the domain ontology defines the content of the dialogue, the strategy to
fill the required slots during the conversation is modelled as a sequence of actions.

## Technologies
Usually, the user’s input is processed by a natural language understanding (NLU) unit, which extracts the slots and their values from the utterance and identifies corresponding the dialogue act. This information is passed to the dialogue state tracker (DST), which infers the current state of the dialogue. Finally the output of the dialogue manager is passed to a natural language generation (NLG) component.

## Evaluation
Two main aspects are evaluated, which have been shown to define the quality of the dialogue: 
 * Task-success
 * Dialogue efficiency




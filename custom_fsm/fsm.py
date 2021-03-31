from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    # def is_going_to_state1(self, update):
    def is_going_to_state1(self, text):
        # text = update.message.text
        return text.lower() == 'go to state1'

    # def is_going_to_state2(self, update):
    def is_going_to_state2(self, text):
        # text = update.message.text
        return text.lower() == 'go to state2'

    # def on_enter_state1(self, update):
    def on_enter_state1(self, text):
        # update.message.reply_text("I'm entering state1")
        # self.go_back(update)
        self.go_back(text)

    # def on_exit_state1(self, update):
    def on_exit_state1(self, text):
        print('Leaving state1')

    # def on_enter_state2(self, update):
    def on_enter_state2(self, text):
        # update.message.reply_text("I'm entering state2")
        self.go_back(text)

    # def on_exit_state2(self, update):
    def on_exit_state2(self, text):
        print('Leaving state2')

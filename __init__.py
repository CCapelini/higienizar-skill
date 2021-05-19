from mycroft import MycroftSkill, intent_file_handler


class Higienizar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('higienizar.intent')
    def handle_higienizar(self, message):
        self.speak_dialog('higienizar')


def create_skill():
    return Higienizar()


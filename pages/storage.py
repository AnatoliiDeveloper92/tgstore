import uuid

class StateManager():
    cart = {}
    def create_order(self, order):
        self.id = uuid.uuid4()
        self.order = {}
        self.client = ''

sm = StateManager()
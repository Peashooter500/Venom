DEFAULT_STATE = 0
TEXT_STATE = 1
IMAGE_STATE = 2

class FSM():
    def __init__(self):
        self.state = {}
    def get_state(self, uid):
        if uid not in self.state:
            self.state[uid] = DEFAULT_STATE
        return self.state[uid]
    def set_state(self, uid ,state):
        self.state[uid] = state
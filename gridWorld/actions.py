
class actions:

    def __init__(self):
        self.actions = ["AR", "AU", "AL", "AD"]
    
    def __getitem__(self, key):
        return self.actions[key]


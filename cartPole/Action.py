class Action:

    def __init__(self):
        a = ["left", "right"]

    def __getitem__(self, item):
        return self.a[item]
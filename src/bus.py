class Bus:

    def __init__(self, data:dict):
        for d in data:
            setattr(self, d, data[d])


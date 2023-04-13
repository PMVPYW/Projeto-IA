

class Parameter:

    def __init__(self, name: str, values: list):
        self.name = name
        self.values = values
        self.active_value_index = 0

    def get_active_value(self) -> str:
        return self.values[self.active_value_index]

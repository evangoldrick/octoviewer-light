from dataclasses import dataclass

@dataclass
class GCommand:
    command: str
    parameters: dict

    def __init__(self, command, parameters):
        self.command = command
        self.parameters = parameters

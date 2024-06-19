class CommandHandler:
    def __init__(self):
        """function passes commands"""
        self.commands = {}

    def register_command(self, name, command):
        """register function for commands"""
        self.commands[name] = command

    def execute_command(self, name):
        """execute function for commands"""
        command = self.commands.get(name)
        if command:
            command.execute()
        else:
            print(f"No such command: {name}")

class Command:
    def execute(self):
        raise NotImplementedError("Command subclasses must implement `execute` method")

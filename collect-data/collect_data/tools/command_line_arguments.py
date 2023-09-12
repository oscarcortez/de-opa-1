class CommandLineArguments:

    def __init__(self, arguments: []):
        self.arguments_len = len(arguments)
        self.arguments = arguments

    def get_type_data(self):
        if self.arguments_len > 1:
            return self.arguments[1]
        else:
            return 'streaming'

    def get_show_details(self):
        if self.arguments_len > 2:
            return self.arguments[2]
        else:
            return 'false'

    def is_helper(self):
        return self.arguments_len == 1
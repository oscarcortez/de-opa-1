import argparse
from tools.print_terminal_title import get_terminal_title
from tools.get_helper import get_helper
class ArgsReader:

    def __init__(self):

        description = ''
        description += get_terminal_title()
        description += get_helper()
        parser = argparse.ArgumentParser(description)
        parser.add_argument('--type_data', type=str, default='streaming', help='type of binance data')
        parser.add_argument('--printer', type=str, default='false', help='Pretty printer')        
        args = parser.parse_args()        
        self.type_data = args.type_data
        self.printer = args.printer

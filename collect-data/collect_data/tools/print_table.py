from prettytable import PrettyTable

def print_table(titles, values, show = True):
    
    if show:
        table = PrettyTable()
        table.field_names = titles
        table.add_row(values)        
        print(table)
from prettytable import PrettyTable

def showTable(rows, headers):
    x = PrettyTable()
    x.field_names = headers
    for row in rows:
        x.add_row(row)
    print(x)
    del x
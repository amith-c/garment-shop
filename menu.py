from consolemenu import SelectionMenu



def Menu():
    choices = [ 
        "Display all products" ,
        "Add a new product" ,
        "Modify a product",
        "Delete a product",
        "View remaining stock of product"
    ]
    selection = SelectionMenu.get_selection(choices, "Garment Shop Management System", "Enter an option")
    return selection+1
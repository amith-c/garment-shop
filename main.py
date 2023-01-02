import database 
import keyboard
import os
import time
from table import showTable
from colorama import init, Style, Fore

init()


def main():
    while True:
        os.system('cls')
        print("Garment Shop Management System")
        print(Style.DIM + "Enter an option\n" + Style.NORMAL)
        print("Press the corresponding number:")
        print("1. Display all products")
        print("2. Add a new product")
        print("3. Modify a product")
        print("4. Delete a product")
        print("5. Search a product")
        print("6. Exit")

        while True:
            try:      
                if keyboard.is_pressed("1"):
                    displayProducts()
                    break
                if keyboard.is_pressed("2"):
                    insertNewProduct()
                    break
                if keyboard.is_pressed("3"):
                    modifyProduct()
                    break
                if keyboard.is_pressed("4"):
                    deleteProduct()
                    break
                if keyboard.is_pressed("5"):
                    search()
                    break
                if keyboard.is_pressed("6"):
                    return
            except:
                break


def displayProducts():
    os.system("cls")  # Used to clear the output screen
    recs = database.readAllRecords()
    showTable(recs, headers=["ID", "Product Name", "Company", "Price", "Stock"])
    input("\nPress Enter to continue...")
    
def insertNewProduct():
    os.system("cls")
    try:
        id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        company = input("Enter company: ")
        price = int(input("Enter product price: "))
        stock = int(input("Enter stock remaining: "))
    except:
        print(Fore.RED + "ERROR: Only integers are allowed for ID, price and stock." + Fore.WHITE)
        input("Press Enter to retry.")
        insertNewProduct()
    try:
        database.insertProduct(id, name, company, price, stock)
        print("Record inserted successfully.")
        time.sleep(1)
    except:
        print("There was an error inserting the record.")

def modifyProduct():
    os.system('cls')
    try:
        id = int(input("Enter ID of product whose details are to be modified: "))
    except:
        print(Fore.RED + "ERROR: Only integers are allowed." + Fore.WHITE)
        input("Press Enter to retry.")
        modifyProduct()

    rec = database.readOneRecord(id)
    print("Enter modified details. Leave it blank if you do not wish to modify a certain detail.")
    new_name = input("Name[%s]: "%(rec[1], ))
    new_company = input("Company[%s]: "%(rec[2], ))
    try:
        new_price = int(input("Price[%s]: "%(rec[3], )))
        new_stock = int(input("Stock remaining[%s]: "%(rec[4], )))
    except:
        print(Fore.RED + "ERROR: Only integers are allowed." + Fore.WHITE)
        input("Press Enter to retry.")
        modifyProduct()
    name = new_name or rec[1]
    company = new_company or rec[2]
    price = new_price or rec[3]
    stock = new_stock or rec[4]
    database.updateRecord(id, name, company, price, stock)

    print("Record updated successfully.")  
    input("Press Enter to continue...")  



def deleteProduct():
    os.system('cls')
    try:
        id = int(input("Enter ID of product to be deleted: "))
    except:
        print(Fore.RED + "ERROR: Only integers are allowed." + Fore.WHITE)
        input("Press Enter to retry.")
        deleteProduct()
    
    database.deleteProduct(id)
    print("Record has been deleted.")  
    input("Press Enter to continue...")  

def search():
    os.system("cls")  # Used to clear the output screen
    try:
        id = int(input("Enter ID of product to search: "))
    except:
        print(Fore.YELLOW + "WARNING: Only integers are allowed." + Fore.WHITE)
        input("Press Enter to retry.")
        search()
    record = database.readOneRecord(id)
    if record == None:
        print(Fore.RED + "ERROR: Record wasn't found." + Fore.WHITE)
    else:
        showTable([record], ["ID", "Product Name", "Company", "Price", "Stock"])
    input("\nPress Enter to continue...")  

main()

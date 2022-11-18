import database 
import keyboard
import os
from tabulate import tabulate


def main():
    running = True
    while running:
        os.system('cls')
        print("Garment Shop Management System\n")
        print("Press the corresponding number:")
        print("1. Display all products")
        print("2. Add a new product")
        print("3. Modify a product")
        print("4. Delete a product")
        print("5. View remaining stock of product")
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
                    insertNewProduct()
                    break
                if keyboard.is_pressed("5"):
                    showStock()
                    break
                if keyboard.is_pressed("6"):
                    return
            except:
                break


def displayProducts():
    os.system("cls")  # Used to clear the output screen
    recs = database.readAllRecords()
    print(tabulate(recs, headers=["ID", "Product Name", "Company", "Price", "Stock"]))
    input("\nPress Enter to continue...")
    
def insertNewProduct():
    os.system("cls")
    id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    company = input("Enter company: ")
    price = int(input("Enter product price: "))
    stock = int(input("Enter stock remaining: "))
    try:
        database.insertProduct(id, name, company, price, stock)
    except:
        print("There was an error inserting the record.")

def modifyProduct():
    os.system('cls')
    id = input("Enter ID of product whose details are to be modified: ")
    rec = database.readOneRecord(id)
    print("Enter modified details. Leave it blank if you do not wish to modify a certain detail.")
    new_name = input("Name[%s]: "%(rec[1], ))
    new_company = input("Company[%s]: "%(rec[2], ))
    new_price = input("Price[%s]: "%(rec[3], ))
    new_stock = input("Stock remaining[%s]: "%(rec[4], ))
    name = new_name or rec[1]
    company = new_company or rec[2]
    price = new_price or rec[3]
    stock = new_stock or rec[4]
    database.updateRecord(id, name, company, price, stock)

    print("Record updated successfully.")  
    input("Press Enter to continue...")  



def deleteProduct():
    os.system('cls')
    id = int(input("Enter ID of product to be deleted: "))
    database.deleteProduct(id)

def showStock():
    os.system("cls")  # Used to clear the output screen
    id = int(input("Enter ID of product to search: "))
    recs = database.readOneRecord(id)
    print(tabulate(recs, headers=["ID", "Product Name", "Company", "Price", "Stock"]))
    input("\nPress Enter to continue...")  

main()

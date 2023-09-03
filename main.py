# Packages
import csv

# Functions
def display_menu():
  print(
"""
----------------------------
Welcome to GDS Data Manager 
----------------------------
Main Menu
----------------------------
1. Add Customer
2. Edit Customer
3. Remove Customer
4. List Customers
5. Search Customer
6. Save Customers
7. Load Customers
8. Exit
----------------------------
"""
  )

def list_customer(customers):
  print('\nList of Customers\n')
  if not customers:
    print('No customers in list')
  else:
    for index, customer in enumerate(customers):
      print((index+1), '.', customer)

def add_customer(customers):
  while True:
    print('\nAdd a New Customer')
    name = input("\nEnter name or enter blank to go back: ")
    if not name:
      print("\nBlank input, going back...")
      break
    email = input("\nEnter email or enter blank to go back: ")
    if not email:
      print("\nBlank input, going back...")
      break
    mobile = input("\nEnter mobile number or enter blank to go back: ")
    if not mobile:
      print("\nBlank input, going back...")
      break
    new_customer = {
        "name": name,
        "email": email,
        "mobile": mobile
    }
    customers.append(new_customer)
    print('\nAdded Succesfully')
    break

def edit_customer(customers):
  print('\nEdit an Existing Customer')
  while True:
    if not customers:
      print('\nNo customers in list')
      break
    else:
      list_customer(customers)
      which_index = input('\nSelect the index you want to edit or enter blank to go back: ')
      if which_index == (''):
        print("\nBlank input, going back...")
        break
      else:
        which_index = (int(which_index)) - 1
        if which_index < 0 or which_index >= len(customers):
          print ('\nInvalid index entered')
        else:
          new_name = input('\nEnter new name or enter blank to go back: ')
          if not new_name:
            print("\nBlank input, going back...")
            break
          new_email = input('\nEnter new email or enter blank to go back: ')
          if not new_email:
            print("\nBlank input, going back...")
            break
          new_mobile = input("\nEnter new number or enter blank to go back: ")
          if not new_mobile:
            print("\nBlank input, going back...")
            break
          customers[which_index] = {
            "name": new_name,
            "email": new_email,
            "mobile": new_mobile
            }
          print('\nEdited Succesfully')
          break

def remove_customer(customers):
  print('\nRemove a Customer')
  while True:
    if not customers:
      print('\nNo customers in list')
      break
    else:
      list_customer(customers)
      which_index = input('\nSelect the index you want to remove or enter blank to go back: ')
      if which_index == (''):
        print("\nBlank input, going back...")
        break
      else:
        which_index = (int(which_index)) - 1
        if which_index < 0 or which_index >= len(customers):
          print ('\nInvalid index entered')
        else:
          del customers[which_index]
          print('\nRemoved Succesfully')
          break

def search_customer(customers):
  while True:
    print('\nSearch Customer')
    if not customers:
      print('\nNo customers in list')
      break
    else:
      new_dictionary = []
      search_critera = input("\nPlease enter the name/email/mobile or enter blank to go back: ")
      if search_critera == '':
        print("\nBlank input, going back...")
        break
      else:
        for index, customer in enumerate(customers):
          if customer["name"].lower() == search_critera.lower() or customer["email"].lower() == search_critera.lower() or customer["mobile"] == search_critera:
            print(index + 1, customer["name"], customer["email"], customer["mobile"])
            new_dictionary.append(customer)
      if len(new_dictionary) == 0:
        print('\nNo matching data')

def save_customer(customers):
  print('\nSaving Customers...')
  file_ptr = open("data.csv", "w", newline="")
  headers = ["name", "email", "mobile"]
  csv_writer = csv.DictWriter(file_ptr, fieldnames=headers)
  csv_writer.writeheader()
  for customer in customers:
    csv_writer.writerow(customer)
  file_ptr.close()
  print('\nFile saved successfully')

def load_customer(customers):
  try:
    print('\nLoading Customers...')
    with open("data.csv", "r") as file_ptr:
      customers.clear()
      csv_reader = csv.reader(file_ptr, delimiter=",")
      next(csv_reader, None)
      for row in csv_reader:
        name = row[0]
        email = row[1]
        mobile = row[2]

        new_customer = {
          "name": name,
          "email": email,
          "mobile": mobile
        }
        customers.append(new_customer)
    print('\nFile loaded successfully')
  except FileNotFoundError:
    print('\nNo file found')

# choice function
def main():
  customers = []
  while True:
    display_menu()
    choice = int(input('Please enter your choice: '))
    if choice == 1:
      add_customer(customers)
    elif choice == 2:
      edit_customer(customers)
    elif choice == 3:
      remove_customer(customers)
    elif choice == 4:
      list_customer(customers)
    elif choice == 5:
      search_customer(customers)
    elif choice == 6:
      save_customer(customers)
    elif choice == 7:
      load_customer(customers)
    elif choice == 8:
      print('\nExiting the program')
      break
    else:
      print('\nWrong input, try again')
  print('\nProgram Exited\n')

if __name__ == "__main__":
  main()
import csv

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
  print('\nAdd a New Customer\n')
  name = input("Enter name: ")
  email = input("Enter email: ")
  mobile = input("Enter number: ")
  new_customer = {
      "name": name,
      "email": email,
      "mobile": mobile
  }
  customers.append(new_customer)
  print('\nAdded Succesfully')

def edit_customer(customers):
  print('\nEdit an Existing Customer\n')
  while True:
    if not customers:
      print('\nNo customers in list')
      break
    else:
      list_customer(customers)
      which_index = int(input('Select the index you want to change: ')) - 1
      if which_index < 0 or which_index > len(customers):
        print ('\nInvalid index entered')
      else:
        new_name = input('Enter new name: ')
        new_email = input('Enter new email: ')
        new_mobile = input("Enter new number: ")
        customers[which_index] = {
          "name": new_name,
          "email": new_email,
          "mobile": new_mobile
          }
        print('\nEdited Succesfully')
        break

def remove_customer(customers):
  print('\nRemove a Customer\n')
  while True:
    if not customers:
      print('\nNo customers in list')
      break
    else:
      list_customer(customers)
      which_index = int(input('Select the index you want to remove: ')) - 1
      if which_index < 0 or which_index > len(customers):
        print ('\nInvalid index entered')
      else:
        del customers[which_index]
        print('\nRemoved Succesfully')
        break

def search_customer(customers):
  print('\nSearch Customer\n')
  new_dictionary = []
  search_critera = input("Please enter the name/email/mobile: ")
  for index, customer in enumerate(customers):
    if customer["name"].lower() == search_critera.lower() or customer["email"].lower() == search_critera.lower() or customer["mobile"] == search_critera:
      print(index + 1, customer["name"], customer["email"], customer["mobile"])
      new_dictionary.append(customer)
  if len(new_dictionary) == 0:
    print('No matching data')

def save_customer(customers):
  print('\nSaving Customers')
  file_ptr = open("data.csv", "w", newline="")
  headers = ["name", "email", "mobile"]
  csv_writer = csv.DictWriter(file_ptr, fieldnames=headers)
  csv_writer.writeheader()
  for customer in customers:
    csv_writer.writerow(customer)
  file_ptr.close()
  print('\nFile saved successfully')

def load_customer(customers):
  print('\nLoading Customers')
  customers.clear()
  file_ptr = open("data.csv", "r")
  csv_reader = csv.reader(file_ptr, delimiter=",")
  next(csv_reader, None)
  for row in csv_reader:
    
    name = row[0]
    email = row[1]
    mobile = row[2]

    new_customer = {
      "name": row[0],
      "email": row[1],
      "mobile": row[2]
    }
    
    customers.append(new_customer)
  file_ptr.close()
  print('\nFile loaded successfully')

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
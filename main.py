#import mysql.connector
#connection = mysql.connector.connect(user = ‘username’, database = ‘database_name’, password = ‘password’)
#connection.close()

def main_menu():
  print("--------------------------")
  print("1. CHECK ACCOUNT BALANCE \n")
  print("2. DEPOSIT FUNDS$\n")
  print("3. WITHDRAW FUNDS$\n")
  print("4.MODIFY ACCOUNT INFORMATION\n")
  print("5. EXIT\n")
  print("--------------------------")    

def login_menu():  
  print("--------------------------")
  print("Hello! Welcome to iBank! \n")
  print("1. LOGIN\n")
  print("2. SIGN UP\n")
  print("3. EXIT\n")
  print("--------------------------")
login_menu()
ask_user = input("What would you like to do?")

if ask_user == "1":
  account_ID=input("Please input your acount ID")
  password=input("Please input your password")
  print("Welcome ___")
  main_menu()
  

if ask_user =="2":
  print("Please input the following")
  user_firstname=input("First Name:")
  user_lastname = input("Last Name")
  user_age=input("Age:")
  if user_age < "18":
    print("Sorry, you are too young to create an account on iBank")
    print("Goodbye!")
    login_menu()
    
  user_address = input("Address:")
  user_email = input("Email:")
  user_phone_number = input("Phone # :")
  print("You have officially made an account with iBank!")  

if ask_user =="3":
    print("Goodbye!")
    quit()
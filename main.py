


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
  

if ask_user =="2":
  user_name=input("Please input your name:")
  user_age=input("Plese input your age:")
  if user_age < "18":
    print("Sorry, you are too young to create an account on iBank")
    print("Goodbye!")
    login_menu()
    
  user_address = input("Please input your address")  

if ask_user =="3":
    print("Goodbye!")
    quit()
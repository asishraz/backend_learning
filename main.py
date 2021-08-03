print("create account now")

user_name = input("Enter your name: ")
user_pwd = input("Enter your password: ")

print("your account has been created successfully!")
print("Login Now")


user_name2 = input("enter your name: ")
user_pwd2 = input("enter your password: ")

if user_name == user_name2 and user_pwd == user_pwd2:
    print("login successful")
else:
    print("Invalid credentials")
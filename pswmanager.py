import time

# Displays and asks Name and Password

print("Enter name")
name = input()
print("Enter password")
password = input()
print("Name and password saved.")

# Writes on file

file = open("passwords.txt", "a")
file.write("\n")
file.write("Name: ")
file.write(name)
file.write("\n")
file.write("Password: ")
file.write(password)
file.write("\n")

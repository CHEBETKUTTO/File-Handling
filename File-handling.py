file = open("linda is an awesome art enthusiast.txt", "w")
file.write("Linda is an awesome art enthusiast")
file.close()
file = open("linda is an awesome art enthusiast.txt", "r")
content = file.read()
print(content)
file.close()

#Modify the file content to "Linda is an awesome art enthusiast and a great cook"
file = open("linda is an awesome art enthusiast.txt", "a")
file.write(" and a great cook")
file.close()    

print("File content modified successfully.")

file = open("linda is an awesome art enthusiast.txt", "r")
content = file.read()
print(content)
file.close()

try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("The file was not found.")

try:
    file = open("/root/secret_file.txt", "r")
    content = file.read()
    print(content)
    file.close()
except PermissionError:
    print("You do not have permission to access this file.")
except Exception as e:
    print(f"An error occurred: {e}")

    


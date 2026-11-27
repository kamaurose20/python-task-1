# File Exception Handling

try:
    file = open("employees.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("The employee file was not found.")

finally:
    print("File processing completed.")
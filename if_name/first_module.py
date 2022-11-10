print("Module #1 Name=", __name__)

print("This code will always execute.")

def main():
   print("This code belongs to the main function in module 1.")

if __name__ == "__main__":
   main()

# the name of the import matches the file name (minus the .py)
# these two files MUST BE IN THE SAME DIRECTORY
import first_module

first_module.main() # ADD THIS LINE

print("Module #2 Name=", __name__)



import requests
import sys
import yaml

def main():
    arg_length = len(sys.argv)

    if arg_length < 2:
         print("Not enough arguments. Usage: python main.py <file_name>")
         sys.exit(1)
    
    elif arg_length > 2:
         print("Too many arguments. Usage: python main.py <file_name>")
         sys.exit(1)
    
    with open(sys.argv[1], 'r') as yaml_file:
         data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    
    print(data)

if __name__ == "__main__":
    main()
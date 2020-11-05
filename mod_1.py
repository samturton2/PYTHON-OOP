# using __name__ and __main__

print("this is a mod_1 name --->" + __name__)

def main():
    pass # keyword pass helps you pass without an error

# Syntax: if __name__ == "__main__":
if __name__ == "__main__": # Checks if code is run from current file
    main()
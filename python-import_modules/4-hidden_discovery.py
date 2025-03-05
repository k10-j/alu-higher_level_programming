#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in the module
    names = dir(hidden_4)
    
    # Print only names that don't start with '__'
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name itself
    argc = len(argv)
    
    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} argument{'s' if argc > 1 else ''}:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()

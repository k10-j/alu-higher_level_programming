#!/usr/bin/python3

import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name itself
    total = sum(int(arg) for arg in argv)  # Convert to integers and sum
    print(total)

if __name__ == "__main__":
    main()


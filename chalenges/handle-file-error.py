import sys
import os

def fileToOpen(file):
    if os.path.exists(file):
        with open(file, "r") as file:
            files = file.read()
            print(files)
        return files
    else:
        allErrors(file)

def allErrors(syntax):
    error = sys.exc_info()
    if os.path.exists(syntax):
        try:
            open(syntax)
        except :
            print(error)

    else:
       print(f"the file '{syntax}' does not exist")


def main():
    print("\nhello! and welcome to the file shelf\nWe sure do have a lot of files to offer so please feel free to check them out\nalso remember to specify the full file path and exeption\neg. \"fileline.exention\"\n")
    file = input("so which file do you want to look at? ")
    fileToOpen(file)

main()
import os

def createFile(data, files):
   
    if data != "CSV" and data !="TXT":
        print(f"error! cannot (GET) file format {data}")
        data = input("what kind of data file do you want to write? ").upper()

    file_name = f"{files}.{data}"
    if os.path.exists(file_name):
        checkifFileExists(files,data,file_name)
    else:
        myFile = open(file_name, 'w')
        info = input(f"which info would you like placed in your {file_name} ")
        myFile.write(info)
        myFile.close()
        print(f"file writen succesfully to {file_name}")

    return 
    
def checkifFileExists(files,data,file_name):
        # file_name = f"{files}.{data}".lower()
        checkFile = input(f"this file ({file_name}) alredy exists. Do you want to rename?\n(yes/no) ").upper()
        if checkFile == "YES" or checkFile == "Y":
            newName = input(f"Which Name Would Like To give your {data} file? ").lower()
            new_file_name = (f"{newName}.{data}")
            checkPath = os.path.exists(new_file_name)
            if checkPath:
                print(f"this file ({new_file_name}) alredy exists. try a new name") 
            else:
                os.rename(file_name, new_file_name)
                print(f"file renamed to {newName}")

        elif checkFile == "NO" or checkFile == "N":
            filePath = input("\nok!, Would You Like To Remove existing file? ").upper()
            if filePath == "YES" or filePath == "Y":
                os.remove(file_name)
                print(f"file {files}.{data} has been removed")
            else:
                fileSearch(files, data)
        else:
            print("error!")

        return


def fileSearch(files, data):
    checkForFile = input("\nSearch for a file path to see if it exists: ")
    
    while "." not in checkForFile:
        print("\nWow! That is not a file path. File paths include the extension data, e.g., 'file.csv'")
        checkForFile = input("Try a full file path: ")
    
    checkForFiles = f"{checkForFile}"
    
    if os.path.exists(checkForFiles):
        print("\nThe file already exists.")
        checkFile = input("Would you like to search for another file? (yes/no): ").upper()
        
        if checkFile == "YES" or checkFile == "Y":
            fileSearch(files, data)
        else:
            print("\nHave a good one and thank you for using z-file search.")
    else:
        print(f"Cannot find {checkForFiles}.")




def main():
    print("\ntxt\ncsv\n")
    data = input("what kind of data do you want to write? ").upper()
    files = input("name of file: ")
    createFile(data,files)
main()
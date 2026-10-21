# Open the file names.txt and read its contents and print the number of names

with open("names.txt") as file_object:
    names = file_object.readlines()
    print(len(names))
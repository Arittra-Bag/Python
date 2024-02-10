try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as file:
        for line in file.readlines():
            print(line[::-1])
except Exception as e:
        print("Error Occured: ",e)
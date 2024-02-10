try:
    file_name = input("Enter the file name: ")
    out_name = input("Enter the Output File Name: ")
    with open(file_name, 'r') as file:
        with open(out_name, 'w') as out:
            out.write(file.read().upper())
except Exception as e:
    print("Error Occured: ",e)
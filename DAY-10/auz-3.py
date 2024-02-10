try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as file:
        with open('rev_file.txt', 'w') as out:
            out.write(file.read()[::-1])
except Exception as e:
    print("Error Occured: ",e)
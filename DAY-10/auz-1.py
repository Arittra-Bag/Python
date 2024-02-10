try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as file:
        num_words = len(file.read().split())
        print(f"The number of words in the file '{file_name}' is: {num_words}")
except Exception as e:
        print(e)
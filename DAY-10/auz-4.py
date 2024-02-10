try:
    with open('input.bin', 'rb') as input_file, open('output.bin', 'wb') as output_file:
        first_100_chars = input_file.read(100)
        output_file.write(first_100_chars)
    print("Copy successful.")
except Exception as e:
    print(f"An error occurred: {e}") 

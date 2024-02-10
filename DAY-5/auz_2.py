rows_a=int(input("Enter the Number of Rows for Matrix A: "))
cols_a=int(input("Enter the Number of Columns for Matrix A: "))
rows_b=int(input("Enter the Number of Rows for Matrix B: "))
cols_b=int(input("Enter the Number of Columns for Matrix B: "))
if cols_a!=rows_b:
    print("Multiplication of Matrices is not possible!")
else:
    matrix_a=[]
    print("Enter the elements for Matrix A:")
    for i in range(rows_a):
        row=[]
        for j in range(cols_a):
            element = int(input(f"Enter the Value for Row-{i+1} Column-{j+1}: "))
            row.append(element)
        matrix_a.append(row)

    matrix_b=[]
    print("Enter the elements for Matrix B:")
    for i in range(rows_b):
        row=[]
        for j in range(cols_b):
            element = int(input(f"Enter the Value for Row-{i+1} Column-{j+1}: "))
            row.append(element)
        matrix_b.append(row)

    result=[[0 for j in range(cols_b)]for i in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j]+=matrix_a[i][k]*matrix_b[k][j]
    
    print("Resultant Matrix:")
    for row in result:
        print(str(row).replace(","," "))
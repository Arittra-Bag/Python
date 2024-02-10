l=list(input("Enter the Numbers(with space): ").split())
min_num=l[0]
max_num=l[0]
for num in l:
    if num>max_num:
        max_num=num
    if num<min_num:
        min_num=num
print(f"Max. Number={max_num}\nMin. Number={min_num}")
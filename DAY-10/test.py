ifile=input("Enter the file name: ")
with open(ifile,'r') as file:
    s=file.read().strip()
    s=s.strip('[]')
    s=s.split(',')
    l=[int(ele) for ele in s]
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    print(sum)

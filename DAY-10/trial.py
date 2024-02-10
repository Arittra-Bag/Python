#For List in Text File
ifile=input("Enter the file name: ")
with open(ifile,'r') as file:
    l1=file.readline().strip()
    l2=file.readline().strip()
l1=l1.strip('[]').split(',')
l2=l2.strip('[]').split(',')
l1=[int(ele) for ele in l1]
l2=[int(ele) for ele in l2]
l3=[l1[i]+l2[i] for i in range(len(l1))]
print(l3)

#For Dictionary in Text File
ifile=input("Enter the file name: ")
with open(ifile,'r') as file:
    s=file.read().strip().strip('{}').replace("'",'').split(',')
    d={}
    for pair in s:
        key,value=pair.split(':')
        d[key.strip()]=int(value.strip())
    print(d)

#For Tuple in Text File
ifile=input("Enter the file name: ")
with open(ifile,'r') as file:
    s=file.read().strip().strip('()').split(',')
    t=tuple([int(ele) for ele in s])
    print(t)

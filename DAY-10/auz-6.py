try:
    ifile=input("Enter the file name: ")
    ofile=input("Enter the Output File Name: ")
    with open(ifile,'r') as file:
        with open(ofile,'w') as out:
            comb = False
            for line in file:
                if "'''" in line:
                    comb = not comb
                    continue
                elif comb:
                    continue
                elif line.strip().startswith('#') or '#' in line:
                    out.write(line.split('#')[0])
                else:
                    out.write(line)
    print("Copy successful.")
except Exception as e:
    print("Error Occured: ",e)

a=int(int(input("Enter First No.:")))
b=int(int(input("Enter Second No.:")))
if(a<b):
    divisor=a
    dividend=b
else:
    divisor=b
    dividend=a
while(divisor>0):
    remainder=dividend%divisor
    dividend=divisor
    divisor=remainder
print("GCD:",dividend)
t=int(input("enter the temp. yuo want to convert: "))
s=input("enter the scale you want to convert to (C/F):").upper()
celcius=lambda t: (t-32)*5/9
farenheight=lambda t: (t*9/5)+32
if s=="C":
    celcius_temp=celcius(t)
    print(f"{t}F is {celcius_temp}C")
elif s=="F":
    farenheight_temp=farenheight(t)
    print(f"{t}C is {farenheight_temp}F")
    
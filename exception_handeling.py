
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
    print("Result:",result)

except Exception as e:
    print("Error:",e)
else:
    print("No errors occurred.")
finally:
    print("Execution completed.")
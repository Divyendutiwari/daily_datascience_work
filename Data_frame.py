import pandas as pd
data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["John Smith", "Jane Doe", "Emily Davis", "Michael Brown", "Linda Johnson"],
    "Age": [29, 34, 26, 41, 31],
    "Department": ["Marketing", "Engineering", "Human Resources", "Finance", "Sales"]
}
df=pd.DataFrame(data)
print(df)
print(type(df))
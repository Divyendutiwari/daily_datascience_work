import pandas as pd
df_employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104],
    "Name": ["John Smith", "Jane Doe", "Emily Davis", "Michael Brown"],
    "DepartmentID": [1, 2, 1, 3]
   })
df_departments = pd.DataFrame({
    "DepartmentID": [1, 2, 3],
    "DepartmentName": ["Marketing", "Engineering", "Finance"]
   })
print(pd.merge(df_departments,df_employees,on="DepartmentID",how="inner"))
print(pd.merge(df_departments,df_employees,on="DepartmentID",how="outer"))
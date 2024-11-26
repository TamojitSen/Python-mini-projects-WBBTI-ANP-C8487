basic_salary = int(input("Enter the Basic Salary of the Employee: "))
if (basic_salary <1500):
    HRA = basic_salary * 0.10
    DA = basic_salary * 0.90
    gross_salary = basic_salary + HRA + DA
    print(f'Gross Salary of the employee is: {gross_salary}')
elif (basic_salary >= 1500):
    HRA = 500
    DA = basic_salary * 0.98
    gross_salary = basic_salary + HRA + DA
    print(f'Gross Salary of the employee is: {gross_salary}')
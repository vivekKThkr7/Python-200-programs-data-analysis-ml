# Employee Salary Analyzer

employees = {
    "Ram": 2500,
    "Sita": 3500,
    "Hari": 1800,
    "Gita": 4200
}

high_salary = {
    name: salary
    for name, salary in employees.items()
    if salary > 3000
}

print(high_salary)
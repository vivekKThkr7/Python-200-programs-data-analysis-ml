employees = {
    "Ram": 2500,
    "Sita": 3500,
    "Hari": 1800,
    "Gita": 4200,
    "Mohan": 3000
}

high_salary_employees = {
    name: salary
    for name, salary in employees.items()
    if salary >= 3000
}

print("High salary employees:")

for name, salary in high_salary_employees.items():
    print(f"{name} → {salary}")

average_salary = sum(high_salary_employees.values()) / len(high_salary_employees)
print("Average salary:", average_salary)

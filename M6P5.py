last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
job_level = int(input("Enter employee job level: "))
if job_level >= 10:
    bonus = 0.25
elif job_level >= 5:
    bonus = 0.2
else:
    bonus = 0.1
Tol_bonus = salary * bonus
print("Last Name:", last_name)
print("Bonus:", Tol_bonus)
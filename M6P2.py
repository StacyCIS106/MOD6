part_num = int(input("Enter the part number: "))
quant = int(input("Enter the quantity: "))
if part_num == 10 or part_num == 55:
    cost_unit = 1
elif part_num == 99:
    cost_unit = 2
elif part_num == 80 or part_num == 70:
    cost_unit = 3
else:
    cost_unit = 5
tol_cost = quant * cost_unit
print("Part Number:", part_num)
print("Cost per unit:", cost_unit)
print("Total Cost:", tol_cost) 


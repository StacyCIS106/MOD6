num_tiks = int(input("Enter the number of tickets: "))
if num_tiks >= 25:
    cost_per_ticket = 50
elif num_tiks >= 10:
    cost_per_ticket = 60
elif num_tiks >= 5:
    cost_per_ticket = 70
else:
    cost_per_ticket = 75
total_cost = num_tiks * cost_per_ticket
print("Number of Tickets:", num_tiks)
print("Cost per Ticket:", cost_per_ticket)
print("Total Cost:", total_cost)
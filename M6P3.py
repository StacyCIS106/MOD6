princ_amount = int(input("Enter the principal amount of a CD: "))
year_maturity = int(input("Enter the year maturity of the CD: "))
if princ_amount > 1000000 and year_maturity == 5:
    interest_rate = 0.06
elif princ_amount <= 1000000 and year_maturity == 10:
    interest_rate = 0.05
elif princ_amount <= 1000000 and year_maturity == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
first_year_interest = princ_amount * interest_rate
print("Principal Amount:", princ_amount)
print("Interest Rate:", interest_rate)
print("First Year Interest:", first_year_interest)
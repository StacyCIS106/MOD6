quant_wid = int(input("Enter the quantity widgets: "))
if quant_wid > 10000:
    price_charge = 10
elif quant_wid <= 10000:
    price_charge = 20
else:
    price_charge = 30
ext_price = quant_wid * price_charge
tax = ext_price * 0.07
total = ext_price + tax
print("Extended Price:", ext_price)
print("Tax:", tax)
print("Total:", total)
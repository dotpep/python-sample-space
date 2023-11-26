# bill = 175.00
# tax_rate = 15
# total_tax = (bill * tax_rate) / 100.00
#
# print("Total tax: ", total_tax)


###

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2) # 42.0461 to 42.05 (show 2 decimal numbers and round it)


print("Total tax: (with func)", calculate_tax(175.00, 15))
print("Total tax: (with func 2)", calculate_tax(247.33, 17))

tax_case3 = calculate_tax(2200.3566, 100)
print("Total tax: (with func 3)", tax_case3)

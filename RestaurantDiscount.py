bill = float(input ("Input your bill."))
if bill > 50:
    discount = bill * 0.1
    finalbill = bill - discount
    print("This is your bill with discount £",finalbill)
else:
    print("This is your bill. £",bill)
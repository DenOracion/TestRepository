age = int(input ("How old are you?")) #customer will be asked to input their age

if age >= 65:
    print("Your ticket costs £6")
elif age <= 64 and age >= 18:
    print("Your ticket costs £10")
elif age <= 17 and age >= 12:
    print("Your ticket costs £7")
else:
    print("Your ticket costs £5")

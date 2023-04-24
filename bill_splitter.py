print("Welcome to the bill splitter!!")
print("NOTE: Every input must be in number format")
bill=input("Enter the total bill :")
person=input("Enter number of persons you wanna slpit the bill :")
tip=input("How much percent of tip you wanna give :")
p=int(person)
t=float(tip)
b=float(bill)
each_pay=b/p
each_tip=each_pay*(t/100)
e_pay=each_pay+each_tip
print("{:.2f}".format(e_pay))

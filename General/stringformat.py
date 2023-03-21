#string format()
price = 90
txt1 = "The price is {:.2f} dollars"
txt = "The price is {} dollars"
print(txt1.format(price))
print(txt.format(price))

#index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number{1} for {2:.2f} dollars"
print(myorder.format(quantity,itemno,price))
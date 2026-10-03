cust_name = input("Enter customer name: ")
prod_name1 = input("Enter the 1st Product name: ")
price1 = float(input("Enter the 1st price: "))
Quantity1 = int(input("Enter the 1st Quantity: "))

prod_name2 = input("Enter the 2nd Product name: ")
price2 = float(input("Enter the 2nd price: "))
Quantity2 = int(input("Enter the 2nd Quantity: "))

totalprice1 = price1 * Quantity1
totalprice2 = price2 * Quantity2
total = totalprice1 + totalprice2

Doubleline = "======================================"
line = "------------------------"

print(f"{Doubleline}\n{'RECEIPT':^15}\n{Doubleline}\n\nCustomer: {cust_name}\n\n{'Product':<15}{'price':<8}{'Qty':<5}\n{line}")
print(f"{prod_name1:<15}{price1:<8}ETB{Quantity1:<5}")
print(f"{prod_name2:<15}{price2:<8}ETB{Quantity2:<5}")
      
print(F"Total: {total}\n\nThank you for shopping!\n{Doubleline}")
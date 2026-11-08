def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["price"]*item["quantity"]
    return subtotal

def calculate_discount(subtotal):
    if subtotal < 1000:
        discount = 0
    elif subtotal >= 1000 and subtotal < 3000:
        discount = subtotal*0.05
    else:
        discount = subtotal*0.1
    return discount

def calculate_tax(amount, tax_rate):
    return amount * tax_rate

def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount, tax_rate)
    final_amount = amount_after_discount + tax
    print()
    print("="*30)
    

    for item in items:
        item_subtoatal = item["price"]*item["quantity"]

        print(
            f"Product name: {item["name"]}\n"
            f"Price: {item["price"]}\n"
            f"Quantity: {item["quantity"]}"
            f"Item subtotal: {item_subtoatal}")

    print("-"*25)
    print(f"Subtotal: {subtotal:.2f} Birr")
    print(f"Discount: {discount:.2f} Birr")
    print(f"Tax: {tax:.2f} Birr")
    print(f"Final amount: {final_amount:.2f} Birr")
    print("="*30)


items = []

while True:
    name = input("Enter the product name: ")
    price = float(input("Enter the price for the product: "))
    quantity = int(input("Enter how much quantity you buy: "))

    if price < 0:
        print("Invalid price")
        continue
    if quantity <0:
        print("Invalid quantity")
        continue

    items.append({"name":name, "price":price, "quantity":quantity})
    question = input("Do you wanna continue?(Yes/No)")

    if question.lower() == "yes":
        continue
    else:
        break

tax_rate = float(input("Enter the tax rate(%): "))
if tax_rate < 0 or tax_rate > 100:
    print("Invalid tax rate.")
else:
    tax_rate = tax_rate / 100

generate_receipt(items, tax_rate)
USD_amount = int(input("Enter the USD amount you want to convert: "))
exchang_rate = int(input("Enter the exchange rate: "))
double_line = "=================================="

ETB_amount = USD_amount * exchang_rate

print(f"{double_line}\n{'CURRENCY EXCHANGE':^25}\n{double_line}\n\n{'USD Amount:':<17}{USD_amount}USD\n\n{'Exchange Rate:':<17} 1 USD ={exchang_rate}ETB\n\n{'ETB Amount:':<17}{ETB_amount}ETB\n{double_line}")
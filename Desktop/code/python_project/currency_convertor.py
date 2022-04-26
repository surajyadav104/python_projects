from locale import currency


with open('currency.txt') as f:
    lines = f.readlines()
curr_dict = {}
for line in lines:
    data = line.split("\t")
    curr_dict[data[0]]=data[1]
amount = int(input("Enter the amount in rupees\n"))
print("Enter the name of currency you want to convert from rupees\n Available currency options:\n")
[print(item) for item in curr_dict.keys()]
currency = input("Enter one of the values given above\n")
print(f"{amount} INR is equal to {amount*float(curr_dict[currency])} {currency}")




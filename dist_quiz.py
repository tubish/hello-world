money = {
    'bank': 8564.61,
    'paypal': 1998.21,
    'cash': 480,
    'payoneer': 250.5
}

total_amount = 0
for i in money.values():
    total_amount += i

print(total_amount)

money = {
    'bank': 8564.61,
    'paypal': 1998.21,
    'cash': 480,
    'payoneer': 250.5
}

## First solution using a for loop
total_amount = 0
for value in money.values():
    total_amount += value

print(total_amount)

## Second solution using sum() function and dictionary.values() method
total_amount = sum(money.values())
print(total_amount)
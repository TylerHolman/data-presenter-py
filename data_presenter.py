open_file = open('CupcakeInvoices.csv')
for row in open_file:
    print(row)
open_file.seek(0,0)

for type in open_file:
   item = type.split(',')
   print(item[2])
open_file.seek(0,0)

for row in open_file:
    price = row.split(',')
    total = int(price[3]) * float(price[4])
    print(total)
open_file.seek(0,0)

total = 0
for row in open_file:
    price = row.split(',')
    total = total + (int(price[3]) * float(price[4]))
    print(total)

open_file.close()
    
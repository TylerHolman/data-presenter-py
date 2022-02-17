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
    
## Note: This will need to be run in Replit.com for visualization.
import matplotlib.pyplot as plt 
    
# x axis values 
x = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"] 
# corresponding y axis values 
y = [10,40,32,84,60,52,18] 
    
# plotting the points  
plt.plot(x, y) 
    
# naming the x axis 
plt.xlabel('Day Purchased') 
# naming the y axis 
plt.ylabel('Cupcakes Purchased') 
    
# giving a title to my graph 
plt.title('My Cupcake Sales') 
    
# function to show the plot 
plt.show()     
# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path
Path.cwd()

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as menufile:
    csvreader=csv.reader(menufile, delimiter=',')
    
    header = next(csvreader)
    print(f"{header}, 'profit'")
 # to directly create list of lists menu =list(csvreader)
 # to print the csv file as list  print(menu)
    for line in csvreader:
       # To view the contents of the csvfile print(line)
        
        
        item = line[0]
        category= line[1]
        description= line[2]
        price= float(line[3])
        cost= float(line[4])
 
# @TODO: Calculate profit of each item in the menu data
        profit = price - cost
        
        line.append(profit)
        menu.append(line)
        
 
 #To print the menu list of lists   
    print(menu)
    print("\n")
    

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Read in the sales data into the sales list

with open(sales_filepath, 'r') as salesfile:
        csvreader=csv.reader(salesfile, delimiter=',')
    
        header = next(csvreader)
        print(header)
 
        for line in csvreader:
         # To view the contents of the csvfile print(line)
        
      # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
      # @TODO: Initialize sales data variables
   
            line_num = int(line[0])
            date= line[1]
            cc_num= int(line[2])
            quantity= float(line[3])
            menu_item= line[4]
            sales.append(line)
        
 #   print(sales[:10])



    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
            if menu_item not in report.keys():
                report[menu_item] = {"01-count": quantity, "02-revenue" : 0, "03-cogs": 0, "04-profit": 0
  
            #If the item is in the report, increase the count of quantity, price, cost and profit    
            else:
                report[menu_item]["01-count"] += quantity
                
        
        for a, b in report.items():
            print (a,b)
    
   # Loop through the list containing sales data  
    for sales_row in sales:
        sale_item = sales_row[4]
        quantity = sales_row[3]
        
        # Loop through the list conatining menu data
        for menu_row in menu:
            menu_item = menu_row[0]
            price = menu_row[3]
            cost = menu_row[4]
            
            # Comparing the data in both the lists to get the desired results
            if sale_item == menu_item:
                report[menu_item]["02-revenue"] += (float(price) * int(quantity))
                report[menu_item]["03-cogs"] += (float(cost) * int(quantity))
                report[menu_item]["04-profit"] += (float(price)-float(cost))* int(quantity)
            elif sale_item != menu_item:
                continue  
    
    # Printing the results on the console            
    for a, b in report.items():
        print (a,b)
        
            
      
# @TODO: Write out report to a text file (won't appear on the command line output)
output_path = Path("../../PyRamen/PyRamen.txt")
    
with open(output_path, 'w') as file:
    file.write("Report for PyRamen.\n")
    for key in report:
        file.write(f"{key} {report[key]} \n")
    

   
        






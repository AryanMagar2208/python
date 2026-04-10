import csv

try:
    with open("sample.csv","r") as file:
        reader=csv.reader(file)
        
        count=0
        
        for row in reader:
            count=count+1
            
    print("total no. of row", count)
    
except FileNotFoundError:
    print("file not found")
    
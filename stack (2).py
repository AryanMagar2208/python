import json
import csv

with open('file.json','r') as json_file:
    data=json.load(json_file)
    
    
with open('output.csv', 'w', newline='') as csv_file:
    writer=csv.DicWriter(csv_file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    
print("Converted succefully")



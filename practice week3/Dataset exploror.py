import json
import csv

while True:
    try:
        filename = input("Enter filename: ")
        with open(filename,"r") as file:
            data = csv.reader(file)
            rows=[]
            for row in data:
                rows.append(row)
            break
    except FileNotFoundError:
        print("File not found.")

def num_of_rc():
    if not rows:
        print("CSV file is empty.")
    else:
        num_ofc = len(rows[0])
        num_ofr = len(rows) - 1
        return num_ofc, num_ofr
    
def avg_of_numc():
    for col in range(len(rows[0])):
        total = 0
        count = 0
        missing = 0
        distinct = set()
        for row in range(1,len(rows)):
            val = rows[row][col]

            if val=="":
                missing += 1
                continue
            try:
                num = float(val)
                total += num
                count +=1
            except ValueError:
                total = 0
                count = 0
                distinct.add(val)
        
        if count >0:
            avg = total / count
            rounded_avg = round(avg, 2)
            summary[rows[0][col]]={
                    "Avg": rounded_avg,
                    "Missing Values": missing
                }
        else:
            lit = list(distinct)
            summary[rows[0][col]]= lit  
    return summary
summary={}
summary["Number of columns"]=num_of_rc()[0]
summary["Number of Rows"]=num_of_rc()[1]
summary = avg_of_numc()


sname = filename.split(".")[0]
with open(f"{sname} summary.json", 'w') as file:
    json.dump(summary, file, indent=4)
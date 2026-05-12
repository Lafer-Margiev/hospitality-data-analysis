import csv

def calculate_labor_percentage(sales, labor):
    return (labor / sales) * 100

print("--- Restaurant Labor Analysis Report ---")

with open('mock_sales_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date = row['Date']
        shift = row['Shift']
        sales = float(row['Sales'])
        labor = float(row['Labor_Cost'])
        
        labor_pct = calculate_labor_percentage(sales, labor)
        
        status = "✅ OPTIMAL" if labor_pct <= 18 else "⚠️ HIGH"
        
        print(f"{date} | {shift:6} | Labor: {labor_pct:.1f}% | {status}")

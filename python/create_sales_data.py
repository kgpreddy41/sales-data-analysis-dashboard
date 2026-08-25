import pandas as pd
import random
from datetime import datetime, timedelta

# Number of sales records
num_records = 1000

# Sample data
categories = ["Technology", "Furniture", "Office Supplies"]

products = {
    "Technology": ["Laptop", "Mobile Phone", "Monitor", "Keyboard", "Printer"],
    "Furniture": ["Chair", "Desk", "Table", "Bookcase", "Sofa"],
    "Office Supplies": ["Notebook", "Pen", "Paper", "File Folder", "Stapler"]
}

regions = ["North", "South", "East", "West"]

customers = [
    "Gnaneswara", "sravan", "shyam", "koushik", "srujan",
    "Ananya", "manoj", "Neha", "Ravi", "Pooja"
]

# Starting date
start_date = datetime(2024, 1, 1)

data = []

for i in range(1, num_records + 1):

    category = random.choice(categories)
    product = random.choice(products[category])

    quantity = random.randint(1, 10)

    price = random.randint(100, 5000)

    sales = quantity * price

    discount = round(random.uniform(0, 0.30), 2)

    profit = round(sales * (1 - discount) * random.uniform(0.05, 0.25), 2)

    order_date = start_date + timedelta(days=random.randint(0, 730))

    data.append({
        "Order_ID": f"ORD{i:04d}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Customer_Name": random.choice(customers),
        "Category": category,
        "Product": product,
        "Region": random.choice(regions),
        "Quantity": quantity,
        "Sales": sales,
        "Discount": discount,
        "Profit": profit
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV inside data folder
df.to_csv("data/sales_data.csv", index=False)

print("Sales dataset created successfully!")
print(f"Total records: {len(df)}")
print("\nFirst 5 records:")
print(df.head())
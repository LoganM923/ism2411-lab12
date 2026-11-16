#
# 1. Excel is better for organizing data, making charts and viewing information. Python is better for automating tasks, processing large amounts of data and repeating calculations quickly.
# 2. A business could use an append-mode log to track daily sales. Each sale would add a new entry without deleting previous records, making it easy to review sales history.

# "--- Exercise 2 ---"
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        print(type(row[0]))

#"--- Exercise 3 ---"
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

#"--- Exercise 4 ---"
total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

    revenue = price * quantity
    total_revenue += revenue

    print(f"{product}: {quantity} units * ${price:.2f} = ${revenue:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")

#"--- Exercise 5 ---"
import csv

original_count = 0
written_count = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)
    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print(f"Rows written: {written_count}")
print(f"Original rows: {original_count}")

#"--- Exercise 6 ---"
import csv

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")

#"--- Exercise 7 ---"
import csv

summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity

        if product in summary:
            summary[product] += revenue
        else:
            summary[product] = revenue

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

#"--- Exercise 8 ---"
import csv
from datetime import datetime

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])

        total_revenue += price * quantity

timestamp = datetime.now()

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print(f"Total Revenue: ${total_revenue:.2f}")
print("Run logged successfully!")
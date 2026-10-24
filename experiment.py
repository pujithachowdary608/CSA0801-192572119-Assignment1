"""Task 10: Compare float and Decimal calculations and execution time."""

from decimal import Decimal
from time import perf_counter
import csv


def run_float(n):
    total = 0.0
    for _ in range(n):
        total += float("33.40")
    return total


def run_decimal(n):
    total = Decimal("0.00")
    amount = Decimal("33.40")
    for _ in range(n):
        total += amount
    return total


# Store experiment results
rows = []

print("FLOAT VS DECIMAL EXPERIMENT")
print("-" * 75)

for n in (300, 6000, 150000):

    # Measure float execution time
    start = perf_counter()
    float_total = run_float(n)
    float_time = perf_counter() - start

    # Measure Decimal execution time
    start = perf_counter()
    decimal_total = run_decimal(n)
    decimal_time = perf_counter() - start

    print(f"\nNumber of payments: {n}")
    print(f"Float total:        {float_total:.2f}")
    print(f"Decimal total:      {decimal_total:.2f}")
    print(f"Float time:         {float_time:.6f} seconds")
    print(f"Decimal time:       {decimal_time:.6f} seconds")

    # Add results to the table
    rows.append([
        n,
        repr(float_total),
        str(decimal_total),
        f"{float_time:.6f}",
        f"{decimal_time:.6f}"
    ])


# Save results.csv in the same folder as this program
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "payments",
        "float_total",
        "decimal_total",
        "float_seconds",
        "decimal_seconds"
    ])

    writer.writerows(rows)


# Demonstrate the difference in rounding policies
amounts = [Decimal("0.105")] * 10

per_payment = sum(
    amount.quantize(Decimal("0.01"))
    for amount in amounts
)

final_only = sum(amounts).quantize(Decimal("0.01"))

print("\nROUNDING EXPERIMENT")
print("Round each payment:", per_payment)
print("Round final total: ", final_only)

print("\nResults saved successfully to results.csv")
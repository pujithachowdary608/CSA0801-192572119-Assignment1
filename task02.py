"""Task 2: values, types, arithmetic and monetary precision."""
from decimal import Decimal

values = [10, 10.0, "10", True, [10, 8.5]]
for value in values:
    print(repr(value), "->", type(value).__name__)

print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

payments = ["33.40"] * 1000 + ["0.10"] * 3
def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

print("float  :", total_float(payments))
print("Decimal:", total_decimal(payments))
print("Decimal equality:", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print("Integer paise total:", sum(int(Decimal(x) * 100) for x in payments), "paise")
print("Decimal(float('0.1')):", Decimal(float("0.1")))

"""Task 8: sample hand trace."""
def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(30.00 + fat_steps * 0.40 + snf_steps * 0.30, 2)


def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)
entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
total = 0.0
print("litres | fat | SNF | rate | payment | running total")
for litres, fat, snf in entries:
    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)
    total += amount
    print(f"{litres:6.1f} | {fat:3.1f} | {snf:3.1f} | {rate:5.2f} | {amount:7.2f} | {total:13.2f}")
print(f"Total = ₹{total:.2f}")

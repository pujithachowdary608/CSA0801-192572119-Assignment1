"""Task 6: reusable functions."""
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Return rate per litre based on fat and SNF."""
    fs = round((fat - 3.5) / 0.1)
    ss = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fs * FAT_STEP_VALUE + ss * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    """Return payment for one milk entry."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(entries):
    """Return total payment for entries supplied during ten days."""
    return round(sum(payout(litres, fat, snf) for litres, fat, snf in entries), 2)

if __name__ == "__main__":
    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for row in entries:
        print(f"Entry {row}: rate ₹{rate_per_litre(row[1], row[2]):.2f}; payment ₹{payout(*row):.2f}")
    print(f"Ten-day total: ₹{ten_day_total(entries):.2f}")

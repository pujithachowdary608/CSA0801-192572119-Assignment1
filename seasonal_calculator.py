"""Task 12: seasonal rates and ten-day volume bonus."""
from decimal import Decimal, ROUND_HALF_UP

def money(value):
    """Round money to two decimal places."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf, month):
    """Use seasonal rate card for April-June; otherwise use original card."""
    seasonal = month in (4, 5, 6)
    base = Decimal("32.00") if seasonal else Decimal("30.00")
    fat_step = Decimal("0.45") if seasonal else Decimal("0.40")
    snf_step = Decimal("0.30")
    fat_steps = round((float(fat) - 3.5) / 0.1)
    snf_steps = round((float(snf) - 8.5) / 0.1)
    return money(base + Decimal(fat_steps) * fat_step + Decimal(snf_steps) * snf_step)

def ten_day_payment(entries, month):
    """Calculate payments and apply ₹0.50/L bonus when ten-day volume exceeds 500 L."""
    volume = sum(Decimal(str(row[0])) for row in entries)
    base_total = Decimal("0.00")
    for litres, fat, snf in entries:
        base_total += money(Decimal(str(litres)) * rate_per_litre(fat, snf, month))
    bonus = money(volume * Decimal("0.50")) if volume > 500 else Decimal("0.00")
    return money(base_total + bonus), volume, bonus

if __name__ == "__main__":
    examples = [(300, 4.20, 8.60), (250.5, 3.55, 8.50)]
    for month in (2, 4):
        total, volume, bonus = ten_day_payment(examples, month)
        print(f"month={month}, volume={volume} L, bonus=₹{bonus:.2f}, total=₹{total:.2f}")

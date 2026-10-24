"""Task 9: validated milk payment calculator using Decimal for money."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def money(value):
    """Round a monetary value to two decimal places."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    """Calculate rate using the assignment's 0.1 percentage-point steps."""
    fat_steps = round((float(fat) - 3.5) / 0.1)
    snf_steps = round((float(snf) - 8.5) / 0.1)
    return money(BASE_RATE + Decimal(fat_steps) * FAT_STEP_VALUE + Decimal(snf_steps) * SNF_STEP_VALUE)

def payout(litres, fat, snf):
    """Calculate the rounded payment for one entry."""
    return money(Decimal(str(litres)) * rate_per_litre(fat, snf))

def validate(litres, fat, snf):
    """Raise ValueError when an entry violates assignment validation."""
    if litres < 0:
        raise ValueError("litres cannot be negative")
    if not 2.0 <= fat <= 7.0:
        raise ValueError("fat must be between 2.0 and 7.0")
    if snf < 0:
        raise ValueError("SNF cannot be negative")

def main():
    total = Decimal("0.00")
    entries = int(input("Number of entries: "))
    for i in range(entries):
        try:
            farmer_id = input("Farmer ID: ").strip()
            litres = float(input("Litres: "))
            fat = float(input("Fat %: "))
            snf = float(input("SNF %: "))
            shift = input("Shift (morning/evening): ").strip()
            if not farmer_id or shift.lower() not in {"morning", "evening"}:
                raise ValueError("farmer ID and valid shift are required")
            validate(litres, fat, snf)
            rate = rate_per_litre(fat, snf)
            amount = payout(litres, fat, snf)
            total += amount
            print(f"{farmer_id} {shift}: rate ₹{rate:.2f}, payment ₹{amount:8.2f}")
        except ValueError as exc:
            print("Invalid entry:", exc)
    print(f"Ten-day total: ₹{total:.2f}")

if __name__ == "__main__":
    main()

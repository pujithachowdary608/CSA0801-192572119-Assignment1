"""Task 1: identify the data required by the milk calculator."""
inputs = {
    "farmer_id": ("string", "non-empty identifier"),
    "litres": ("float", "must be >= 0"),
    "fat": ("float", "must be between 2.0 and 7.0 inclusive"),
    "snf": ("float", "must be a plausible non-negative percentage; confirm upper bound with faculty"),
    "shift": ("string", "for example morning or evening"),
}
outputs = ["rate_per_litre (₹)", "payment (₹)", "ten_day_total (₹)"]
constants = {"BASE_RATE": 30.00, "STANDARD_FAT": 3.5, "STANDARD_SNF": 8.5,
             "FAT_STEP_VALUE": 0.40, "SNF_STEP_VALUE": 0.30,
             "FAT_MIN": 2.0, "FAT_MAX": 7.0}
print("INPUTS")
for name, details in inputs.items():
    print(f"{name}: type={details[0]}, rule={details[1]}")
print("\nOUTPUTS:", ", ".join(outputs))
print("CONSTANTS:", constants)
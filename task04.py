"""Task 4: expressions, rounding and operator behaviour."""
import math

def compare_methods(fat):
    raw = (fat - 3.5) / 0.1
    print(f"fat={fat}: raw={raw}, round={round(raw)}, int={int(raw)}, floor={math.floor(raw)}")

fat, snf, litres = 4.2, 8.7, 8.5
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = 30.0 + fat_steps * 0.40 + snf_steps * 0.30
print("fat steps:", fat_steps, "SNF steps:", snf_steps)
print(f"rate=₹{rate:.2f}; payment=₹{litres * rate:.2f}")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("round(2.5) =", round(2.5), "(Python uses ties-to-even)")
print("-7 / 2 =", -7 / 2, "; -7 // 2 =", -7 // 2)
compare_methods(4.2)
compare_methods(3.1)
print("fat valid:", 2.0 <= fat <= 7.0)
print("both quality checks:", (2.0 <= fat <= 7.0) and (snf > 0))
print("precedence example:", -2 ** 2, "versus", (-2) ** 2)

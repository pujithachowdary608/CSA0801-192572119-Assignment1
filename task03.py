"""Task 3: named constants and variable assignment."""
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
FAT_MIN = 2.0
FAT_MAX = 7.0

value = 10
print("Integer:", value, type(value).__name__)
value = "ten"
print("String:", value, type(value).__name__)
a, b = 3, 8
a, b = b, a
print("Swapped values:", a, b)
RATE_CARD = {"base": BASE_RATE, "fat": FAT_STEP_VALUE, "snf": SNF_STEP_VALUE}
print("Rate card:", RATE_CARD)

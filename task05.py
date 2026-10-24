"""Task 5: safe input conversion and validation."""
def read_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Enter a number using a decimal point, e.g. 8.5.")

def main():
    litres = read_float("Enter litres: ")
    fat = read_float("Enter fat percentage: ")
    snf = read_float("Enter SNF percentage: ")
    if litres < 0:
        print("Error: litres cannot be negative.")
    elif not 2.0 <= fat <= 7.0:
        print("Error: fat must be between 2.0 and 7.0.")
    elif snf < 0:
        print("Error: SNF cannot be negative.")
    else:
        print(f"Litres: {litres:6.2f}; Fat: {fat:4.2f}; SNF: {snf:4.2f}")

if __name__ == "__main__":
    main()

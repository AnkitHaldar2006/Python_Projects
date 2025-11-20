import math

def calculate_ncr(n, r):
    """Calculate nCr using factorial formula."""
    if r > n or n < 0 or r < 0:
        return None
    return math.comb(n, r)  # Python 3.8+ has built-in comb()

def main():
    while True:
        print("\n--- NCR Calculator ---")
        print("1. Calculate nCr")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ").strip()
        
        if choice == "1":
            try:
                n = int(input("Enter n (total items): "))
                r = int(input("Enter r (items chosen): "))
                
                result = calculate_ncr(n, r)
                if result is None:
                    print("❌ Invalid input: r cannot be greater than n, and both must be non-negative.")
                else:
                    print(f"✅ {n}C{r} = {result}")
            except ValueError:
                print("⚠️ Please enter valid integers.")
        
        elif choice == "2":
            print("Exiting NCR Calculator. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
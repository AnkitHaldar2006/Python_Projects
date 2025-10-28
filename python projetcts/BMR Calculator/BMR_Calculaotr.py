def calculate_bmr(gender, weight_kg, height_cm, age_years):
    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age_years + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age_years - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    return bmr

def main():
    print("Welcome to the BMR Calculator!")
    gender = input("Enter your gender (male/female): ").strip()
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age in years: "))

    try:
        bmr = calculate_bmr(gender, weight, height, age)
        print(f"\nYour Basal Metabolic Rate (BMR) is: {bmr:.2f} calories/day")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
def calculate_bmi(scale, weight, height):
    #Function to calculate BMI
    if scale == "metric":
        return weight / (height ** 2)
    if scale == "standard":
        heightin = height * 12 
        return 703 * weight / (heightin ** 2)

def analyze(bmi):
    #Function to analyze BMI
    
    if bmi < 18.5:
        return "Under weight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Over weight"
    else:
        return "Obese"

def main():
    scale = input("Choose scale Metric or Standard: ")

    scale = scale.lower()

    if scale == "metric":
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    
    if scale == "standard":
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in feet inches: "))

    bmi = calculate_bmi(scale, weight, height)
    resultBMI = analyze(bmi)

    print("Your BMI is:", bmi)
    print("Analysis:", resultBMI)

if __name__ == "__main__":
    main()